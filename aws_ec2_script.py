# @Author: mdrhri-6
# @Date:   2016-11-21T13:55:38+01:00
# @Last modified by:   mdrhri-6
# @Last modified time: 2016-11-24T18:52:21+01:00

import boto3
import datetime

ec2 = boto3.resource('ec2', region_name='us-east-2')
ec2c = boto3.client('ec2', region_name='us-east-2')


'''
    Listing region names and their endpoints.
'''
availZones = []
availRegionNames = []
for zone in ec2c.describe_availability_zones()['AvailabilityZones']:
    if zone['State'] == 'available':
        availZones.append(zone['ZoneName'])
        availRegionNames.append(zone['RegionName'])


'''
    Run an instance from the list of regions from the previous step.
'''

# Step 1: Create a keypair
myKeyName = ""
outfile = open(myKeyName, 'w')
key_pair = ec2.create_key_pair(KeyName=myKeyName)
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)


# Step 2: Setup instance parameters
kw_args = {
    'ImageId': '',
    'MinCount': 1,
    'MaxCount': 1,
    'KeyName': '',
    'InstanceType': 't2.micro',
    'SecurityGroupIds': ['',]
}
instances = ec2.run_instances(**kw_args)

# instance_id = []
# instance_type = []
#
# for instance in instances:
#     instance_id.append(instance.id)
#     instance_type.append(instance.instance_type)
#     print instance.id, instance.instance_type

'''
    Check if a keyPair exists.
'''
key_pair_info_iterator = ec2.key_pairs.all()
for each in key_pair_info_iterator:
    print each.key_name


'''
    Retrieve the status of your running instances
'''

instance_ids = []
for each in ec2.instances.all():
    resp = ec2c.describe_instance_status(InstanceIds=[str(each._id)])
    if bool(resp['InstanceStatuses']):
        for each in resp['InstanceStatuses']:
            if each['InstanceState']['Name'] == 'running':
                instance_ids.append(each['InstanceId'])

print instance_ids

'''
    Stop all/one the running instances.
'''

for each in instance_ids:
    resp = ec2c.stop_instances(InstanceIds=[each])
    if bool(resp['StoppingInstances']):
        for each in resp['StoppingInstances']:
            print "Stopped instance: {}".format(each['InstanceId'])
            print "Current state is: {}".format(each['CurrentState']['Name'])


'''
    Monitor status of EC2 Clients
'''

# Cloudwatch objects creation
cloudwatch = boto3.resource('cloudwatch', region_name='us-east-2')
cwclient = boto3.client('cloudwatch', region_name='us-east-2')

# Get all the matrices
kw_args = {'Namespace': 'AWS/EC2', 'MetricName': 'NetworkOut'}

metric_iterator = cloudwatch.metrics.filter(**kw_args)

for each in metric_iterator:
    print "Metric namespace: {}, Metric Name: {}".format(each.namespace, each. name)

# Get statistics from metrics.
kw_args = {
    'Namespace': 'AWS/EC2',
    'MetricName': 'NetworkOut',
    'StartTime': datetime.datetime.strptime("2016-11-21 00:00:00", "%Y-%m-%d %H:%M:%S"),
    'EndTime': datetime.datetime.strptime("2016-11-21 02:00:00", "%Y-%m-%d %H:%M:%S"),
    'Period': 300,
    'Statistics': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'],
    'Unit': 'Bytes',
    'Dimensions': [
        {'Name': 'InstanceId', 'Value': 'i-0bd38be22ce886804'}
    ]
}

response = cwclient.get_metric_statistics(**kw_args)

print "Statistics for each datapoints:"
count = 0
for each in response['Datapoints']:
    print "\n"
    print "Average value for datapoints {}: {}".format(count, each['Average'])
    print "Sum of all datapoints: {}".format(each['Average'])
    print "Minumum value for this datapoints: {}".format(each['Minimum'])
    print "Maximum value for this datapoints: {}".format(each['Maximum'])
    count += 1

print "Number of datapoints: {}".format(count)
