import boto3

client = boto3.client("ec2")
# resp = client.describe_instances(Filters=[{
#     'Name': 'instance-state-name',
#     'Values': ['terminated']
# }])
# # filter ile terminated olan ec2 listesini istedik.
# for reservation in resp["Reservations"]:
#     for instance in reservation["Instances"]:
#         print("InstanceId is {}".format(instance["InstanceId"]))  # InstanceId is i-0bed83164f56d3eb9
        
resp = client.describe_instances(Filters=[{
    'Name': 'tag:Env',
    'Values': ['Prod']
}])
# tag-key (Env-Prod) ile filtreleme yaparak ec2 listesini istedik.
for reservation in resp["Reservations"]:
    for instance in reservation["Instances"]:
        print("InstanceId is {}".format(instance["InstanceId"]))  # InstanceId is i-0bed83164f56d3eb9
        