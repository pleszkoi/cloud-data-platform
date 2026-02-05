# Cloud Data Platform – Homelab Project

## Overview

This project simulates a simplified cloud-based data platform in a local homelab environment using Docker containers.
The goal is to understand how cloud data pipelines work in practice, including storage, processing, and database integration.

The system ingests CSV data into an S3-compatible object storage (MinIO), processes it with a Python-based pipeline, and loads it into a PostgreSQL database.

This project is designed as a learning environment for cloud engineering and data platform concepts.

## Architecture

```plsql
CSV file
   │
   ▼
MinIO (S3-like Object Storage)
   │
   ▼
Python Data Pipeline (Docker container)
   │
   ▼
PostgreSQL Database
```
All components run in isolated Docker containers orchestrated with Docker Compose.

## Technologies

- Linux (Ubuntu)
- Docker & Docker Compose
- PostgreSQL
- MinIO (S3-compatible object storage)
- Python (pandas, boto3, psycopg2)
- Git & GitHub

Cloud concepts simulated locally:

- Object Storage (S3)
- Data pipeline / ETL
- Containerized services
- Infrastructure-as-Code mindset

## Data Pipeline Flow

1. A CSV file is uploaded to a MinIO bucket.
2. The Python pipeline container retrieves the CSV via the S3 API.
3. The data is parsed using pandas.
4. The processed data is inserted into PostgreSQL.
5. The pipeline container exits after successful execution.

This workflow simulates a real-world data ingestion and processing pipeline.

## Project Structure

<pre>
cloud-data-platform/
├── ci-cd/
├── docs/
├── homelab/
│   └── docker/
│       ├── data/
│       |   └── sample.csv
│       ├── docker-compose.yml
│       ├── .env
│       ├── postgres/
│       └── python/
│           ├── Dockerfile
│           ├── pipeline.py
│           └── requirements.txt
├── scripts/
└── terraform/
</pre>

## Setup & Run

### Start services

```bash
docker compose up --build
```

### Upload sample data to MinIO

Example CSV:
```csv
id,name,amount
1,apple,10
2,banana,5
3,orange,7
```
Upload to MinIO bucket (raw-data).

### Verify data in PostgreSQL

```bash
docker exec -it postgres psql -U data_user -d data_platform
```

```sql
SELECT * FROM sales;
```

## Example Workflow

- MinIO simulates cloud object storage (Azure Blob / AWS S3).
- PostgreSQL simulates a data warehouse or operational database.
- Python simulates a data processing job (ETL/ELT).
- Docker Compose simulates a microservice-based architecture.

