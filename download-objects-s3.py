import boto3
import os

# bucket içindeki objeleri bilgisayarımıza indirme

s3 = boto3.resource("s3")

#my_bucket=s3.Bucket("osvaldo-vpc-44")

working_directory = r"C:\Users\aydin\Desktop\boto3\download"

for bucket in s3.buckets.all():
    my_bucket = s3.Bucket(bucket.name)

    for file in my_bucket.objects.all():
        #if file.key.endswith(".yml"):
        local_file_name=os.path.join(working_directory, file.key.split("/")[0])
        #listeye çevirdik ve 0ncı indexteydi bilgiler
        
        print(f"Downloading {file.key} to {local_file_name}")
        my_bucket.download_file(file.key, local_file_name)
        print(f"Finished downloading {local_file_name}")
            