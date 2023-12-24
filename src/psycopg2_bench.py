from time import perf_counter
from config import *
import psycopg2

def run():
    time = [0] * COUNT
    db_con = psycopg2.connect(**params)
    cur = db_con.cursor()
    for i in range(COUNT):
        for j in range(TRIALS):
            start = perf_counter()
            cur.execute(queries["psycopg2"][i])
            finish = perf_counter()
            time[i] += finish - start
    cur.close()
    db_con.close()
    return list(map(lambda x: round(x / TRIALS, 8), time))
