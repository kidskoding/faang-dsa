# Astranis — Software Engineer Intern, Enterprise Systems

Prep for the live "Coding (Python Packet)" round, 45–60 minutes, two
interviewers. The team builds internal tooling, database architecture, and
analytics pipelines behind the design, procurement, assembly, and testing of
micro-geostationary satellites.

Two write-ups on this track agree on the shape: practical Python and data
manipulation rather than abstract algorithms, with weight on stream and window
calculations, parsing messy input, light object-oriented state, and explaining
yourself while you code. Neither source is verified, so treat the themes as
priors and not a syllabus.

## Reported Themes

| Theme                                                                            | Drilled by                                                                          |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Stream and window calculations — rolling metrics, anomalies over a moving window | `MovingAverage` and `RecentCounter` in module 03, `max_sliding_window` in module 04 |
| Parsing and reconciling messy data                                               | `INTERNAL_TOOLING.md` here                                                          |
| Object-oriented state tracking                                                   | `InventoryTracker` here; `StockPrice` and `SnapshotArray` in module 18              |
| Binary or telemetry packet parsing                                               | `PACKET_PARSING.md` here                                                            |
| Debugging a deliberately broken snippet                                          | not drilled — see below                                                             |

## The Sets

**`INTERNAL_TOOLING.md`** — the likelier one for this role. Two systems disagree
about parts inventory, procurement's export is dirty, and you write the tool
that reconciles them. Five exercises: clean, aggregate, join, rank, then hold
running state. Nothing may raise on bad input.

**`PACKET_PARSING.md`** — a telemetry wire format: fixed-offset header fields, a
length field, a checksum, and frames that arrive split across reads. Less likely
for Enterprise Systems than for a flight-software team, but "packet" is in the
round's name and the `struct` fluency is cheap to acquire.

```bash
uv run pytest other/mock_interviews/astranis -q
```

## On The Debug Round

No exercise here drills this, because reading someone else's broken code is a
different skill from writing your own. The habits that carry it: read the whole
snippet before touching anything, say what it is *supposed* to do, then check
off-by-ones, mutation during iteration, mutable default arguments, state shared
across instances, and swallowed exceptions. Voice each hypothesis before you
test it — on a debug question the reasoning is the answer, not the patch.

## What Actually Gets Scored

Ask about the **data** before writing anything. Can fields be missing? Can an id
repeat within one export? What happens when two sources conflict — trust one,
take the max, or flag it? For an internal-tools team those questions are the
technical signal, not a preamble to it.

Then: reach for `defaultdict` and `Counter` instead of hand-rolled key checks,
name intermediate values rather than chaining comprehensions three deep, handle
empty input out loud before being asked, and state complexity unprompted.

Both write-ups also flag a resume deep dive. Have three projects ready — what it
did, one design decision and why, one thing that broke, what you would change.
Astranis is small enough that "why did you build it that way" carries real
weight.
