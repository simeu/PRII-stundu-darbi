import requests
import json

url = "https://timeapi.io/api/TimeZone/AvailableTimeZones"
response = requests.get(url)
print(response)