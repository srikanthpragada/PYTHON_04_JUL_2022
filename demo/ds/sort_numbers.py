nums = []
while True:
    num = int(input("Enter number [0 to stop]:"))
    if num == 0:
        break
    if num not in nums:
        nums.append(num)

# nums.sort()

for n in sorted(nums):
    print(n, end=' ')
