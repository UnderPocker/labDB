from sqlalchemy import create_engine
import pandas as pd
from sqlite3 import connect
from config import *

import psycopg2_bench as DB_psycopg2
import sqlite3_bench as DB_sqlite3
import duckdb_bench as DB_duckdb

# Reading data from dataset
# ------------------------------------------------------------------------------
df = pd.read_csv(f"data\\{dataset}")
df = df.drop(columns=["Airport_fee"])
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
df = df.rename(columns={"Unnamed: 0": "id"})
# ------------------------------------------------------------------------------

# Insert data in PostgreSQL
# ------------------------------------------------------------------------------
path = f"postgresql://{username}:{password}@{hostname}:{port}/{name_database}"
engine = create_engine(path)
df.to_sql("trips", engine, if_exists="replace", index=False, chunksize=10000)
engine.dispose()
# ------------------------------------------------------------------------------


# Insert data in SQLite
# ------------------------------------------------------------------------------
con = connect(f"data\\database.db")
df.to_sql("trips", con, if_exists="replace", index=False, chunksize=10000)
con.close()
# ------------------------------------------------------------------------------


# Run queries
# ------------------------------------------------------------------------------
if sqlite3: print("SQLite3:", *DB_sqlite3.run())
if psycopg2: print("Psycopg2:", *DB_psycopg2.run())
if duckdb: print("Duckdb:", *DB_duckdb.run())
# ------------------------------------------------------------------------------
