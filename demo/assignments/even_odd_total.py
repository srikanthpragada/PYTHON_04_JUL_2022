even_total = odd_total = 0

for n in range(5):
    n = int(input("Enter the Number :"))
    if n % 2 == 0:
        even_total += n
    else:
        odd_total += n

print(f"Even total : {even_total}, Odd total : {odd_total}")
