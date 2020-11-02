from sendgrid import SendGridAPIClient
import os
import requests

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

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
print(res.body)
# b'{"is_reseller_customer":true,"reputation":100,"type":"free"}'
