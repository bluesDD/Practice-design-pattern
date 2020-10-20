import boto3
import json
import pprint

pricing = boto3.client("pricing", region_name="us-east-1")

res = pricing.describe_services()
for service in res["Services"]:
  print(service["ServiceCode"])

