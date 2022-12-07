from clickhouse_driver import Client

client = Client(host="localhost")

print(client.execute(("DROP TABLE distance")))
print(client.execute("SHOW DATABASES"))

create_query = """CREATE TABLE default.distance (id Int32, id_base1 Int32 NULL, id_base2 Int32 NULL,
            station_id1 Int32 , station_id2 Int32, distance Int32, node Int32 NULL, deleted Int32 NULL,
             verify UInt8 NULL, user_id Int32 NULL,
               date_update DateTime NULL) engine = Log """
client.execute(create_query)
print(client.execute("SHOW TABLES from default"))
