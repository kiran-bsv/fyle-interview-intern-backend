from flask import jsonify
import requests

headers= {
    'X-Principal': '{"user_id":5, "principal_id":1}'
}
payload = {
    "id": 1,
    "grade": "A"
}

url= "http://0.0.0.0:7755/principal/assignments/grade"

try:
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")
except requests.RequestException as e:
    print(f"Request error: {e}")
