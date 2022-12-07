import vertica_python

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
    cursor.execute("""
    CREATE TABLE station_rel_10000 (
        id INTEGER NOT NULL, 
        id_base1 INTEGER, 
        id_base2 INTEGER,
        station_id1 INTEGER,
        station_id2 INTEGER, 
        distance INTEGER,
        node INTEGER, 
        deleted INTEGER, 
        verify INTEGER, 
        user_id INTEGER, 
        date_update DATETIME
    );
    """)
