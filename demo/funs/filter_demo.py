def islongname(name):
    return len(name) > 5


def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


names = ['JavaScript', 'Java', 'Python', 'C#']

for n in filter(islongname, names):
    print(n)

for n in filter(isprime, [10, 3, 9, 13, 37, 45]):
    print(n)
