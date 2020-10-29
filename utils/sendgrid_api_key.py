from sendgrid import SendGridAPIClient
import os


sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
