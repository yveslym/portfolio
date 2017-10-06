from pymongo import MongoClient
from mongoengine import *
from flask import Flask
from flask_pymongo import PyMongo
from flask import Flask, request, make_response
#from flask_restful import Resource
from utils.mongo_json_encoder import JSONEncoder
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.BlogDB
app.bcrypt_rounds = 12
#api = Api(app)

@app.route('/user', method=['GET'])
def get_user():
    user_age_dict = request.args

    first_name = int(user_age_dict['first_name'])

    users_collection = app.db.user

    result = users_collection.find_one({'first_name': first_name})

    response_json = JSONEncoder().encode(result)

    return (response_json, 200, None)

if __name__ == '__main__':
    app.run()