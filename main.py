import requests
from requests.auth import HTTPBasicAuth

url = "https://api.intel471.com/v1/breachAlerts?confidence=medium&gir=1.1.1&gir=1.2.2&from=7day&count=100"
KEY = ""
email = ""

response = requests.get(url, auth=HTTPBasicAuth(email, KEY), verify=False)
    
if response.status_code == 200:
    data = response.json()
else:
    response.raise_for_status()
    
print(data["breach_alerts"])

for item in data["breach_alerts"]:
    print(item["data"]["breach_alert"]["victim"]["name"], ",", item["data"]["breach_alert"]["victim"]["urls"][0], ",", item["data"]["breach_alert"]["actor_or_group"])
