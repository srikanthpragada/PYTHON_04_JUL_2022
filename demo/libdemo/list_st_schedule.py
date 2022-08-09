from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find(id='ctl00_ContentPlaceHolder1_GridView2')
rows = table.find_all("tr")[1:]  # ignore headings and take the rest
for row in rows:
    cols = row.find_all("td")
    title = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    print(f"{title:50} {timings:20} {stdate:10}")
