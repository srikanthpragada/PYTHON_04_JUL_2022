from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = bs.find_all("a")
print(f"No. of links : {len(links)}")

for link in links:
    href = link['href']
    if href.startswith("javascript:"):
        continue
    if not href.startswith("http"):
        href = WEBSITE + href
    print(href)