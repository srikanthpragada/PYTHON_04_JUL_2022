import re

with open("story2.txt", "rt") as f:
    contents = f.read()

newcontents = re.sub(' +', ' ', contents)
newcontents = re.sub('\n+', '\n', newcontents)
print(newcontents)


