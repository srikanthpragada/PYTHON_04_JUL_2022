nums = ['10', '30', '40', '50']
# code + marks
marks = ['j80', 'p60', 'c76']


def take_marks(s):
    return int(s[1:])


# total = 0
# for n in nums:
#     total += int(n)
#
# print(total)

print(sum(map(int, nums)))
print(sum(map(take_marks, marks)))

marks = '40,60,90,87'


def ispass(m):
    return m > 50


map_obj = map(int, marks.split(","))
total = sum(filter(ispass, map_obj))
print(total)
