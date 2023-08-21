from dotenv import load_dotenv, find_dotenv
import os
import urllib.parse
from pymongo import MongoClient

load_dotenv(find_dotenv())

username = urllib.parse.quote_plus(os.environ.get('MONGODB_USER'))
password = urllib.parse.quote_plus(os.environ.get('MONGODB_PWD'))
URL = os.environ.get('MONGODB_URL')

# print(username)
# print(password)

CONNECTION_STRING = URL % (username, password)
client = MongoClient(CONNECTION_STRING)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# print(CONNECTION_STRING)
