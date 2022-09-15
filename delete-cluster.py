import boto3
import sys
import time

status = sys.argv[1]
list_db = sys.argv[2] # Global DB Cluster
db_clu = sys.argv[3]    # DB Cluster (after being removed)
list_inst = sys.argv[4] # Instance name inside the cluster
client = boto3.client('rds')
n = 3
p = 3

def remove_global_clusters():
    global n
    global p
    
#     response = client.describe_global_clusters(GlobalClusterIdentifier=list_db)
#     print(response)
#     for i in response['GlobalClusters']:
#         if status.lower() =='delete':
#             if i['Status'] == 'available':
#                 response = client.remove_from_global_cluster(
#                     GlobalClusterIdentifier=i['GlobalClusterIdentifier'],
#                     DbClusterIdentifier='arn:aws:rds:ap-northeast-2:760451896171:cluster:db-global-cluster-1'
#                 )                   
#                 print('Removing Global cluster {0}'.format(i['GlobalClusterIdentifier']))
#             elif i['Status'] == 'starting' or i['Status'] == 'stopping':
#                 print("It is in starting or stopping mode")
#                 sys.exit(1)
#             else :
#                 print('Wrong status')
#                 sys.exit(1)
# # Deleting RDS Instance inside the cluster
#     while n > 0:
#         response = client.describe_db_instances(DBInstanceIdentifier=list_inst)
#         print(response)
#         for j in response['DBInstances']:
#             if j['DBInstanceStatus'] == 'available':
#                 client.delete_db_instance(
#                     DBInstanceIdentifier = j['DBInstanceIdentifier'],
#                     SkipFinalSnapshot=True
#                 )
#                 print('Deleting DB instance {0}'.format(j['DBInstanceIdentifier']))
#         n = 0

# # Deleting RDS DB cluster(after it has been removed from global database)
#     while p > 0:
#         response = client.describe_db_clusters(DBClusterIdentifier=db_clu)
#         print(response)
#         time.sleep(100)
#         for k in response['DBClusters']:
#             if k['Status'] == 'available':
#                 client.delete_db_cluster(DBClusterIdentifier = k['DBClusterIdentifier'],SkipFinalSnapshot = True)
#                 print('Deleting Global_DB Cluster {0}'.format(k['DBClusterIdentifier']))
   
# Recreate the RDS DB cluster(after it has been removed from the global database)
        # time.sleep(120)
    print("!!!!!!!!Creating the Cluster Now!!!!!!")
        # response = client.describe_db_clusters(DBClusterIdentifier=db_clu)
        #     print(response)
        # for j in response['DBClusters']:
        #     if j['Status'] != 'available':
    client.create_db_cluster(
       # DatabaseName='database-4',
            #CharacterSetName = 'string',
        DBClusterIdentifier=db_clu,
        DBClusterParameterGroupName='default.aurora-mysql5.7',
      #  VpcSecurityGroupIds=['default'],
        DBSubnetGroupName='db-subnet',
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.10.2',
        Port=3306,
#         MasterUsername='admin',
#         MasterUserPassword='password',
       # OptionGroupName='default:aurora-mysql-5-7',
       # ReplicationSourceIdentifier='arn:aws:rds:us-east-1:760451896171:cluster:database-3',
        StorageEncrypted=True,
        KmsKeyId='dfc76317-d847-4a42-b8c7-1c17ffadde02',
        EnableCloudwatchLogsExports=['general'],
        EngineMode='provisioned',
        EnableIAMDatabaseAuthentication=False,
        DeletionProtection=False,
        GlobalClusterIdentifier=list_db,
            #Domain='string',
            #DomainIAMRoleName='string',
            #EnableGlobalWriteForwarding=True|False,
       # DBClusterInstanceClass='db.r5.large',
       # AllocatedStorage=100,
       # StorageType='io1',
       # Iops=2000,
       # PubliclyAccessible=True,
       # AutoMinorVersionUpgrade=True,
       # MonitoringInterval=0,
       # EnablePerformanceInsights=False,
        NetworkType='IPV4',
        SourceRegion='us-east-1'
    )
    print("Congratulations, Cluster has been created!!!")
    p = 0


if __name__ == '__main__':
   remove_global_clusters()
