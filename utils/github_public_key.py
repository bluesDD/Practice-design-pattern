import requests
import json
import yaml


BASE_URL = "https://github.com/bluesDD.keys"
usernames = ["bluesDD", "bluesDD"]
YAML_FILE = "test.yml"

def get_public_keys_from_github(users):
  keys = []
  for user in users:
    if "state" in user:
      if user["state"] == "absent":
        continue

    res = requests.get(user["authorized_keys"][0]["key"])
    keys.append({
      "user": user["name"],
      "key": res.text
    })
  return keys


def load_yaml(file):
  with open(file) as f:
    return yaml.safe_load(f)


if __name__ == "__main__":
  obj = load_yaml(YAML_FILE)
  users = obj["users"]
  print(users)
  a = get_public_keys_from_github(users)
  print(a)
  
