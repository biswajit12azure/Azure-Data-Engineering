# 🚀 Day 4 – Data Lake vs Data Warehouse vs Lakehouse

## 📌 What is a Data Lake?

A **Data Lake** is a storage system that stores **raw data in its original format**.

- Supports structured, semi-structured, and unstructured data
- Uses **schema-on-read** (structure is applied when reading data)
- Highly scalable and cost-effective

### Examples:
- Logs
- Images
- JSON / CSV files
- IoT data

### Key Features:
- Stores raw data
- Flexible schema
- Used for big data and analytics

---

## 📌 What is a Data Warehouse?

A **Data Warehouse** is a system designed to store **structured and processed data** for reporting and analytics.

- Uses **schema-on-write** (data must be structured before storing)
- Optimized for fast SQL queries
- Ensures data quality and consistency

### Examples:
- Business reports
- Financial dashboards
- Sales analytics

### Key Features:
- Structured data only
- High performance queries
- Data is cleaned and transformed before loading

---

## 📌 What is a Lakehouse?

A **Lakehouse** combines the features of both:

👉 Data Lake + Data Warehouse

It allows you to:
- Store raw data like a Data Lake
- Perform analytics like a Data Warehouse

### Key Component:
- **Delta Lake** (core of Lakehouse architecture)

---

## ⚡ What is Delta Lake?

**Delta Lake** is a storage layer that brings:

- ACID transactions
- Data reliability
- Schema enforcement
- Versioning (time travel)

It converts a Data Lake into a **Lakehouse architecture**.

---

## 🔥 Comparison Table

| Feature | Data Lake | Data Warehouse | Lakehouse |
|--------|----------|---------------|-----------|
| Data Type | All types | Structured only | All types |
| Schema | Schema-on-read | Schema-on-write | Hybrid |
| Cost | Low | High | Medium |
| Performance | Medium | High | High |
| Use Case | Big data, ML | BI & reporting | Modern analytics |

---

## 🎯 Summary

- **Data Lake** → Raw, flexible, scalable  
- **Data Warehouse** → Structured, fast, reliable  
- **Lakehouse** → Best of both worlds  

---

📂 Folder: `day-04-data-architecture/`
