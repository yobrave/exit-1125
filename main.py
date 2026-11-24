"""exit-1125: resignation one-liner; walks the plank through a 140-char gate."""

import json
import os

DOOR = "entry.txt"
BOUND = 140
SUBJECT = "one-line resignation"


def pick_up(folder):
    memo = open(os.path.join(folder, DOOR), encoding="utf-8")
    text = memo.read().strip()
    memo.close()
    return text


def set_down(folder, text):
    zone = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(zone, exist_ok=True)
    desk = os.path.join(zone, DOOR)
    with open(desk, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return desk


notice = pick_up(os.path.dirname(os.path.abspath(__file__)))
size = len(notice)
cleared = False
while not cleared:
    cleared = 1 <= size <= BOUND
    if not cleared:
        raise SystemExit("the notice does not fit through the door: %d chars" % size)
print(json.dumps({"subject": SUBJECT, "notice": notice[:38], "size": size, "desk": set_down(os.path.dirname(os.path.abspath(__file__)), notice)}))
