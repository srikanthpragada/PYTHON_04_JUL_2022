from bs4 import BeautifulSoup

with open("courses.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")

courses = bs.find_all("course")
for course in courses:
    title = course.title.text
    duration = course.duration.text
    fee = int(course.fee.text)
    print(f"{title:50} {duration:15} {fee:6} INR")
