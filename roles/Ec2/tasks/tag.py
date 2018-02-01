import boto.ec2
import sys
conn=boto.ec2.connect_to_region(sys.argv[1], aws_access_key_id=sys.argv[3], aws_secret_access_key=sys.argv[4])
reservations = conn.get_all_instances()

def instance_check(instance_name):
  for res in reservations:
    for inst in res.instances:
        if 'Name' in inst.tags:
            instance_name_list=inst.tags['Name']
            if instance_name_list == instance_name:
              instance_status="exist"
              print instance_status
instance_check(sys.argv[2])
