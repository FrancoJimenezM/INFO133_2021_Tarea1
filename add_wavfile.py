from pymongo import MongoClient
import gridfs

MONGO_URL = 'mongodb://localhost'
client = MongoClient(MONGO_URL)
db = client['FuSA']

file_name = "human.wav"
file_location = "/sounds_wav/" + file_name
file_data = open(file_location, 'rb')
data = file_data.read()
fs = gridfs.GridFS(db)
fs.put(data,filename = file_name)

data = db.fs.files.find_onde({'filename':file_name})

#Lo añade pero como un archivo por chunks con data
#como binarios que no pude transformar nuevamente a audio.

