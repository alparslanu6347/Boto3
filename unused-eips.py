import boto3
import os

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

SOURCE_EMAIL = os.environ['aydintokuslu78@gmail.com']
DEST_EMAIL = os.environ['aydintokuslu78@gmail.com']

def lambda_handler(event,context):
    response = ec2_client.describe_addresses()
    unused_eips = []
    for address in response['Addresses']:
        if 'InstanceId' not in address  :
            unused_eips.append(address['PublicIp'])
    print(unused_eips)

    # send email using ses
    response = ses_client.send_email(
           Source = SOURCE_EMAIL,
           Destination={
            'ToAddresses': [
                DEST_EMAIL
            ]
          },
          Message={
            'Subject': {
                'Data': 'Unused  EIPS',
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': str(eips),
                    'Charset': 'utf-8'
                }
            }
          }
        )
        
