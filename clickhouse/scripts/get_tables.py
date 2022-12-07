from clickhouse_driver import Client

client = Client(host="localhost")

print(client.execute("SHOW DATABASES"))
print(client.execute("SHOW TABLES from default"))
