#!/usr/bin/env python3
from typing import *
from os import listdir, rename
from shutil import rmtree
from os.path import abspath
import random
from subprocess import run

i_dont_want_to: List[str] = []
projects = [p for p in listdir("/mnt/d/projects") if not p.startswith(".")]

# print("Got projects:\n" + "\n- ".join(projects))

no_dash_next = False
while True:
    selected = random.choice([p for p in projects if p not in i_dont_want_to])
    ans = (
        input(
            ("- " if not no_dash_next else "  ") + f"You will work on {selected!r}!\n- "
        )
        .strip()
        .lower()
        .replace('"', "")
    )
    if ans == "no":
        i_dont_want_to += [selected]
        print("- No? Oh-okay, well...")
    elif ans.startswith("delete"):
        if input("- You sure?\n- ").strip().lower() == "yes":
            print("- M'kay")
            rmtree(selected)
        else:
            print("- Thought so.")
    elif ans.startswith("archive"):
        print("- Okay, moving this project to .archived/")
        rename(f"/mnt/d/projects/{selected}", f"/mnt/d/projects/.archived/{selected}")
    else:
        run(["code", abspath(selected)], shell=True)
        break
    no_dash_next = True
