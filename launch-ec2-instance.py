import boto3
import os

ec2 = boto3.resource('ec2')

# create a new EC2 instance
instance = ec2.create_instances(
     ImageId='ami-0aa7d40eeae50c9a9',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='second-key'
 )

print(instance)