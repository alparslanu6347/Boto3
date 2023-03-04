import boto3

client = boto3.client("ec2")

#client.start_instances(InstanceIds=['i-0118d05208d143c4c'])
#client.stop_instances(InstanceIds=['i-0118d05208d143c4c'])
#client.terminate_instances(InstanceIds=['i-0bed83164f56d3eb9'])
resp = client.terminate_instances(InstanceIds=['i-0bed83164f56d3eb9'])

for instance in resp["TerminatingInstances"]:
    #print("The instance with id {} Teminated".format(instance["InstanceId"]))
    #print("The instance with id {} Teminated".format(instance["CurrentState"]))
    print("The instance with id {} Teminated".format(instance["PreviousState"]))