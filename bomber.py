import requests
import json


# Define the new value you want to fill
number = input("Please Enter Phone Number: ")
new_value = number

# Keys to update in Payload are given here
keys_to_update = [
    "phone",
    "mobile_num",
    "mobileNumber",
    "mobile",
    "mobileNo",
    "Mobile_Email",
    "number",
]

# Opening JSON file
f = open("info.json")

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for obj in data:
    url = obj["url"]
    headers = obj["headers"]
    payload = obj["body"]
    for key in keys_to_update:
        if key in payload:
            obj["body"][key] = new_value
    response = requests.post(url, headers=headers, json=payload)
    print(response)
    # print("Status Code:", response.status_code)

# Closing file
f.close()
