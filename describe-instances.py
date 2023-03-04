import boto3

client = boto3.client("ec2")
resp = client.describe_instances()

for reservation in resp["Reservations"]:
    for instance in reservation["Instances"]:
        #print("InstanceId is {}".format(instance["InstanceId"]))  # InstanceId is i-0bed83164f56d3eb9
        #print("InstanceId is {}".format(instance["ImageId"]))  # InstanceId is ami-0aa7d40eeae50c9a9
        print("InstanceId is {}".format(instance["LaunchTime"]))  # InstanceId is 2023-02-18 18:07:55+00:00