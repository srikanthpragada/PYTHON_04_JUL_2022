from bs4 import BeautifulSoup

with open("courses.html", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "html.parser")
trainer = bs.h2.text
print(trainer)

rows = bs.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    print(f"{cols[0].text:20}  {cols[1].text:10}  {cols[2].text}")
