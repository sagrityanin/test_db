import vertica_python
import time
from datetime import datetime, timedelta
import random
import uuid


connection_info = {
    'host': '127.0.0.1',
    'port': 5433,
    'user': 'app',
    'password': '123qwe',
    # 'database': 'docker',
    'autocommit': True,
}

with vertica_python.connect(**connection_info) as connection:
    cursor = connection.cursor()
    all_duration = 0
    for i in range(1):
        start_time = time.time()
        cursor.execute("SELECT count(id) FROM station_rel_10000;")
        res = cursor.fetchone()
        duration = time.time() - start_time
        print(i, res[0])
        # time.sleep(0.1)
        all_duration += duration
    print("Midle time ", str(all_duration/100))