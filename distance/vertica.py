import vertica_python
from time import time
from datetime import datetime, timedelta
import random
import uuid
from config import settings

stations = [23011, 135, 23008, 230, 23002, 440, 22659, 2297, 2604, 22936]

connection_info = {
    'host': settings.VERTICA_HOST,
    'port': settings.VERTICA_PORT,
    'user': settings.VERTICA_USER,
    'password': settings.VERTICA_PASSWORD,
    # 'database': 'docker',
    'autocommit': True,
}

with vertica_python.connect(**connection_info) as connection:
    cursor = connection.cursor()
    all_duration = 0
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

    query_count = "select count(*) from station_rel_10000"
    cursor.execute(query_count)
    res = cursor.fetchone()
    print("Count", res, "by", str(time() - start), "sec")


    # for i in range(1):
    #     start_time = time.time()
    #     cursor.execute("SELECT count(id) FROM station_rel_10000;")
    #     res = cursor.fetchone()
    #     duration = time.time() - start_time
    #     print(i, res[0])
    #     # time.sleep(0.1)
    #     all_duration += duration
    # print("Midle time ", str(all_duration/100))