from datetime import datetime
import pymongo

import json
from time import time
import pickle
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["vtk"]
collection = db["distance"]

# collection.delete_many({})

stations_list = [23011, 135, 23008, 230, 23002, 440, 22659, 2297, 2604, 22936]
bigining = time()
for station1 in stations_list:
    for station2 in stations_list:
        start = time()
        query = {"station_id1": station1,
                "station_id2": station2}
        # select  station_id1 from station_rel_10000 where
        # station_id2 = '{st2}' and distance <= 500 and station_id1 <> station_id2
        query = {"station_id2": station2,
                 "distance": { "$lte": 500 }}

        res = collection.find(query)
        for line in res:
            print(line["station_id1"], end=", ")
        print()
        if res is not None:
            print(station1, station2, str(time() - start))
print("Total time", str(time() - bigining), "sec")
start = time()
count = collection.count_documents({})
print("Count ", count, "by", str(time() - start), "sec")

