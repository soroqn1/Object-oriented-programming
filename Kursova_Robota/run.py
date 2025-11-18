#!/usr/bin/env python
import sys
from pathlib import Path

src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

for mod in list(sys.modules.keys()):
    if mod.startswith("task_planner"):
        del sys.modules[mod]

from task_planner.pl.cli import main, member_add
import inspect

print(f"DEBUG: Loaded member_add from: {member_add.__code__.co_filename}")
sig = inspect.signature(member_add)
print(f"DEBUG: member_add signature: {sig}")

if __name__ == "__main__":
    main()
