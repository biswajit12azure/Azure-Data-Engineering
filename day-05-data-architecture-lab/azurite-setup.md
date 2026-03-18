# 🏗️ Day 5 – Azure Data Lake Lab Using Azurite (Local Emulator)
Azurite is a lightweight Azure Storage emulator that lets you practice Blob, Queue, and Table Storage locally — without an Azure subscription.
In this lab, we simulate a Data Lake architecture (raw → processed → curated) and access it using Python + Azure SDK.

## 📌 1. What You Will Learn
•	🔹 What Azurite is and why Data Engineers use it
•	🔹 How to simulate a local Data Lake
•	🔹 Creating containers: raw/, processed/, curated/
•	🔹 Uploading JSON & CSV files
•	🔹 Connecting Python to Azurite
•	🔹 Listing blobs programmatically
•	🔹 Fixing authentication & API version issues

## 📥 2. Install Azurite
Run this command on Windows/macOS/Linux:
npm install -g azurite

## ▶️ 3. Start Azurite
azurite --skipApiVersionCheck
Default local endpoints:
Service	URL:
Blob Storage	http://127.0.0.1:10000/devstoreaccount1
Queue Storage	http://127.0.0.1:10001/devstoreaccount1
Table Storage	http://127.0.0.1:10002/devstoreaccount1

## 🔐 4. Default Storage Credentials
Azurite includes built-in development credentials:
Account Name: devstoreaccount1
Account Key: Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==

## 🗂️ 5. Create Data Lake Folder Structure
- Open Azure Storage Explorer →
- Right-click → Create Blob Container
- Create:
  raw
  processed
  curated
- These represent:
•	🟤 Bronze → raw
•	⚪ Silver → processed
•	🟡 Gold → curated

## 📝 6. Upload Sample Files
Upload the following into raw:
•	employees.csv
•	sales.json
•	data.json
(You can create simple test files.)

## 🐍 7. Python Code to Access Azurite
Create a file named: python-access-azurite.py
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
Run:
python python-access-azurite.py
Expected output:
Blobs in 'raw' container:
 - curomers.csv
 - device.json

## 🛠️ 8. Fixing Common Errors
❌ API version not supported
The API version 2026-02-06 is not supported by Azurite
✔ Fix:
azurite --skipApiVersionCheck

❌ AuthorizationFailure
Occurs when connection string or key is mismatched.
✔ Fix:
Use the exact default Azurite key.

❌ ModuleNotFoundError: No module named 'azure'
✔ Install Azure Blob SDK:
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

## 🎉 10. Summary
Today you created a fully functional local Data Lake using Azurite:
✔ Created Blob containers
✔ Organized data into raw/processed/curated
✔ Uploaded CSV & JSON files
✔ Accessed data with Python
✔ Resolved API + authentication issues
✔ Built a local Azure-like development environment
This is exactly how professional Data Engineers test pipelines before pushing to Azure.

