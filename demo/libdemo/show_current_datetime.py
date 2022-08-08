import requests

resp = requests.get("http://worldtimeapi.org/api/timezone/Asia/Tokyo")
#print(resp.status_code)
details = resp.json()    # convert json to dict
print(details['datetime'])
