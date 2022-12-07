import psycopg2
from time import time
from psycopg2.extras import DictCursor
from clickhouse_driver import Client, connect
from time import time
client = Client(host="192.168.1.102")

stations = [23011, 135, 23008, 230, 23002, 440, 22659, 2297, 2604, 22936]


def get_clickhouse():
    ch_conn = connect('clickhouse://192.168.1.102')
    ch_cursor = ch_conn.cursor()
    bigining = time()
    for st1 in stations:
        for st2 in stations:
            start = time()
            query = f"select station_id1 from distance where station_id2 = '{st2}' and\
                                                    distance <= 500 and station_id1 <> station_id2;"
            ch_cursor.execute(query)
            res = ch_cursor.fetchall()
            print(time() - start, "sec", end=": ")
            print(st1, st2, res)
    print("all time", time() - bigining, "sec")
    ch_cursor.execute('SELECT count(*) FROM distance')
    print("count in distance", ch_cursor.fetchall(), str(time() - start), "sec")


if __name__ == "__main__":
    get_clickhouse()
