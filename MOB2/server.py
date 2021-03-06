from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
from utils.mongo_json_encoder import JSONEncoder
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.server
app.bcrypt_rounds = 12
api = Api(app)


## Write Resources here
class User(Resource):
    def get(self):
        user_collect = app.db.users
        user_dict = user_collect.find()
        if user_dict is None:
            response = jsonify(data=[])
            pdb.set_trace()
            response.status_code = 404
            return response
        else:
            return myobject
    def post(self):
        user_dict = request.json
        user_collect = app.db.users

        result = user_collect.insert_one(user_dict)
        return result




## Add api routes here

#  Custom JSON serializer for flask_restful
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(JSONEncoder().encode(data), code)
    resp.headers.extend(headers or {})
    return resp

if __name__ == '__main__':
    # Turn this on in debug mode to get detailled information about request
    # related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)