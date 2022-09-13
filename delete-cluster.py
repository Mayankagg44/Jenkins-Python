import boto3
import sys

status = sys.argv[1]
list_db= sys.argv[2]
client = boto3.client('rds')

#Deleting RDS cluster
def status_clusters_rds():
    for db in list_db.split(","):
        response = client.describe_global_clusters(
            GlobalClusterIdentifier=db
        )
        for i in response['GlobalClusters']:
            if status.lower() =='delete':
                if i['Status'] == 'available':
                    response = client.remove_from_global_cluster(
                        GlobalClusterIdentifier=i['GlobalClusterIdentifier'],
                        DbClusterIdentifier='arn:aws:rds:ap-northeast-2:760451896171:cluster:db-global-cluster-1'
                    )                   
                    print('Removing DB cluster {0}'.format(i['GlobalClusterIdentifier']))
                elif i['Status'] == 'starting' or i['Status'] == 'stopping':
                    print("It is in starting or stopping mode")
                    sys.exit(1)
                else :
                    print('Wrong status')
                    sys.exit(1)
            # if status.lower() =='stop':
            #     if i['Status'] == 'stopped' or i['Status'] == 'stopping':
            #         print("Already stopped")
            #         sys.exit(1)
            #     elif i['Status'] == 'starting':
            #         print('The DB cluster {0} is in starting mode...Kindly wait for few mins'.format(i['DBClusterIdentifier']))
            #         sys.exit(1)
            #     else:
            #         client.delete_db_cluster(DBClusterIdentifier = i['DBClusterIdentifier'])
            #         print('Deleting DB cluster {0}'.format(i['DBClusterIdentifier']))
if __name__ == '__main__':
   status_clusters_rds()
