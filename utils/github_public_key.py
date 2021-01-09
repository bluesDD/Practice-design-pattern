import requests
import json
import yaml


BASE_URL = "https://github.com/bluesDD.keys"
usernames = ["bluesDD", "bluesDD"]
YAML_FILE = "test.yml"

def get_public_keys_from_github(users):
  keys = []
  for user in users:
    if is_state_absent(user):
        continue

    res = requests.get(user["authorized_keys"][0]["key"])
    keys.append({
      "user": user["name"],
      "public_key": res.text
    })
  return keys

def is_state_absent(user):
  if "state" in user:
    if user["state"] == "absent":
      return True
  else:
    return False

def load_yaml(file):
  with open(file) as f:
    return yaml.safe_load(f)

def public_key_exists(key):
  if key["public_key"] == "":
    return False
  else:
    return True


def send_message_to_slack(key):
  ## TODO: 実際にSlackにメッセージ送る実装に変える
  print(key["user"] + "さんのGitHub上の公開鍵が消えてしまっているようです。再登録作業を案内してあげてください。")

if __name__ == "__main__":
  obj = load_yaml(YAML_FILE)
  users = obj["users"]
  print(users)
  keys = get_public_keys_from_github(users)
  print(keys)
  for key in keys:
    if public_key_exists(key) == False:
      send_message_to_slack(key)
