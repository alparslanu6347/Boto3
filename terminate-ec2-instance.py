import boto3


ec2 = boto3.resource('ec2')

# create a new EC2 instance
# instance = ec2.create_instances(
#      ImageId='ami-0aa7d40eeae50c9a9',
#      MinCount=1,
#      MaxCount=1,
#      InstanceType='t2.micro',
#      KeyName='second-key'
#  )

#ec2.instance('your InstanceID').stop()
#ec2.instance('your InstanceID').terminate()
#ec2.instance('i-00f169ed328db0db9').terminate()
ec2.instances.filter(InstanceIds= ["i-018bcf86a14531799", "i-0b9517d3f099d3840"]).terminate()
#ec2.instances.filter(InstanceIds= ["i-00f169ed328db0db9","i-00f169ed328db0db9"]).terminate()


#print(instance)