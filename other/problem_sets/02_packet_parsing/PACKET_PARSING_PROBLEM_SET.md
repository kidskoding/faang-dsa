# Astranis Warm-Up — Telemetry Packet Parsing

Prep for a "Coding (Python Packet)" round. Written 2026-08-17, a few hours
before the interview.

The round title is ambiguous: "packet" may mean a packet of problems, or a
binary data packet. At a satellite comms company the second reading is likely,
and it is the one that needs preparation, so that is what this drills.

## The Format

A ground station receives telemetry frames over a serial link. Every frame is
laid out big-endian:

```text
 offset  size  field
 ------  ----  --------------------------------------------------
   0      2    sync word, always 0xACE1 — frames start here
   2      1    version, high nibble; message type, low nibble
   3      1    spacecraft id
   4      2    sequence counter, wraps at 65535
   6      2    payload length in bytes
   8      N    payload
  8+N     1    checksum: sum of every byte from offset 0 to 8+N-1, mod 256
```

A frame is valid when the sync word matches, enough bytes are present for the
declared payload, and the checksum agrees.

## The Exercises

Work in `packet_problems.py`. Do them in order — each one is the kind of follow-up an
interviewer adds once the previous part works.

1. **`parse_frame(data: bytes) -> dict | None`** — parse one frame from the
   front of `data`. Return a dict with `version`, `msg_type`, `spacecraft_id`,
   `sequence`, `payload`. Return `None` if the sync word is wrong, the buffer is
   truncated, or the checksum fails.

2. **`parse_stream(data: bytes) -> list[dict]`** — the link delivers a
   concatenated byte blob that may start mid-frame and may contain corruption.
   Scan for sync words, parse what you can, skip what you cannot, and never
   raise.

3. **`decode_payload(payload: bytes) -> dict`** — the payload of a type-3
   message is three sensor readings: a signed 16-bit temperature in
   hundredths of a degree Celsius, an unsigned 16-bit bus voltage in
   millivolts, and an unsigned 32-bit uptime in seconds. Return them in real
   units.

4. **`FrameBuffer`** — packets arrive split across reads. Implement a class with
   `feed(chunk: bytes) -> list[dict]` that buffers partial frames and returns
   whichever frames completed on this call.

Run the tests as you go:

```bash
uv run pytest mock-interviews/astranis/01_interview -q
```

## Python You Want Ready

```python
import struct

struct.unpack('>HBBHH', data[:8])   # big-endian: H=uint16 B=uint8 I=uint32
struct.unpack('>h', b)[0]           # lowercase = signed
struct.calcsize('>HBBHH')           # 8

int.from_bytes(data[0:2], 'big')
(1234).to_bytes(2, 'big')

(byte >> 4) & 0x0F                  # high nibble
byte & 0x0F                         # low nibble
sum(data[:n]) & 0xFF                # checksum

data.find(b'\xac\xe1', start)       # locate the next sync word
```

Format characters: `B` uint8, `H` uint16, `I` uint32, `Q` uint64; lowercase is
signed. `>` big-endian, `<` little-endian. Watch that Python has no max-heap and
no unsigned int — signedness comes from the format character.

## What They Are Watching For

Ask about **endianness** before writing anything. Then ask what should happen to
a **malformed frame** — skip, raise, or resynchronize. Both questions signal you
have handled a real wire format before.

Then: validate the length field before slicing, name the fields instead of
indexing raw offsets, and say out loud what happens on truncated input. Code
that survives a bad frame from orbit is the actual bar here, more than an
optimal complexity.

## If It Turns Out To Be A Problem Set

Then it is ordinary easy-to-medium Python and the repo already covers it. Warm
up with hashing instead:

```bash
uv run pytest 01_arrays_and_hashing/tests/test_hashing_problems.py -k "two_sum or valid_anagram" -q
```
