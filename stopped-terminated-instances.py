import boto3


ec2 = boto3.resource('ec2')

#stop edilmiş veya terminate edilmiş instance'ların listesini gösterir.

#instances=ec2.instances.filter(Filters= [{"Name":"instance-state-name", "Values":["stopped","terminated"]}])
instances=ec2.instances.all()
#ikisi de aynı sonucu verir.
for instance in instances:
    print(instance.id, instance.instance_type)


# i-0b9517d3f099d3840 t2.micro
# i-00f169ed328db0db9 t2.micro
# i-018bcf86a14531799 t2.micro