import boto3
import os

# bucketa objects yüklemek

s3 = boto3.resource("s3")

#bu adresteki objeleri yüklicek
local_upload_directory=r"C:\Users\aydin\Desktop\my-projects\aws\Project-101-deneme\static-web"

# for bucket in s3.buckets.all():
my_bucket = s3.Bucket("deneme1-boto3-bucket")
#     print(my_bucket)

for image in os.listdir(local_upload_directory):
    full_upload_path=os.path.join(local_upload_directory, image) # yüklemek için tam yolu ayarlarız
    print(full_upload_path)
    #print(image) #istenilen yerdeki tüm objeleri listeler
    print(f"uploading {full_upload_path} to boto3_examples/{image}")
    my_bucket.upload_file(full_upload_path, f"boto3_examples/{image}")
    print(f"done uploading {full_upload_path} to boto3_examples/{image}\n")


