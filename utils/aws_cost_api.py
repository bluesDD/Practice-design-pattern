import boto3
import json
import pprint

pricing = boto3.client("pricing", region_name="us-east-1")

res = pricing.describe_services()
# for service in res["Services"]:
#   print(service["ServiceCode"])

res = pricing.get_products(
  ServiceCode="AmazonEC2",
  Filters=[
    {
      'Type': 'TERM_MATCH',
      'Field': 'operatingSystem',
      'Value': 'Linux'
    }
  ])

price_items = json.loads(res["PriceList"][0])
terms = price_items["terms"]
print(price_items)
print(terms)
