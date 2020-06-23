#!/usr/bin/env python3

PROJECTS_DIRECTORY = "/mnt/d/projects"
ARCHIVED_PROJECTS_DIRECTORY = "/mnt/d/projects/.archived"
# This will be executed with one positional argument, the chosen project's directory.
CODE_EDITOR_COMMAND = "code"

from typing import *
from os import listdir, rename, path
from shutil import rmtree
from os.path import abspath
import random
from subprocess import run

i_dont_want_to: List[str] = []
projects = [p for p in listdir(PROJECTS_DIRECTORY) if not p.startswith(".")]

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
        if input("- You sure?\n- ").strip().lower().startswith('y'):
            print(f"- M'kay! Everyone, say goodbye to {selected}!")
            print(f"- Goodbyyyyyyyyye")
            rmtree(path.join(PROJECTS_DIRECTORY, selected))
            print(f"Narrator: user-kun didn't realize its mistake, {selected!r} would make the rest of his life a nightmare")
            i_dont_want_to += [selected]
        else:
            print("- Thought so.")
    elif ans.startswith("archive"):
        print("- Okay, I'll archive it.")
        rename(path.join(PROJECTS_DIRECTORY, selected), path.join(ARCHIVED_PROJECTS_DIRECTORY, selected))
        i_dont_want_to += [selected]
    else:
        run(f'code "{path.join(PROJECTS_DIRECTORY, selected)}"', shell=True)
        break
    no_dash_next = True
