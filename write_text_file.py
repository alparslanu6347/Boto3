import boto3
import os

# bucketları listeleyerek dosyaya yazdırmak

s3 = boto3.resource("s3")
# my_bucket = s3.Bucket("deneme1-boto3-bucket")

text_file_location=r"C:\Users\aydin\Desktop\boto3\boto3_list.txt"

with open(text_file_location,"a") as text_file:
    for bucket in s3.buckets.all():
        my_bucket = s3.Bucket(bucket.name)

        for file in my_bucket.objects.all():
            if file.key.endswith(".yml"):
                #print(file.key)
                #print(my_bucket.name)
                text_file.write(file.key + "\n")