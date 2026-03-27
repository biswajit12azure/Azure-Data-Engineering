# 📘 Day 7 – File Formats: CSV, Parquet, Avro

This session covers three essential file formats every Data Engineer must understand.  
These formats impact **performance**, **storage cost**, and **pipeline speed**.

# 🎯 Learning Objectives
- Understand when to use CSV, Parquet, and Avro
- Explore columnar vs row-based storage
- Compare file size behavior
- Measure read performance using Spark
- Work with Databricks Volumes (since DBFS is disabled in CE)
---

## 🗂️ 1. CSV (Comma Separated Values)
- Row-based
- Human readable
- No schema included
- Large file sizes
- Slow for analytics

**Best For:**  
- Logs  
- Interchange between systems  

---

## 🗂️ 2. Parquet (Columnar Format)
- Columnar storage  
- Built for analytics  
- Highly compressed  
- Supports predicate pushdown  
- Schema included

**Best For:**  
- Data Lakes  
- Warehouses  
- Databricks / Spark workloads  

---

## 🗂️ 3. Avro (Row-Based Schema-Aware Format)
- Row-based  
- Optimized for streaming  
- Schema stored in header  
- Used by Kafka, CDC systems  

**Best For:**  
- Event streaming  
- Messaging systems  
- Schema evolution  

---

# 🧪 Lab Setup (Google Colab / Databricks)

### Install libraries
```python
!pip install pyspark fastavro
```
## 📍 Volume Path

All files are stored under:
```
/Volumes/workspace/default/biswajit/
```
### 1️⃣ Generate 1 Million Records (Synthetic Dataset)
```python
from pyspark.sql.functions import rand, round, udf
from pyspark.sql.types import StringType

names = ["John", "Ana", "Ravi", "Maya", "Leo", "Sara", "Tom", "Nina"]

df_large = spark.range(1_000_000) \
    .withColumn("name_idx", round(rand() * len(names)).cast("int")) \
    .withColumn("salary", (rand() * 1_000_000).cast("int"))

def pick_name(i):
    return names[i % len(names)]

name_udf = udf(pick_name, StringType())
df_large = df_large.withColumn("name", name_udf("name_idx")).drop("name_idx")

df_large.show(5)
```
### 2️⃣ Write Files in All Three Formats
```python
base = "/Volumes/workspace/default/biswajit"

csv_path = f"{base}/large_csv"
parquet_path = f"{base}/large_parquet"
avro_path = f"{base}/large_avro"

df_large.write.option("header", True).mode("overwrite").csv(csv_path)
df_large.write.mode("overwrite").parquet(parquet_path)
df_large.write.format("avro").mode("overwrite").save(avro_path)
```
### 3️⃣ Measure Read Time for Each Format
```python
import time

# CSV
start = time.time()
spark.read.option("header", True).csv(csv_path).count()
csv_time = time.time() - start

# Parquet
start = time.time()
spark.read.parquet(parquet_path).count()
parquet_time = time.time() - start

# Avro
start = time.time()
spark.read.format("avro").load(avro_path).count()
avro_time = time.time() - start

print(f"CSV read time: {csv_time:.4f}s")
print(f"Parquet read time: {parquet_time:.4f}s")
print(f"Avro read time: {avro_time:.4f}s")
```
### 4️⃣ Approximate In-Memory Size (Not Disk Size!)
```python
from pyspark.sql.functions import length, concat_ws, sum as _sum

def approx_size(df):
    return df.withColumn("row_len", length(concat_ws(",", *df.columns))) \
             .agg(_sum("row_len")).collect()[0][0]

df_csv = spark.read.option("header", True).csv(csv_path)
df_parquet = spark.read.parquet(parquet_path)
df_avro = spark.read.format("avro").load(avro_path)

csv_size = approx_size(df_csv)
parquet_size = approx_size(df_parquet)
avro_size = approx_size(df_avro)

print(csv_size, parquet_size, avro_size)
```
## 📊 Results (Your Output)
### Approximate Data Size in Chars (same for all formats)
```
CSV: 17403205  
Parquet: 17403205  
Avro: 17403205
```
### Read Performance (your execution results)
```
CSV read time: 1.6256s
Parquet read time: 0.8772s
Avro read time: 1.1195s
```
## 📌 Why Size Was Same? Important Note
The size computed is in-memory row length, not actual disk size.

- Parquet and Avro are binary formats → disk size is much smaller with compression
- CSV is plain text → often the largest on disk

👉 But Databricks CE Volumes doesn’t allow file-size listing (dbutils.fs.ls), so we use in-memory estimates.

## 📎 Summary Table
| Format      | Read Speed (Fast → Slow) | Best Use Case                      |
| ----------- | ------------------------ | ---------------------------------- |
| **Parquet** | ⭐ Fastest                | Analytics, Big Data                |
| **Avro**    | ⭐⭐ Medium                | Streaming, Kafka, Schema evolution |
| **CSV**     | ⭐⭐⭐ Slowest              | Debugging, Simple ingestion        |

This lab demonstrates real-world differences between file formats using 1M records on Databricks CE.
