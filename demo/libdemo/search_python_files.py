import os

STARTDIR = r"c:\classroom\jul4\demo"
SEARCH_PATTERNS = "class"  # ("with", "yield", "super")


def filecontainspattern(filename: str, patterns: tuple | str) -> bool:
    with open(filename, "rt") as f:
        contents = f.read()
        if isinstance(patterns, str):
            return patterns in contents

        for p in patterns:
            if p in contents:
                return True

        return False


g = os.walk(STARTDIR)

for dname, dirs, files in g:
    for f in files:
        if f.endswith(".py"):
            filename = dname + "\\" + f
            if filecontainspattern(filename, SEARCH_PATTERNS):
                print(filename)
