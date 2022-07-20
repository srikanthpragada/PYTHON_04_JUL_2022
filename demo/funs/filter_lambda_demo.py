names = ['JavaScript', 'Java', 'Python', 'C#']

for n in filter(lambda v: len(v) > 5, names):
    print(n)
