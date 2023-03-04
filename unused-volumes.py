import boto3

ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')
volumes = ec2_client.describe_volumes()
sns_arn = 'arn:aws:sns:us-east-1:731967392843:udemy-lambda-alerts'
unused_vols = []
size=0 #ebatını da eklemek istersek
for volume in volumes['Volumes']:
    #print(volume)
    if len(volume['Attachments']) == 0:
        unused_vols.append(volume['VolumeId'])
        print(volume)
        print("----"*5)
        size+=volume["Size"]

email_body = "##### Unused Volumes ##### \n"

for vol in unused_vols:
    email_body = email_body + "VolumeId = {} \n".format(vol)

# Send Email

email_body = email_body + "\n\nTotal Unused Volume Size = {}".format(size)

sns_client.publish(
    TopicArn = sns_arn,
    Subject = 'Unused Volumes',
    Message = email_body
)
print(email_body)
