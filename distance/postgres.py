import psycopg2
from time import time
from config import settings

stations =  [23011, 135, 23008, 230, 23002, 440, 22659, 2297, 2604, 22936]

with psycopg2.connect(host=settings.POSTGRES_HOST, user=settings.POSTGRES_USER,
                      password=settings.POSTGRES_PASSWORD, database=settings.POSTGRES_DATABASE) as conn:
    cursor = conn.cursor()
    bigining = time()
    for st1 in stations:
        for st2 in stations:
            start = time()
            query = f"select distance from station_rel_10000 where station_id1 = '{st1}' \
                    and station_id2 = '{st2}'"

            query4 = f"select station_id1 from station_rel_10000 where station_id2 = '{st2}' and\
                            distance <= 500 or station_id2 in ( select station_id2 from station_rel_10000 \
                                where station_id1 = '{st1}' and distance <= 500);"
            query2 = f"select r1.station_id1 from station_rel_10000 r1 inner join  \
                                station_rel_10000 r2 on r1.station_id1 = r2.station_id2 where r2.station_id2 = '{st2}' and\
                                                        r2.distance <= 500 and r1.station_id1 <> r1.station_id2;"
            query1 = f"select station_id1 from station_rel_10000 where station_id2 = '{st2}' and\
                        distance <= 500 and station_id1 <> station_id2;"

            cursor.execute(query2)
            res = cursor.fetchall()
            print(time() - start, "sec")
            # print(st1, st2, res)

    print("all time", time() - bigining, "sec")
    start = time()
    query_count = "select count(*) from station_rel_10000"
    cursor.execute(query_count)
    res = cursor.fetchone()
    print("Count", res, "by", str(time() - start), "sec")

