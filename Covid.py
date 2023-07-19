import requests

url = "https://api.covidtracking.com/v1/us/daily.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for entry in data:
        date = entry["date"]
        positive = entry["positive"]
        deaths = entry["death"]
        recovered = entry["recovered"]
        print(f"Date: {date}, Positive cases: {positive}, Deaths: {deaths}, Recovered: {recovered}")
else:
    print(f"Error: {response.status_code}")
