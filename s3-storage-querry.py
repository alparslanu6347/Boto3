import boto3


# bucket içindeki objelerin storage'larını listeleme

s3_resource = boto3.resource("s3")
bucket=s3_resource.Bucket("deneme1-boto3-bucket")

for bucket_obj in bucket.objects.all():
    object_name=bucket_obj.key
    storage_class=bucket_obj.storage_class

    print(f"This is the Key : {object_name} and this is the storage class : {storage_class}")
