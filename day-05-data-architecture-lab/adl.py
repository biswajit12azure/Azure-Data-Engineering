from azure.storage.blob import BlobServiceClient

connection_string = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUHb8G==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

client = BlobServiceClient.from_connection_string(
    connection_string,
    api_version="2021-08-06"   # 👈 IMPORTANT
)

container = client.get_container_client("raw")

print("Blobs in container:")
for blob in container.list_blobs():
    print(blob.name)