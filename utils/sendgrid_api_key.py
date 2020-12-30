from sendgrid import SendGridAPIClient
import os
import requests
import json
import typing as tp
from dataclasses import dataclass

base_url = "https://api.sendgrid.com/v3"
sg = SendGridAPIClient()

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

class Client:
    def __init__(
          self,
          base_url="https://api.sendgrid.com/v3",
          api_key=None):

        self.__base_url = base_url
        self.__api_key = api_key


@dataclass
class APIKeyTeammatesReadOnly:  
    api_key = {
      "name": "teammates read only",
      "scopes": [
        "teammates.read"
      ]
    }

    res = ""

    def __post_init__(self):
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        self.res = sg.client.api_keys.post(request_body=data)

        return self.res

    def __set_api_key_env(self):
        os.environ['SENDGRID_TEAMMATES_API_KEY'] = json.loads(self.res.body)["api_key"]
        return print('API Key set in env.')
