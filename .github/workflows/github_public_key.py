import requests
import json
import yaml
import os

yaml_file = os.environ.get("TARGET_FILE", "test.yml")
webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "https://hooks.slack.com/zzz")

def get_public_keys_from_github(users):
  keys = []
  for user in users:
    if is_state_absent(user):
        continue
    res = requests.get(user["authorized_keys"][0]["key"])
    keys.append({
      "user": user["name"],
      "public_key": res.text,
      "key_url": user["authorized_keys"][0]["key"]
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
  warning_message = key["user"] \
    + "さんのGitHub上の公開鍵が消えてしまっているようです。再登録作業を案内してあげてください。\n" \
    + "→当該URL： " + key["key_url"]
  
  try:
    # TODO: テスト用にかえてる
    # requests.post(webhook_url, data=json.dumps({
    #   "text" : warning_message,
    # }))
    return print("Warning have been sent to slack successfully!")
  except:
    raise


if __name__ == "__main__":
  obj = load_yaml(yaml_file)
  users = obj["users"]
  keys = get_public_keys_from_github(users)
  for key in keys:
    if public_key_exists(key) == False:
      send_message_to_slack(key)
