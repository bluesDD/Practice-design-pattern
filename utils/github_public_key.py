import requests
import json


BASE_URL = "https://github.com/bluesDD.keys"
usernames = ["bluesDD", "bluesDD"]

def get_public_keys_from_github(usernames):
  keys = []
  for username in usernames:
    r = requests.get(BASE_URL)
    keys.append({
      "user": username,
      "key": r.text
    })
  return keys


if __name__ == "__main__":
  ke = get_public_keys_from_github(usernames)
  print(ke)
