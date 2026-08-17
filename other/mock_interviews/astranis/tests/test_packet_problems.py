import struct

from packet_problems import HEADER_SIZE, SYNC_WORD, FrameBuffer, decode_payload, parse_frame, parse_stream


def build_frame(
    payload: bytes,
    *,
    version: int = 1,
    msg_type: int = 3,
    spacecraft_id: int = 7,
    sequence: int = 42,
    corrupt_checksum: bool = False,
) -> bytes:
    header = struct.pack(
        ">HBBHH",
        SYNC_WORD,
        (version << 4) | msg_type,
        spacecraft_id,
        sequence,
        len(payload),
    )
    body = header + payload
    checksum = sum(body) % 256
    if corrupt_checksum:
        checksum = (checksum + 1) % 256
    return body + bytes([checksum])


def test_parse_frame_reads_every_header_field():
    frame = build_frame(b"\x01\x02")

    assert parse_frame(frame) == {
        "version": 1,
        "msg_type": 3,
        "spacecraft_id": 7,
        "sequence": 42,
        "payload": b"\x01\x02",
    }


def test_parse_frame_empty_payload():
    assert parse_frame(build_frame(b""))["payload"] == b""


def test_parse_frame_rejects_bad_sync_word():
    frame = bytearray(build_frame(b"\x01"))
    frame[0] = 0x00

    assert parse_frame(bytes(frame)) is None


def test_parse_frame_rejects_truncated_buffer():
    assert parse_frame(build_frame(b"\x01\x02\x03")[:-2]) is None


def test_parse_frame_rejects_short_header():
    assert parse_frame(b"\xac\xe1\x13") is None


def test_parse_frame_rejects_bad_checksum():
    assert parse_frame(build_frame(b"\x09", corrupt_checksum=True)) is None


def test_parse_stream_reads_back_to_back_frames():
    stream = build_frame(b"\xaa", sequence=1) + build_frame(b"\xbb\xcc", sequence=2)
    frames = parse_stream(stream)

    assert [f["sequence"] for f in frames] == [1, 2]
    assert [f["payload"] for f in frames] == [b"\xaa", b"\xbb\xcc"]


def test_parse_stream_skips_leading_garbage():
    stream = b"\xde\xad\xbe\xef" + build_frame(b"\xaa", sequence=5)

    assert [f["sequence"] for f in parse_stream(stream)] == [5]


def test_parse_stream_recovers_after_a_corrupt_frame():
    stream = (
        build_frame(b"\xaa", sequence=1)
        + build_frame(b"\xbb", sequence=2, corrupt_checksum=True)
        + build_frame(b"\xcc", sequence=3)
    )
    sequences = [f["sequence"] for f in parse_stream(stream)]

    assert 1 in sequences
    assert 3 in sequences
    assert 2 not in sequences


def test_parse_stream_empty_input():
    assert parse_stream(b"") == []


def test_decode_payload_positive_temperature():
    payload = struct.pack(">hHI", 2350, 28000, 86400)

    assert decode_payload(payload) == {
        "temperature_c": 23.5,
        "voltage_v": 28.0,
        "uptime_s": 86400,
    }


def test_decode_payload_negative_temperature():
    payload = struct.pack(">hHI", -1875, 12000, 0)
    decoded = decode_payload(payload)

    assert decoded["temperature_c"] == -18.75
    assert decoded["voltage_v"] == 12.0
    assert decoded["uptime_s"] == 0


def test_frame_buffer_returns_frame_once_complete():
    frame = build_frame(b"\xaa\xbb", sequence=9)
    buffer = FrameBuffer()

    assert buffer.feed(frame[:5]) == []
    completed = buffer.feed(frame[5:])

    assert [f["sequence"] for f in completed] == [9]


def test_frame_buffer_handles_two_frames_in_one_chunk():
    stream = build_frame(b"\xaa", sequence=1) + build_frame(b"\xbb", sequence=2)
    buffer = FrameBuffer()

    assert [f["sequence"] for f in buffer.feed(stream)] == [1, 2]


def test_frame_buffer_splits_across_three_reads():
    frame = build_frame(b"\x01\x02\x03\x04", sequence=77)
    buffer = FrameBuffer()
    seen = []
    for chunk in (frame[:3], frame[3:7], frame[7:]):
        seen.extend(buffer.feed(chunk))

    assert [f["sequence"] for f in seen] == [77]


def test_header_size_matches_the_layout():
    assert HEADER_SIZE == struct.calcsize(">HBBHH")
