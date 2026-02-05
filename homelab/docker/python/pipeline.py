import os
import boto3
import psycopg2
import pandas as pd
from io import BytesIO

#Environment variables
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

MINIO_USER = os.getenv("MINIO_ROOT_USER")
MINIO_PASSWORD = os.getenv("MINIO_ROOT_PASSWORD")

# MinIO (S3) client
s3 = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id=MINIO_USER,
    aws_secret_access_key=MINIO_PASSWORD,
)

# CSV letöltése MinIO-ból
obj = s3.get_object(Bucket="raw-data", Key="sample.csv")
df = pd.read_csv(BytesIO(obj["Body"].read()))

# PostgreSQL kapcsolat
conn = psycopg2.connect(
    host="postgres",
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

cur = conn.cursor()

# Tábla létrehozás (idempotens)
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INT,
    name TEXT,
    amount INT
)
""")

# Adatok betöltése
for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO sales (id, name, amount) VALUES (%s, %s, %s)",
        (row["id"], row["name"], row["amount"])
    )

conn.commit()
cur.close()
conn.close()

print("Pipeline finished successfully")