import boto3
import datetime



s3client = boto3.client('s3')
list_buckets_resp = s3client.list_buckets()

for bucket in list_buckets_resp["Buckets"]:
  print(bucket["Name"])


ec2client = boto3.client('ec2')


print(datetime.datetime.now())
# list_ebs_backups = ec2client.describe_snapshots()
# for ebs in list_ebs_backups["Snapshots"]:

#   print(ebs["StateMessage"])

