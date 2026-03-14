<h1>Azure Data Engineering</h1>

This repository contains all my hands-on exercises, notes, code, notebooks, and outputs as I learn and practice Azure Data Engineering for 30 days.

🗓️ Day-wise Progress

I am documenting everything I learn each day — with code examples, Google Colab notebooks, theory notes, visuals, and output files.

## 🚀 Day 1 – ETL vs ELT Fundamentals

### Topics Covered

ETL (Extract–Transform–Load)

ELT (Extract–Load–Transform)

Differences, architecture, and use cases

Tools used in ETL vs ELT

Why ELT is preferred in modern cloud systems

### Deliverables

Theory notes

Architecture diagrams

Comparison table

📂 Folder: day-01-etl-elt/
Contains:

ETL-vs-ELT.md

Architecture diagrams

Notes

## 🚀 Day 2 – ETL Hands-On Using Google Colab

### Topics Covered

✔ Loaded CSV directly from GitHub (raw link)
✔ Performed transformations using Pandas
✔ Renamed columns
✔ Filtered rows
✔ Added new calculated fields
✔ Saved processed CSV
✔ Downloaded output

Code Used
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

**1. Rename column**

df = df.rename(columns={"total_bill": "bill_amount"})

**2. Filter rows**

df_filtered = df[df["bill_amount"] > 20]

**3. Add new column**

df_filtered["tip_percent"] = (df_filtered["tip"] / df_filtered["bill_amount"]) * 100

**Save output**

df_filtered.to_csv("processed_tips.csv", index=False)

### Deliverables

📂 day-02-etl-practical/
Contains:

Google Colab notebook (etl_colab_notebook.ipynb)

Output file (processed_tips.csv)

Notes file (day2-notes.md)

## 🚀 Day 3 – Batch Processing vs Stream Processing

### Topics Covered

- Batch Processing
- Stream Processing
- Differences between Batch and Streaming
- Real-world examples

### Deliverables

Folder: `day-03-batch-stream/`

Contains:

- batch-vs-stream.md
- notes
- diagrams

## 📚 Repository Structure
azure-data-engineering
│
├── day-01-etl-elt
│   ├── ETL-vs-ELT.md
│   ├── diagrams
│   └── notes
│
├── day-02-etl-practical
│   ├── etl_colab_notebook.ipynb
│   ├── processed_tips.csv
│   └── day2-notes.md
│
├── day-03-batch-stream
│   ├── batch-vs-stream.md
│   └── diagrams
│
├── datasets
│   └── raw
│
├── README.md
└── LICENSE
