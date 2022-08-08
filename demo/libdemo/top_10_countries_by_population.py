import requests
from datetime import *

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print(f"Sorry! Could not get details! Status Code : {resp.status_code}")
    exit()

countries = resp.json()  # convert array of json objects to list[dict]

for c in sorted(countries, key=lambda country: country['population'], reverse=True)[:10]:
    population = c['population']
    area = c['area']
    density = population // area
    print(f"{c['name']['common']:50} {c['region']:15} {population:12.0f}  {area:12.0f}  {density:5.0f}")
