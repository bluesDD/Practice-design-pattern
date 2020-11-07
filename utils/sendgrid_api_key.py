from sendgrid import SendGridAPIClient
import os
import requests
import json

base_url = "https://api.sendgrid.com/v3"
sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

data = {
  "name": "Test key",
  "sample": "data",
  "scopes": [
    "teammates.read"
  ]
}

res = sg.client.api_keys.post(request_body=data)
print(res.status_code)
#200
print(json.loads(res.body)["api_key"])
api_key = json.loads(res.body)["api_key"]
headers = {'Authorization': 'Bearer ' + api_key}

res_teammates = requests.get(base_url + "/teammates", headers=headers)
print(json.loads(res_teammates.text)["result"])
# b'{"is_reseller_customer":true,"reputation":100,"type":"free"}'
