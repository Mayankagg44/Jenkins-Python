import boto3
import sys

status = sys.argv[1]
list_db= sys.argv[2]
client = boto3.client('rds')

#Describe RDS Instance
def status_rds():
    for db in list_db.split(","):
        response = client.describe_db_instances(
            DBInstanceIdentifier=db
        )
        for i in response['DBInstances']:
            if status.lower() =='start':
                if i['DBInstanceStatus'] == 'available' or i['DBInstanceStatus'] == 'starting':
                    print("Already started")
                    sys.exit(1)
                elif i['DBInstanceStatus'] == 'stopping':
                    print('The DB instance {0} is in stopping mode...Kindly wait for few mins'.format(i['DBInstanceIdentifier']))
                    sys.exit(1)
                else:
                    client.start_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
                    print('starting DB instance {0}'.format(i['DBInstanceIdentifier']))          
            if status.lower() =='stop':
                if i['DBInstanceStatus'] == 'stopped' or i['DBInstanceStatus'] == 'stopping':
                    print("Already stopped")
                    sys.exit(1)
                elif i['DBInstanceStatus'] == 'starting':
                    print('The DB instance {0} is in starting mode...Kindly wait for few mins'.format(i['DBInstanceIdentifier']))
                    sys.exit(1)
                else:
                    client.stop_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
                    print('stopping DB instance {0}'.format(i['DBInstanceIdentifier']))

if __name__ == '__main__':
    status_rds()
    
