##AWS dynamic inventory script
import boto3
import json
import argparse

def get_ec2_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['PrivateIpAddress'])
    return instances

def generate_inventory(region):
    instances = get_ec2_instances(region)
    inventory = {
        'all': {
            'hosts': instances
        },
        '_meta': {
            'hostvars': {}
        }
    }
    return inventory

def main():
    parser = argparse.ArgumentParser(description='AWS Dynamic Inventory Script')
    parser.add_argument('--region', required=True, help='AWS region')
    args = parser.parse_args()

    inventory = generate_inventory(args.region)
    print(json.dumps(inventory))

if __name__ == '__main__':
    main()
import boto3
import json
import argparse
