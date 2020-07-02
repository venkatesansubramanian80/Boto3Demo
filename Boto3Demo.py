import boto3

client = boto3.client('ecs')
response = client.list_services(cluster="python-cluster", maxResults=100)

"""
print(response['serviceArns'])
response = client.stop_task(cluster="",
                            task="", reason="For Testing")
"""

response = client.list_clusters(maxResults=100)
for single_task in response['clusterArns']:
    print(single_task)
    print("------------------")
    sub_response = client.list_tasks(cluster=single_task, maxResults=100)
    for sub_task in sub_response['taskArns']:
        print(sub_task)
    print("------------------")
