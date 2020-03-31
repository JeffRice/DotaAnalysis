import pymongo

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')

db = client.dotatest

matches = db.Matches

match_data = {"matchID": 2341343, "duration": 1440, "radiant_win": "True"  }

result = matches.insert_one(match_data)

print('One match: {0}'.format(result.inserted_id))
