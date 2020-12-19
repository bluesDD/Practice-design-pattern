import json
import csv
from dataclasses import dataclass


def get_a_list_of_teammate():
  return json.dumps({
    "results": [
      {
        "username": "teammate1",
        "email": "teammate1@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "user_type": "owner",
        "is_admin": "true",
        "phone": "123-345-3453",
        "website": "www.example.com",
        "company": "ACME Inc.",
        "address": "123 Acme St",
        "address2": "",
        "city": "City",
        "state": "CA",
        "country": "USA",
        "zip": "12345"
      },
      {
        "username": "teammate2",
        "email": "teammate2@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "user_type": "teammate",
        "is_admin": "false",
        "phone": "123-345-3453",
        "website": "www.example.com",
        "company": "ACME Inc.",
        "address": "123 Acme St",
        "address2": "",
        "city": "City",
        "state": "CA",
        "country": "USA",
        "zip": "12345"
      },
      {
        "username": "teammate3",
        "email": "example@example.com",
        "first_name": "Steve",
        "last_name": "Doe",
        "user_type": "admin",
        "is_admin": "true",
        "phone": "123-345-3453",
        "website": "www.example.com",
        "company": "ACME Inc.",
        "address": "123 Acme St",
        "address2": "",
        "city": "City",
        "state": "CA",
        "country": "USA",
        "zip": "12345"
      }
    ]
  })
  
@dataclass
class Teammate(object):
  username: str
  email: str
  first_name: str
  last_name: str
  is_admin: bool

  class teammate:
  """
  deal with teammate
  """

  res_data = ""

  def __init__(self, json_res_data):
      self.res_data = json.loads(json_res_data)["results"]

  def get_basic_user_info(self):
      items = []
      for item in self.res_data:
        self.username = item["username"]
        self.email = item["email"]
        self.first_name = item["first_name"]
        self.last_name = item["last_name"]
        basic_info = [self.username, self.email, self.first_name, self.last_name]
        items.append(basic_info)
      return items

if __name__ == "__main__":
  tm = teammate(get_a_list_of_teammate())

  with open('data.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(tm.get_basic_user_info())
    # print(json.loads(get_a_list_of_teammate())["results"])
