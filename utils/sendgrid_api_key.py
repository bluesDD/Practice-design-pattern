from sendgrid import SendGridAPIClient
import os


sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
res = sg.client.user.account.get()
print(res.status_code)
#200
print(res.body)
#b'{"is_reseller_customer":true,"reputation":100,"type":"free"}'
