import psycopg2
from time import time
from psycopg2.extras import DictCursor
from clickhouse_driver import Client, connect
from time import time
client = Client(host="localhost")




def fill_clickhouse():
    ch_conn = connect('clickhouse://localhost')
    ch_cursor = ch_conn.cursor()
    start = time()
    ch_cursor.execute('SELECT count(*) FROM distance')
    print("count in distance", ch_cursor.fetchall(), str(time() - start), "sec")


if __name__ == "__main__":
    fill_clickhouse()
