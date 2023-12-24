from time import perf_counter
from config import *
import duckdb

def run():
    duckdb.install_extension("sqlite")
    time = [0] * COUNT
    db_con = duckdb.connect(f"data\\database.db")
    cur = db_con.cursor()
    for i in range(COUNT):
        for j in range(TRIALS):
            start = perf_counter()
            cur.execute(queries["duckdb"][i])
            finish = perf_counter()
            time[i] += finish - start
    cur.close()
    db_con.close()
    return list(map(lambda x: round(x / TRIALS, 8), time))
