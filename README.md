# you-will-work-on
When you have a bunch of projects but don't known which one to work on right now.

## Installation

You can be fancy and `git clone` this repo, or just download [the script](https://raw.githubusercontent.com/ewen-lbh/you-will-work-on/master/you-will-work-on.py) (or even just copy-paste its content into a file)

Mark the script as executable (linux-based OSes only):

```sh-session
chmod +x you-will-work-on.py
```

Then edit the script to input your own settings, see the three constants at the top:

```python
PROJECTS_DIRECTORY = "/mnt/d/projects" # <---- Where all of your projects are
ARCHIVED_PROJECTS_DIRECTORY = "/mnt/d/projects/.archived" # <----- Where all of your _archived_ projects are
# This will be executed with one position argument, the chosen project's directory.
CODE_EDITOR_COMMAND = "code"
```

## Usage

Execute it, duh. Then, you have several things you can answer with:

- "no" to get select another project (it won't select the same one twice)
- "archive" to move the folder to `ARCHIVED_PROJECTS_DIRECTORY`
- "delete" to delete the folder **permanently** (will ask you for a confirmation)
- anything else to open the project using `CODE_EDITOR_PROGRAM`
