Day 05 – Local Data Lake Simulation Using Azurite

Today’s goal:
Simulate Azure Data Lake Storage locally using Azurite, and interact with it using Python SDK.

✅ 1. Install Azurite (Free & Local)
npm install -g azurite

If you see warnings (deprecated packages) — ignore them. Azurite will still work fine.

✅ 2. Start Azurite
azurite --silent --location . --debug azurite_debug.log

It opens three endpoints:

Blob → http://127.0.0.1:10000

Queue → http://127.0.0.1:10001

Table → http://127.0.0.1:10002

✅ 3. Default Azurite Credentials
AccountName: devstoreaccount1
AccountKey: Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==

Connection String:

DefaultEndpointsProtocol=http;
AccountName=devstoreaccount1;
AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;
BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;
✅ 4. Create Containers (Raw / Processed / Curated)

Use Azure Storage Explorer (recommended) or Python.

Containers:

raw/
processed/
curated/

Upload sample JSON/CSV files to raw/.

✅ 5. Python Script to List Blobs (adl.py)
from azure.storage.blob import BlobServiceClient

connection_string = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

client = BlobServiceClient.from_connection_string(connection_string)

container = client.get_container_client("raw")

print("Blobs in 'raw/' container:\n")
for blob in container.list_blobs():
    print(blob.name)