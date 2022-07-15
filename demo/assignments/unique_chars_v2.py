chars = set()  # empty set
for i in range(5):
    st = input("Enter string :")
    chars = chars | set(st)

print(chars)
