even_total = 0

for n in range(5):
    n = int(input("Enter the Number :"))
    if n % 2 == 0:
        even_total += n

print(f"The Sum of Even Numbers :     {even_total}")
