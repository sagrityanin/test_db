import psycopg2
from time import time
from psycopg2.extras import DictCursor
from clickhouse_driver import Client, connect
from time import time
from config import settings
client = Client(host=settings.CLICKHOUSE_HOST)

stations = [23011, 135, 23008, 230, 23002, 440, 22659, 2297, 2604, 22936]


def get_clickhouse():
    ch_conn = connect(f"clickhouse://{settings.CLICKHOUSE_HOST}")
    ch_cursor = ch_conn.cursor()
    bigining = time()
    for st1 in stations:
        for st2 in stations:
            start = time()
            query = f"select distance from distance where station_id1 = '{st1}' \
                                and station_id2 = '{st2}'"

            query4 = f"select station_id1 from distance where station_id2 = '{st2}' and\
                                        distance <= 500 or station_id2 in ( select station_id2 from distance \
                                            where station_id1 = '{st1}' and distance <= 500);"
            query2 = f"select r1.station_id1 from distance r1 inner join  \
                                    distance r2 on r1.station_id1 = r2.station_id2 where r2.station_id2 = '{st2}' and\
                                    r2.distance <= 500 and r1.station_id1 <> r1.station_id2;"
            query1 = f"select station_id1 from distance where station_id2 = '{st2}' and\
                                    distance <= 500 and station_id1 <> station_id2;"
            ch_cursor.execute(query2)
            res = ch_cursor.fetchall()
            print(time() - start, "sec")
            # print(st1, st2, res)
    print("all time", time() - bigining, "sec")
    ch_cursor.execute('SELECT count(*) FROM distance')
    print("count in distance", ch_cursor.fetchall(), str(time() - start), "sec")


if __name__ == "__main__":
    get_clickhouse()
