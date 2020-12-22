from sendgrid import SendGridAPIClient
import os
import requests
import json

def set_api_key_env():
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
  os.environ['SENDGRID_TEAMMATES_API_KEY'] = json.loads(res.body)["api_key"]
  return print('API Key set in env.')

def get_teammates():
  api_key = os.environ.get('SENDGRID_TEAMMATES_API_KEY')
  sg = SendGridAPIClient(api_key)
  res = sg.client.teammates.get()
  return json.loads(res.body)

def touch_json():
  with open("teammates.json", "w") as target:
    pass
if __name__ == "__main__":
  print(get_teammates())
