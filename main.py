import requests
import json 

hypixel_base_url = "https://api.hypixel.net/skyblock/bazaar"
response = requests.get(hypixel_base_url)
items_obj = json.dumps(response.json(), indent=4)
with open("bazaar.json", "w") as outfile:
    outfile.write(items_obj)