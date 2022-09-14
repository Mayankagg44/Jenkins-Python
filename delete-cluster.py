import boto3
import sys

status = sys.argv[1]
#list_db = sys.argv[2] # Global DB name
#list_inst = sys.argv[3] # Instance name inside the cluster
db_clu = sys.argv[2]
client = boto3.client('rds')
n = 3
p = 3

def remove_global_clusters():
    global n
    global p
    
    # response = client.describe_global_clusters(GlobalClusterIdentifier=list_db)
    # print(response)
    # for i in response['GlobalClusters']:
    #     if status.lower() =='delete':
    #         if i['Status'] == 'available':
    #             response = client.remove_from_global_cluster(
    #                 GlobalClusterIdentifier=i['GlobalClusterIdentifier'],
    #                 DbClusterIdentifier='arn:aws:rds:ap-northeast-2:760451896171:cluster:db-global-cluster-1'
    #             )                   
    #             print('Removing Global cluster {0}'.format(i['GlobalClusterIdentifier']))
    #         elif i['Status'] == 'starting' or i['Status'] == 'stopping':
    #             print("It is in starting or stopping mode")
    #             sys.exit(1)
    #         else :
    #             print('Wrong status')
    #             sys.exit(1)
    # while n > 0:
    #     response = client.describe_db_instances(DBInstanceIdentifier=list_inst)
    #     print(response)
    #     for j in response['DBInstances']:
    #         if j['DBInstanceStatus'] == 'available':
    #             client.delete_db_instance(
    #                 DBInstanceIdentifier = j['DBInstanceIdentifier'],
    #                 SkipFinalSnapshot=True
    #             )
    #             print('Deleting DB instance {0}'.format(j['DBInstanceIdentifier']))
        # n = 0

#Deleting RDS Global cluster(after it has been removed from global database)
    while p > 0:
        response = client.describe_db_clusters(DBClusterIdentifier=db_clu)
        print(response)
        for k in response['DBClusters']:
            if k['Status'] == 'available':
                client.delete_db_cluster(DBClusterIdentifier = k['DBClusterIdentifier'],SkipFinalSnapshot = True)
                print('Deleting Global_DB Cluster {0}'.format(k['DBClusterIdentifier']))
        p = 0
        # n = 0

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

#Deleting RDS Global Instance
# def delete_global_inst():
#     for db in list_inst.split(","):
#         response = client.describe_db_instances(
#             DBInstanceIdentifier=db
#         )     
#         print(response)
#         for i in response['DBInstances']:
#             if status.lower() =='delete':
#                 if i['DBInstanceStatus'] == 'available':
#                     client.delete_db_instance(
#                         DBInstanceIdentifier=i['DBInstanceIdentifier'],
#                         SkipFinalSnapshot=True
#                     )
#                     print('Deleting DB instance {0}'.format(i['DBInstanceIdentifier']))
#                 elif i['DBInstanceStatus'] == 'stopping' or i['DBInstanceStatus'] == 'starting':
#                     print('The DB instance {0} is in stopping or starting mode...Kindly wait for few mins'.format(i['DBInstanceIdentifier']))
#                     sys.exit(1)
#                 else:
#                     print('Wrong status')
#                     sys.exit(1)                


if __name__ == '__main__':
   remove_global_clusters()
