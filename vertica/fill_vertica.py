import psycopg2
from time import time
from psycopg2.extras import DictCursor
import vertica_python

STEP = 1000

connection_info = {
    'host': '127.0.0.1',
    'port': 5433,
    'user': 'app',
    'password': '123qwe',
    # 'database': 'docker',
    'autocommit': True,
}


def get_postgres_records():
    with psycopg2.connect(host="localhost", user="app", password="123qwe", database="vtk_postgres") as conn:
        cursor = conn.cursor(cursor_factory=DictCursor)
        query = f"select * from station_rel_10000 offset 12432000;"
        cursor.execute(query)
        while res := cursor.fetchmany(STEP):
            yield res


def fill_vertika():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        count = 0
        for items in get_postgres_records():
            print(count)
            count += 1
            insert_list = []
            for item in items:
                insert_list.append((item["id"], item["id_base1"], item["id_base2"], item["station_id1"],
                                   item["station_id2"], item["distance"], item["node"], item["deleted"],
                                   item["verify"], item["user_id"], item["date_update"]))

            cursor.executemany(
                "INSERT INTO station_rel_10000 (id, id_base1, id_base2, station_id1, station_id2, distance,"
                " node, deleted, verify, user_id, date_update) VALUES"
                " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", insert_list)

        cursor.execute('SELECT count(*) FROM station_rel_10000')
        print("count in station_rel_10000", cursor.fetchall())


if __name__ == "__main__":
    fill_vertika()
