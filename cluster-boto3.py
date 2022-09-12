import boto3
import sys

status = sys.argv[1]
list_db= sys.argv[2]
client = boto3.client('rds')

def status_clusters_rds():
    for db in list_db.split(","):
        response = client.describe_db_clusters(
            DBClusterIdentifier=db
        )
        for i in response['DBClusters']:
            if status.lower() =='start':
                if i['Status'] == 'available' or i['Status'] == 'starting':
                    print("Already started")
                    sys.exit(1)
                elif i['Status'] == 'stopping':
                    print('The DB cluster {0} is in stopping mode...Kindly wait for few mins'.format(i['DBClusterIdentifier']))
                    sys.exit(1)
                else:
                    client.start_db_cluster(DBClusterIdentifier = i['DBClusterIdentifier'])
                    print('starting DB cluster {0}'.format(i['DBClusterIdentifier']))          
            if status.lower() =='stop':
                if i['Status'] == 'stopped' or i['Status'] == 'stopping':
                    print("Already stopped")
                    sys.exit(1)
                elif i['Status'] == 'starting':
                    print('The DB cluster {0} is in starting mode...Kindly wait for few mins'.format(i['DBClusterIdentifier']))
                    sys.exit(1)
                else:
                    client.stop_db_cluster(DBClusterIdentifier = i['DBClusterIdentifier'])
                    print('stopping DB cluster {0}'.format(i['DBClusterIdentifier']))
if __name__ == '__main__':
    status_clusters_rds()
