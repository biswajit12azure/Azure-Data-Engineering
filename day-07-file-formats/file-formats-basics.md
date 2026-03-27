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
