import pymongo
import os

db_user = os.environ.get('DB_USER', 'albertshady')
db_pass = os.environ.get('DB_PASS', 'tyJtiw-vazhy1-risxyr')

client = pymongo.MongoClient(
   f'mongodb://{db_user}:<{db_pass}>@shadycluster-iawb7.mongodb.net/test?retryWrites=true&w=majority')

db = client.test


# if __name__ == '__main__':
#     print(db_user, db_pass)

# db_user = 'albertshady'
# db_pass = 'tyJtiw-vazhy1-risxyr'
