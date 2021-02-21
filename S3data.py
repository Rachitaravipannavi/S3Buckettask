import boto3
def filterBySClass():
    SC=int(input('storage type \nplease enter associate number from the above \n1.Standard \n2.IA \n3.RR\n'))
    if SC==1:
        SClass="STANDARD"
    elif SC==2:
        SClass="STANDARD_IA"
    elif SC==3:
        SClass="REDUCED_REDUNDANCY"
    else:
        main()
    return SClass

client=boto3.client('s3')
def bls(SC):
    bucketlist=client.list_buckets()
    for bucket in bucketlist['Buckets']:
        files=ols(bucket['Name'],SC)
        if files:
            print('Name:',bucket['Name'])
            print('Creation Date:',bucket['CreationDate'])
            print('number of files:',len(files))
            totalSize=0
            for file in files:
                totalSize +=file['Size']
                
            if totalSize < 1000:
                print('Total size of files:',totalSize,'bytes')    
            elif totalSize< 1000000:
                print('Total size of files:',totalSize/1000,'Kb') 
            else:
                print('Total size of files:',totalSize/1000000,'Mb')   
            
            print('Last modified date of the most recent file:',files[-1]['LastModified'])
            print('------------------------------------------------------')


def ols(bucketName,SC):
    objectlist=client.list_objects(Bucket=bucketName)
    files=[]
    for file in objectlist['Contents']:
        if file['StorageClass']==SC:
            files.append(file)

    return files

def main():
    SC=filterBySClass()

    bls(SC)

main()