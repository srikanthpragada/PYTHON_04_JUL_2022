import requests
from datetime import *

user = "srikanthpragada"
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print(f"Sorry! Could not get details! Status Code : {resp.status_code}")
    exit()

details = resp.json()  # convert json to dict

createdat = details['created_at']
created_date_str = createdat[:10]
created_date = datetime.strptime(created_date_str, '%Y-%m-%d')
current_date = datetime.now()
years = (current_date - created_date).days // 365

print(f"Name     : {details['name']}")
print(f"Company  : {details['company']}")
print(f"Location : {details['location']}")
print(f"Years    : {years}")
