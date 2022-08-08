import requests
from datetime import *


resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print(f"Sorry! Could not get details! Status Code : {resp.status_code}")
    exit()

countries = resp.json()  # convert array of json objects to list[dict]

for c in countries:
    capital = c['capital'][0] if 'capital' in c else 'Unknown'
    print(f"{c['name']['common']:50} {capital:30} {c['region']:15} {c['population']:12}")



