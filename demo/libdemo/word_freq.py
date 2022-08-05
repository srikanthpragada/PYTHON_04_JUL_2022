import re

with open("story.txt", "rt") as f:
    contents = f.read().upper()

words = re.findall('\w+', contents)

for w in sorted(set(words)):
    print(f"{w} - {words.count(w)}")
