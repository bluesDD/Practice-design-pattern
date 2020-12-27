from sendgrid import SendGridAPIClient
from dataclasses import dataclass
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
  with open("teammates.json", "w") as f:
    res = get_teammates()
    f.write(json.dumps(res["result"], indent=4))
if __name__ == "__main__":
  touch_json()

@dataclass(frozen=True)
class Teammate(object):
  username: str
  email: str
  first_name: str
  last_name: str
  user_type: str
  is_admin: bool
  phone: str
  website: str
  company: str
  address: str
  address2: str
  city: str
  state: str
  country: str
  zip: str


class Teammates:
  def get_teammates(self, event):
    teammate = Teammate()

    teammate["username"] = event.get("username")
    teammate["email"] = event.get("email")
    teammate["first_name"] = event.get("first_name")
    teammate["last_name"] = event.get("last_name")
    teammate["is_admin"] = event.get("is_admin")
    teammate["phone"] = event.get("phone")
    teammate["website"] = event.get("website")
    teammate["company"] = event.get("company")
    teammate["address"] = event.get("address")
    teammate["city"] = event.get("city")
    teammate["state"] = event.get("state")
    teammate["country"] = event.get("country")
    teammate["zip"] = event.get("zip")

    return teammate


