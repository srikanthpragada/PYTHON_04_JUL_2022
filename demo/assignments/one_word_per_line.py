st = "This is to test how to print one word per line"

for c in st:
    if c == ' ':
        print()  # print new line
    else:
        print(c, end='')

for w in st.split(" "):
    print(w)
