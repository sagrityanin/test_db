import psycopg2
from time import time
from psycopg2.extras import DictCursor
from clickhouse_driver import Client, connect

client = Client(host="localhost")

STEP = 1000


def get_postgres_records():
    with psycopg2.connect(host="localhost", user="app", password="123qwe", database="vtk_postgres") as conn:
        cursor = conn.cursor(cursor_factory=DictCursor)
        query = f"select * from station_rel_10000 ;"
        cursor.execute(query)
        while res := cursor.fetchmany(STEP):
            yield res


def fill_clickhouse():
    ch_conn = connect('clickhouse://localhost')
    ch_cursor = ch_conn.cursor()
    count = 0
    for items in get_postgres_records():
        print(count)
        count += 1
        insert_list = []
        for item in items:
            insert_list.append({"id": item["id"], "id_base1": item["id_base1"], "id_base2": item["id_base2"],
                                "station_id1": item["station_id1"], "station_id2": item["station_id2"],
                                "distance": item["distance"], "node": item["node"],
                                "deleted": item["deleted"], "verify": item["verify"],
                                "user_id": item["user_id"], "date_update": item["date_update"]})
        ch_cursor.executemany("INSERT INTO default.distance VALUES", insert_list)

    ch_cursor.execute('SELECT count(id) FROM distance')
    print("count in station_rel_10000", ch_cursor.fetchall())


if __name__ == "__main__":
    fill_clickhouse()
