from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

port = os.getenv('MONGO_PORT')
host = os.getenv('MONGO_HOST')

mongo_db_port = int(port)
mongo_client = MongoClient('localhost', mongo_db_port)