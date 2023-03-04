import boto3

client = boto3.client("s3")

response = client.select_object_content(
    Bucket='osvaldo-vpc-44',
    Key='string',
    SSECustomerAlgorithm='string',
    SSECustomerKey='string',
    Expression='string',
    ExpressionType='SQL',
)