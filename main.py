"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import shutil

PITCH = (
    "SnoozeBroker rents idle AI agents as professional Zoom attendees "
    "who nod, take no notes, and bill startups ten cents a minute "
    "for a warm body on the call."
)


def main():
    if not (1 <= len(PITCH) <= 200):
        raise ValueError("pitch must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
