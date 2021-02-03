import boto3


#create volume
def create_volume(ec2_client, availability_zone, DryRunFlag=False):
    try:
        response= ec2_client.create_volume(
            AvailabilityZone=availability_zone,
            Encrypted=False,
            #Iops=100,
            #KmsKeyId='string',
            Size=10,
            #SnapshotId='string',
            VolumeType='gp2',    #standard'|'io1'|'gp2'|'sc1'|'st1',
            DryRun=DryRunFlag
            )
        #pprint(response)

        if response['ResponseMetadata']['HTTPStatusCode']== 200:
            volume_id= response['VolumeId']
            print('***volume:', volume_id)

            ec2_client.get_waiter('volume_available').wait(
                VolumeIds=[volume_id],
                DryRun=DryRunFlag
                )
            print('***Success!! volume:', volume_id, 'created...')

    except Exception as e:
            print('***Failed to create the volume...')
            print(type(e), ':', e)


def attach_volume(volume_id, instance_id, DryRunFlag=False):

     try:
        print('***attaching volume:', volume_id, 'to:', instance_id)
        response= ec2_client.attach_volume(
            Device=device,
            InstanceId=instance_id,
            VolumeId=volume_id,
            DryRun=DryRunFlag
            )
        #pprint(response)

        if response['ResponseMetadata']['HTTPStatusCode']== 200:
            ec2_client.get_waiter('volume_in_use').wait(
                VolumeIds=[volume_id],
                DryRun=False
                )
            print('***Success!! volume:', volume_id, 'is attached to instance:', 
  instance_id)

    except Exception as e:
        print('***Error - Failed to attach volume:', volume_id, 'to the instance:', instance_id)
        print(type(e), ':', e)
