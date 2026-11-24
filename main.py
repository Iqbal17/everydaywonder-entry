"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

FINAL SENTENCE (132 characters, hand-counted letter by letter, gate 1-200):
"The escalator handrail moves a little faster than the steps, so for
thirty seconds my hand is quietly travelling into my own future."

Hand count, in three chunks (recounted twice, independently):
  "The escalator handrail moves" = 28
    The(3) space(1) escalator(9) space(1) handrail(8) space(1) moves(5)
  " a little faster than the steps," = 32
    space(1) a(1) space(1) little(6) space(1) faster(6) space(1)
    than(4) space(1) the(3) space(1) steps,(6)
  " so for thirty seconds my hand is quietly travelling into my own
  future." = 72
    space(1) so(2) space(1) for(3) space(1) thirty(6) space(1)
    seconds(7) space(1) my(2) space(1) hand(4) space(1) is(2) space(1)
    quietly(7) space(1) travelling(10) space(1) into(4) space(1)
    my(2) space(1) own(3) space(1) future.(7)
  Total: 28 + 32 + 72 = 132 characters. One sentence, one clear read.

DECISION RECORD — candidates written from scratch, weighed against the
judge brief (1. small everyday moment of wonder; 2. angle the reader has
not met before, phrasing itself the surprise; 3. surprise lands in one
read, single clear sentence; 4. grounded in something real and specific;
5. every word working, no filler, no worn phrase). The brief's own
examples (lift door on a stranger's song, kettle click, puddle holding
the sky) were deliberately NOT reused — copying the brief reads as
copying the brief.

A. "The escalator handrail moves a little faster than the steps, so for
   thirty seconds my hand is quietly travelling into my own future."
   (132 chars)
   - WINNER. The observation is real and checkable: a handrail genuinely
     drifts a little faster than the steps, so your hand creeps forward
     of your body (criterion 4). The angle is the turn: a mundane
     mechanical drift becomes time travel, and "quietly" makes it a
     private wonder rather than a physics fact (criterion 2). The
     surprise lands in the last four words, in a single read
     (criterion 3). Every word earns its place (criterion 5).

B. "The supermarket doors opened before I reached them, and I walked
   through feeling briefly like someone the building had been
   expecting." (134 chars)
   - Good and grounded (automatic doors really do open early), and
     "someone the building had been expecting" is a warm turn. Loses:
     the surprise is a feeling ("feeling briefly like") rather than an
     image, so it lands softer than A, and "briefly" apologises for its
     own wonder (criterion 2 and 3).

C. "My reflection in the bus window kept walking after I sat down, and
   for a block I watched myself go on without me." (113 chars)
   - The strongest raw strangeness of the five ("watched myself go on
     without me"). Loses: a reflection does not actually keep walking
     after you sit down, so the image is dreamlike rather than grounded
     in something real (criterion 4), and the judge's brief rewards the
     everyday made strange, not the everyday replaced by a dream.

D. "A raindrop raced another down the bus window, and I realised I had
   been rooting for water." (90 chars)
   - Tightest and most playful; watching raindrops race is real and
     universal, and "rooting for water" is a genuine small laugh.
     Loses: the raindrop race is a familiar pastime, so the angle is
     one the reader HAS met before (criterion 2); the surprise is mild
     where A and C are startling.

E. "The washing machine finished its spin and sat there humming the
   last note of a song it had never been taught." (109 chars)
   - Lyrical and specific, and "the last note of a song it had never
     been taught" is a lovely phrase. Loses: a humming appliance is a
     familiar personification (criterion 2), and "never been taught" is
     abstract where the brief wants the surprise grounded (criterion 4).

WRITING PASS 1 (draft): A as written above, 132 chars. Critique: the
opening is plain observation ("moves a little faster than the steps"),
which is exactly what the brief wants — the wonder must grow out of the
everyday, not be announced. "Thirty seconds" is the right scale: long
enough to notice, short enough to be one ride. "Quietly" is the word
that turns a mechanical fact into a private moment; without it the
sentence is a physics note.

WRITING PASS 2 (tighten): three changes tested, all rejected:
  - "moves" -> "runs" (131 chars): "runs" is the standard verb for a
    handrail, but it puts the sentence in the register of machinery;
    "moves" keeps it in the register of quiet observation. Rejected.
  - Cut "quietly" (124 chars): the sentence becomes a bare fact and the
    wonder drains out of it. Rejected.
  - "into my own future" -> "ahead of me" (126 chars): flatter, and it
    kills the turn the whole sentence is built for. Rejected.
  Verdict: keep pass 1 exactly. 132 characters, inside the 1-200 gate.

REVISION (fix pass, after kit check flagged thinking_revised): the
sentence above is unchanged — only the code below was restructured.
Gate validation (1-200 chars, exactly one sentence, no stray
whitespace) moved out of main() into validate_entry(), output-path
resolution into resolve_output_path(), and the write itself into
write_entry(), so a future edit that breaks the gate fails loudly
here instead of silently shipping a bad entry.
"""

import os

LINE = (
    "The escalator handrail moves a little faster than the steps, so for "
    "thirty seconds my hand is quietly travelling into my own future."
)


# Gate for this bounty: a single sentence, 1-200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(line: str) -> None:
    """Fail loudly if the entry breaks the bounty gate.

    The sentence itself is fixed by the decision record above; this
    guard exists so any future edit that changes its length or splits
    it into two sentences is caught here instead of at judging time.
    """
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate"
        )
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def resolve_output_path() -> str:
    """Output path, honouring MAKEFUN_OUTPUT_DIR when the harness sets it."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str) -> None:
    validate_entry(LINE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


def main() -> None:
    path = resolve_output_path()
    write_entry(path)
    print(f"Verified: {len(LINE)} characters, 1 sentence.")
    print(LINE)


if __name__ == "__main__":
    main()
