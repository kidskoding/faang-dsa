# Astranis warm-up: telemetry packet parsing.
# Frame layout (big-endian) is in docs/PACKET_PARSING_WARMUP.md.
#
#  offset  size  field
#    0      2    sync word 0xACE1
#    2      1    version (high nibble) | msg_type (low nibble)
#    3      1    spacecraft id
#    4      2    sequence counter
#    6      2    payload length
#    8      N    payload
#   8+N     1    checksum = sum(bytes[0 : 8+N]) % 256

SYNC_WORD = 0xACE1
HEADER_SIZE = 8


def parse_frame(data: bytes) -> dict | None:
    # Parse one frame from the front of data.
    # Return None on a bad sync word, a truncated buffer, or a checksum mismatch.
    # Keys: version, msg_type, spacecraft_id, sequence, payload

    raise NotImplementedError


def parse_stream(data: bytes) -> list[dict]:
    # Scan a concatenated blob that may start mid-frame and contain corruption.
    # Parse every frame you can, skip what you cannot, never raise.

    raise NotImplementedError


def decode_payload(payload: bytes) -> dict:
    # Type-3 payload: int16 temperature in hundredths of a degree C,
    # uint16 bus voltage in millivolts, uint32 uptime in seconds.
    # Return real units: temperature_c, voltage_v, uptime_s

    raise NotImplementedError


class FrameBuffer:
    # Frames arrive split across reads. Buffer partial frames and return
    # whichever ones completed on this call.

    def __init__(self) -> None:
        raise NotImplementedError

    def feed(self, chunk: bytes) -> list[dict]:
        raise NotImplementedError
