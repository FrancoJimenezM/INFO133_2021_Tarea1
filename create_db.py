import json
from pymongo import MongoClient

MONGO_URL = 'mongodb://localhost'
client = MongoClient(MONGO_URL)
db = client['FuSA']

collection_recordings = db["Grabaciones"]
collection_fonts = db["Fuentes"]

collection_recordings.insert_one(
    {
    "user": {
        "rut" : "20429849-1",
        "name" : "Franco",
        "last_name":"Jimenez"
    },
    "record_date":"20 de Julio de 2021",
    "duration":"0:10",
    "latitude":-39.8139,
    "longitude":-73.2458,
    "city":"Valdivia",
    "format":".wav",
    "outside":True,
    "segment": {
        "format":".mp3",
        "duration":"0:05",
        "start":"0:03",
        "end":"0:08",
        "attributes": {
            "font_name":"Moto",
            "description":"Una moto pasa por delante",
            "analyzer_id":0,
            "confidence":"100%"
        }
    }
    }
)
collection_fonts.insert_one(
    {
    "_id": 'ObjectId("60f6391a4db4c19c3d29602e")',
    "type":"Vehiculo",
    "description":"Es un medio de transporte",
    "subcategory":["Moto","Auto","Autobus","Bus","Patineta"]
    }
)

collection_recordings.insert_one(
    {
    "user": {
        "rut" : "20429849-1",
        "name" : "Franco",
        "last_name":"Jimenez"
    },
    "record_date":"20 de Julio de 2021",
    "duration":"0:12",
    "latitude":-39.824464,
    "longitude":-73.242242,
    "city":"Valdivia",
    "format":".wav",
    "outside":False,
    "segment": {
        "format":".wav",
        "duration":"0:06",
        "start":"0:06",
        "end":"0:12",
        "attributes": {
            "font_name":"Sirena",
            "description":"Suena una alarma",
            "analyzer_id":1,
            "confidence":"92%"
        }
    }
    }
)
collection_fonts.insert_one(
    {
    "_id": 'ObjectId("60f6391a4db4c19c3d29602e")',
    "type":"Alarma",
    "description":"Señal que avisa un peligro",
    "subcategory":["Sirena","Anti incendios","Ambulancia","Evacuación"]
    }
)


collection_recordings.insert_one(
    {
    "user": {
        "rut" : "20429849-1",
        "name" : "Franco",
        "last_name":"Jimenez"
    },
    "record_date":"20 de Julio de 2021",
    "duration":"0:03",
    "latitude":-39.832241,
    "longitude":-73.220442,
    "city":"Valdivia",
    "format":".wav",
    "outside":False,
    "segment": {
        "format":".wav",
        "duration":"0:02",
        "start":"0:01",
        "end":"0:03",
        "attributes": {
            "font_name":"Estornudo",
            "description":"Una persona estornuda",
            "analyzer_id":2,
            "confidence":"81%"
        }
    }
    }
)
collection_fonts.insert_one(
    {
    "_id": 'ObjectId("60f6391a4db4c19c3d29602e")',
    "type":"Humano",
    "description":"Sonidos hechos por personas",
    "subcategory":["Estornudo","Tos","Pasos","Conversaciones"]
    }
)
