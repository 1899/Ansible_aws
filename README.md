# Ansible

Roles:
1. VPC - Virtual Private Cloud
2. EC2 - Elastic Cloud Compute
3. RDS - Relational Database Service
4. ECS - Elastic container service
5. S3  - Simple storage service
6. R53 - Route 53
7. IAM - Identity Access management
8. ELB - Elastic Load Balancer

VPC Execution:

Setting up Virtual Private Cloud
Step 1: Update AWS access key and secret key in "key.yml" along with other parameters required for customization.
Step 2: Below command provisions VPC in specific region.
$ ansible-playbook install.yml

Ec2 Execution:
Step 1:
$ ansible-playbook -i inventory ec2.yml

RDS Execution
Step 1:
$ ansible-playbook -i inventory rds.yml
