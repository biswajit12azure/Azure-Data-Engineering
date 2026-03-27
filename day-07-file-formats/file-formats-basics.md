# 📘 Day 7 – File Formats: CSV, Parquet, Avro

This session covers three essential file formats every Data Engineer must understand.  
These formats impact **performance**, **storage cost**, and **pipeline speed**.

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

# 🧪 Hands-on (Google Colab / Databricks)

### Install libraries
```python
!pip install pyspark fastavro
```

# 🎯 Learning Objectives
Understand when to use CSV, Parquet, and Avro
Explore columnar vs row-based storage
Compare file size behavior
Measure read performance using Spark
Work with Databricks Volumes (since DBFS is disabled in CE)
