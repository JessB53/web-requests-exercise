# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")

import requests
import json
import statistics

# request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
# response = requests.get(request_url)
# parsed_response = json.loads(response.text)
# print(parsed_response["name"])

# request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
# response2 = requests.get(request_url)
# parsed_response2 = json.loads(response2.text)
# for p in parsed_response2:
#     print(p["name"], p["id"])


request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request_url)
parsed_response3 = json.loads(response3.text)

grades = []
students = parsed_response3["students"]
for x in students:
    grades.append(x["finalGrade"])

print("MAX:", max(grades))
print("MIN:", min(grades))
print("AVG:", statistics.mean(grades))