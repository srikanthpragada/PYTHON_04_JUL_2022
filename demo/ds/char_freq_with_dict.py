st = "this is to test"

chars = {}

for c in st:
    cnt = chars.get(c, 0)
    chars[c] = cnt + 1

for c, cnt in sorted(chars.items()):
    print(c, cnt)
