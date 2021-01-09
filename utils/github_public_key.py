import requests
import json
import yaml


BASE_URL = "https://github.com/bluesDD.keys"
usernames = ["bluesDD", "bluesDD"]
YAML_FILE = "test.yml"

def get_public_keys_from_github(users):
  keys = []
  for user in users:
    print(user)
    # if user["state"]:
    #   if user["state"] == "absent":
    #     continue
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
  top_var = "users"
  obj = load_yaml(YAML_FILE)
  print(obj)
  a = get_public_keys_from_github(obj)
  print(a)
  
