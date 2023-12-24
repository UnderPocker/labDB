TRIALS = 10

# Info to connect to PostgreSQL
name_database = ""
username = ""
password = ""
hostname = ""
port = ""

# File name with data
dataset = ""

# Queries for modules
COUNT = 4
queries = {
    "sqlite3": [
        f"""SELECT "VendorID", COUNT(*)
        FROM "trips" GROUP BY 1;""",
        f"""SELECT "passenger_count", AVG("total_amount")
       FROM "trips" GROUP BY 1;""",
        f"""SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
       FROM "trips" GROUP BY 1, 2;""",
        f"""SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
    ],
    "psycopg2": [
        f"""SELECT "VendorID", COUNT(*)
        FROM "trips" GROUP BY 1;""",
        f"""SELECT "passenger_count", AVG("total_amount")
       FROM "trips" GROUP BY 1;""",
        f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM "trips" GROUP BY 1, 2;""",
        f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
    ],
    "duckdb": [
        f"""SELECT "VendorID", COUNT(*)
        FROM "trips" GROUP BY 1;""",
        f"""SELECT "passenger_count", AVG("total_amount")
       FROM "trips" GROUP BY 1;""",
        f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM "trips" GROUP BY 1, 2;""",
        f"""SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
    ],
}

# Dictionary to connect to PostgreSQL
params = {
    "dbname": name_database,
    "user": username,
    "password": password,
    "host": hostname,
    "port": port,
}

# Modules
sqlite3 = True
psycopg2 = True
duckdb = True
