from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = bs.find_all("a")
print(f"No. of links : {len(links)}")

for link in links:
    href = link['href']
    if href == '#':
        continue

    if href.startswith("javascript:"):
        continue

    if not href.startswith("http"):
        href = WEBSITE + ('/' if not href.startswith("/") else '') + href

    print(href)
