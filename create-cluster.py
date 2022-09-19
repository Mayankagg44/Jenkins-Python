import boto3
import sys

status = sys.argv[1]
list_db = sys.argv[2] # Global DB Cluster
db_clu = sys.argv[3]    # DB Cluster (after being removed)
list_inst = sys.argv[4] # Instance name inside the cluster
client = boto3.client('rds')


def recreate_global_cluster():

# Recreate the RDS DB cluster(after it has been removed from the global database)
    print("!!!!!!Creating the DB Cluster Now!!!!!!")
    client.create_db_cluster(
        DBClusterIdentifier=db_clu,
        DBClusterParameterGroupName='default.aurora-mysql5.7',
        DBSubnetGroupName='db-subnet',
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.10.2',
        Port=3306,
        StorageEncrypted=True,
        KmsKeyId='49c0c0b0-6e8a-4150-9d40-ed8f1385b1bd',
#        KmsKeyId='dfc76317-d847-4a42-b8c7-1c17ffadde02',
        EnableCloudwatchLogsExports=['general'],
        EngineMode='provisioned',
        EnableIAMDatabaseAuthentication=False,
        DeletionProtection=False,
        GlobalClusterIdentifier=list_db,
        NetworkType='IPV4',
        SourceRegion='us-east-1'
    )

    waiter = client.get_waiter('db_cluster_available')
    waiter.wait(
        DBClusterIdentifier=db_clu,
        WaiterConfig={
            'Delay': 4800,   #80 mins
            'MaxAttempts': 2
        }
    )
    print("DB Cluster {0} has been created!!!\n\n".format(db_clu))
  
    response = client.describe_db_clusters(DBClusterIdentifier=db_clu)
    print(response)
    print("*****Now creating the DB Cluster instance*****")
    client.create_db_instance(
        DBInstanceIdentifier=list_inst,
        DBInstanceClass='db.r5.large',
        Engine='aurora-mysql',
        DBSubnetGroupName='db-subnet',
        DBParameterGroupName='default.aurora-mysql5.7',
        EngineVersion='5.7.mysql_aurora.2.10.2',
        DBClusterIdentifier=db_clu,
        StorageEncrypted=True,
        EnablePerformanceInsights=False,
    )
    print("DB Cluster Instance {0} has been created!!!\n\n".format(list_inst))

            
if __name__ == '__main__':
    recreate_global_cluster()
