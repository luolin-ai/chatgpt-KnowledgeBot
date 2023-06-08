import datetime
from pymongo import MongoClient
class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://root:Is2WQKd0lPxx8jY0@45.204.10.148:27017/')
        self.db = self.client['wxjqr']
        self.chat_collection = self.db['chat_collection']

    def insert_chat(self, session_id, query, response):
        chat_document = {
            'session_id': session_id,
            'query': query,
            'response': response,
            'timestamp': datetime.datetime.now()
        }
        self.chat_collection.insert_one(chat_document)

    def close(self):
        self.client.close()
