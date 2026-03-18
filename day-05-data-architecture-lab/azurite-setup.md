# 🏗️ Day 5 – Azure Data Lake Lab Using Azurite (Local Emulator)

Azurite is a lightweight Azure Storage emulator that allows you to practice Azure Blob, Queue, and Table Storage without an Azure subscription.

In this lab, we simulate a Data Lake folder structure and interact with it using Python + Azure SDK.

## 📌 1. What You Will Learn

What Azurite is and why Data Engineers use it

How to simulate a Data Lake locally

Creating containers (raw/, processed/, curated/)

How to upload JSON & CSV files

How to connect to Azurite using Python

How to list blobs programmatically

Fixing common Azurite errors (API version issues, authentication, etc.)

## 📥 2. Install Azurite

Run this command on Windows/macOS/Linux:

npm install -g azurite

## ▶️ 3. Start Azurite
azurite --skipApiVersionCheck

This runs Azurite on default local ports:

Service	URL
Blob Storage	http://127.0.0.1:10000/devstoreaccount1

Queue Storage	http://127.0.0.1:10001/devstoreaccount1

Table Storage	http://127.0.0.1:10002/devstoreaccount1

## 🔐 4. Default Storage Credentials

Azurite provides built-in test credentials:

Account Name: devstoreaccount1
Account Key: Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==

No need to change anything.

## 🗂️ 5. Create Data Lake Folder Structure

Open Azure Storage Explorer

Right-click → Create Blob Container → Name it raw

Then create three containers:

raw
processed
curated

These represent typical Bronze (raw), Silver (processed), and Gold (curated) layers.

## 📝 6. Upload Sample Files

Upload the following sample files into raw:

employees.csv

sales.json

data.json

You can create your own small test files.

## 🐍 7. Python Code to Access Azurite

Create a Python file: python-access-azurite.py

from azure.storage.blob import BlobServiceClient

connection_string = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

client = BlobServiceClient.from_connection_string(connection_string)

container = client.get_container_client("raw")

print("Blobs in 'raw' container:")
for blob in container.list_blobs():
    print(" -", blob.name)

Run it:

python python-access-azurite.py

If everything is correct, you will see:

Blobs in 'raw' container:
 - employees.csv
 - sales.json
 - data.json

## 🛠️ 8. Fixing Common Errors
❌ Error: API version not supported
The API version 2026-02-06 is not supported by Azurite

✔ Fix:
Run Azurite with:

azurite --skipApiVersionCheck
❌ Error: AuthorizationFailure

Occurs when connection string is wrong.

✔ Fix:
Ensure you used exactly the default Azurite key.

❌ ModuleNotFoundError: No module named 'azure'

✔ Fix:

pip install azure-storage-blob

## 📦 9. Folder Structure for Day-05
day-05-data-architecture-lab/
│
├── azurite-lab.md
├── python-access-azurite.py
├── screenshots/
│   ├── azurite_running.png
│   ├── storage_explorer_containers.png
│   └── uploaded_files.png
└── sample-data/
    ├── employees.csv
    ├── sales.json
    └── data.json

## 🎉 10. Summary

Today you learned how to run a local Data Lake environment using Azurite:

✔ Created Blob containers
✔ Uploaded raw files
✔ Used Python to list blobs
✔ Fixed API version & authorization issues
✔ Simulated Azure Storage without cloud cost

This is a real Data Engineering skill used in local development.
