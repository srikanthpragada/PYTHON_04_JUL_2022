from datetime import *


def convert_date(st):
    try:
        d = datetime.strptime(st, '%d-%m-%Y')
        return d
    except:
        try:
            d = datetime.strptime(st, '%d-%b-%Y')
            return d
        except:
            raise ValueError("Invalid Date!")


f = open("tasks.txt", "rt")
for line in f.readlines():
    parts = line.strip().split(",")
    # print(parts)
    try:
        stdate = convert_date(parts[1])
        enddate = convert_date(parts[2])
        days = (enddate - stdate).days
        print(f"{parts[0]:30}  {days:3}")
    except:
        pass

f.close()
