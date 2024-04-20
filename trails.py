from flask import jsonify
import requests


headers= {
    'X-Principal': '{"user_id":5, "principal_id":1}'
}
url= "http://0.0.0.0:7755/principal/teachers"

response = requests.get(url, headers = headers)

if response.status_code==200:
    print(response.json())
else:
    print(response.text)
