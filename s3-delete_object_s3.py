import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='javahomecloud123',
    Key='s3-create_bucket.py'
)