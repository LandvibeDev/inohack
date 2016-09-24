from pymongo import MongoClient
import datetime

connection = MongoClient("localhost",27017)
db = connection.LIBINFO
collection = db.lib

date,time = str(datetime.datetime.utcnow()).split()
temperature : 25
temperature_state : "good"
humidity : 70
humidity_state : "normal"
air_pollution : 500
air_pollution : "bad"

lib = {
    "jungsuck":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    },
    "it_engineer":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    },
    "engineer":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    },
    "liberal":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    },
    "business":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    },
    "education":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    },
    "living":{
        "date": date,
        "time": time,
        "temperature" : temperature,
        "temperature_state" : temperature_state,
        "humidity": humidity,
        "humidity_state":humidity_state,
        "air_pollution": air_pollution,
        "air_pollution_state": air_pollution_state
    }
}


collection.insert(lib)


print("lib :", lib)
print("collection_info", db.collection_names())
