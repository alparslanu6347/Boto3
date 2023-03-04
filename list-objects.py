import boto3

# bucketları ve içindeki tüm objeleri listeleme

s3 = boto3.resource("s3")


for bucket in s3.buckets.all():
    my_bucket = s3.Bucket(bucket.name)

    for file in my_bucket.objects.all():
        print(f"Bucket: {bucket.name} Key: {file.key}")

