import time

import boto3

import funcs

aws_region = "eu-west-2"
availability_zone = "eu-west-2a"
volume_size = 10

ec2 = boto3.client("ec2", region_name=aws_region)

# Create new volume

funcs.create_volume(ec2, availability_zone)
