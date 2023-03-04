import boto3

# aradığımız bir bucketın içindeki objeleri listeleme

s3 = boto3.resource("s3")

my_bucket=s3.Bucket("osvaldo-vpc-44")

# for file in my_bucket.objects.all():
#     print(file.key)
#     print(my_bucket.name)

# folder içini görmek

# for file in my_bucket.objects.filter(Prefix="FOLDER ISMI (UZANTISI DAHIL)"):
#     print(file.key)
#     print(my_bucket.name)

# belli bir objcet'ten sonrasını görmek istiyorsak, ondan sonrasını gösterir:
#bu osvaldo-vpc-44 içinde aslan0.jpeg sonrasını gösterir
# for file in my_bucket.objects.filter(Marker="aslan0.jpeg"):
#     print(file.key)
#     print(my_bucket.name)

# #bu tüm bucket'ların içindeki object'lerden 2023021XDl-template1xhschbbt59 sonrasını gösterir
# for bucket in s3.buckets.all():
#     my_bucket = s3.Bucket(bucket.name)

#     for file in my_bucket.objects.filter(Marker="2023021XDl-template1xhschbbt59"):
#         print(file.key)
#         print(my_bucket.name)

#bu tüm bucket'ların içinde dosya uzantısı yml olanları gösterir
for bucket in s3.buckets.all():
    my_bucket = s3.Bucket(bucket.name)

    for file in my_bucket.objects.all():
        if file.key.endswith(".yml"):
            print(file.key)
            #print(my_bucket.name)