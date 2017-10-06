import json
import pdb
from flask import Flask, request
from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps

app = Flask(__name__)

mongo = MongoClient('localhost', 27017)
app.db = mongo.local

#FETCHING DOCUMENT FROM COLLECTION
#@app.route('/courses', method= ['GET'])
@app.route('/courses', methods=['GET'])
def get_course_by_subject():

    #create a collection request argument
    course_dict = request.args

    #createan subject document filter
    subject_name = course_dict["subject"]

    #create a subject collection
    subject = app.database.courses

    #look trough the database in the collection subject, find subject name
    result = subject.find_one({'subject': subject_name})

    response_json = JSONEncoder().encode(result)

    return (response_json, 200, None)

#@app.route('/courses')
#def fetch_courses():
#
#    course_dict = request.json
#
#    json_subject = dumps(course_dict)
#
#    print (json_subject)
#    return (json_subject,200, None)

if __name__ == '__main__':
    app.run()
#fetch_courses()







