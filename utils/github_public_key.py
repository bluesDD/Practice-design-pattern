import requests
import json


BASE_URL = "https://github.com/"
username = "bluesDD"
r = requests.get(BASE_URL + username + ".keys")
print(r.text)
# public key
