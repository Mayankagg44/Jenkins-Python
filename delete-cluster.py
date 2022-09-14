import boto3
import sys

status = sys.argv[1]
list_db = sys.argv[1]
list_inst = sys.argv[2]
client = boto3.client('rds')
n = 3

#Removing RDS Global cluster
def remove_global_clusters():
    for db in list_db.split(","):
        response = client.describe_global_clusters(
            GlobalClusterIdentifier=db
        )
        print(response)
        for i in response['GlobalClusters']:
            if status.lower() =='delete':
                if i['Status'] == 'available':
                    response = client.remove_from_global_cluster(
                        GlobalClusterIdentifier=i['GlobalClusterIdentifier'],
                        DbClusterIdentifier='arn:aws:rds:ap-northeast-2:760451896171:cluster:db-global-cluster-1'
                    )                   
                    print('Removing Global cluster {0}'.format(i['GlobalClusterIdentifier']))
                elif i['Status'] == 'starting' or i['Status'] == 'stopping':
                    print("It is in starting or stopping mode")
                    sys.exit(1)
                else :
                    print('Wrong status')
                    sys.exit(1)
        while n > 0:
            for db in list_inst.split(","):
                response = client.describe_db_instances(
                    DBInstanceIdentifier=db
                )
            print(response)
                for j in response['DBInstances']:
                    if j['DBInstanceStatus'] == 'available':
                        client.delete_db_instance(
                            DBInstanceIdentifier=i['DBInstanceIdentifier'],
                            SkipFinalSnapshot=True
                        )
                        print('Deleting DB instance {0}'.format(j['DBInstanceIdentifier']))
            n = 0




#Deleting RDS Global cluster(after it has been removed from global database)
# def delete_global_cluster():
#     for db in list_inst.split(","):
#         response = client.describe_db_instances(
#             DBInstanceIdentifier=db
#         )     
#         print(response)
#         for i in response['DBInstances']:
#             if status.lower() =='delete':
#                 if i['DBClusterStatus'] == 'available':
                   
            #        for j in response['GlobalClusters']:
            #     if j['Status'] == 'available':
            #         client.delete_global_cluster(
            #         GlobalClusterIdentifier=i['GlobalClusterIdentifier']
            #         )
            #         print('Deleting Global Cluster {0}'.format(j['GlobalClusterIdentifier']))
            # n = 0
                    
#                 elif i['DBInstanceStatus'] == 'stopping' or i['DBInstanceStatus'] == 'starting':
#                     print('The DB instance {0} is in stopping or starting mode...Kindly wait for few mins'.format(i['DBInstanceIdentifier']))
#                     sys.exit(1)
#                 else:
#                     print('Wrong status')
#                     sys.exit(1)   
            


if __name__ == '__main__':
   remove_global_clusters()
#    delete_global_cluster()
#    delete_global_inst()
