import requests
import json


BASE_URL = "https://github.com/"
usernames = ["bluesDD", "bluesDD"]

def get_public_keys_from_github(usernames):
  for username in usernames:
    r = requests.get(BASE_URL + username + ".keys")
    print(r.text)
# public key


if __name__ == "__main__":
  get_public_keys_from_github(usernames)
