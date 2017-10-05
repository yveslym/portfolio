import json
import pdb
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient('localhost', 27017)
app.db = mongo.local

@app.route('/person')
def person_route():
    #pdb.set_trace()
    person = {name:"yves", 'age': 24}
    json_person = json.dumps(person)
    return (json_person, 200, None)

def hello_world():
    return 'Hello World!'


#challenge
#Add a new route called my_page and return some text.
@app.route('/my_page')
def print_some_thing():
    print("Hello Yveslym")

#Use Paw or Postman to perform a get request to a "/pets" routes and return a list of your favorite pets in JSON format.

@app.route('/pets')
def pet_route():
    pets = [{'name': "charlie", 'color': "Brow"}, {'name': "Bingo", 'color': "Blue"}]
    json_pets = json.dumps(pets)
    return (json_pets, 200, None)

#Add a new route handler that receives POST requests to the route /pets with JSON data in the body(an array of
#pet objects) and returns that JSON data unmodified in the response body. Test the /pets route using Paw, Curl,
#Postman, or another tool to make HTTP POST requests to ensure it responds correctly with the same data given
#in the request.

#create a course root


# Matthew code
#if __name__ == '__main__':
#    app.run()
#    course_dictionary = {"subject": "Science","course_id": 38428,"students":["Matthew","ShannonDougherty","Corey", "Steven Spielberg"]}
#    client = MongoClient('mongodb://localhost:27017/')
#    # This essentially creates our database
#    db = client["courses"]
#    # This is what is going to be creating our collection within the database
#    subject_courses = db.subject_courses
#    subject_courses.drop()
#    #  Now that we have a collection we have to be able to create the documents that populate the collection
#    subject_courses.insert_one(course_dictionary)
#
##We are going to create another document that serves as another documents
#    second_course_dictionary = {"name": "Social Studies","course_id": 32334,"students": ["Matthew", "Corey", "Rohan"]}
#    third_course_dictionary = {"name": "Economics","course_id": 36248,"students": ["Matthew", "Other People", "Corey", "Nick Swift"]}
##In this line of code we are essentially inserting another document into our collection
#    subject_courses.insert_one(second_course_dictionary)
#    subject_courses.insert_one(third_course_dictionary)
#    pet_route()

if __name__ == '__main__':

#creae a document "course_dic" which is a dictionary
    app.run()
#course_dictionary = {"subject": "Science","course_id": 38428,"students": ["Matthew","Shannon Dougherty", "Corey", "Steven Spielberg"]}
    course_dict = {"subject": "Math","course_id": 12343,"students":["yves","matthew","Chris","Charmelle","Laurel"]}
# Making a Connection with MongoClient
#client = MongoClient(mongodb://localhost:27017/)
#client = MongoClient('mongodb://localhost:27017/')

#create a database
    database = client["courses"]

# create a "subject" collection into the database
    subject = database.subject
    subject.drop()

# Add doccument "course_dic" in the collection "Subject"
    subject.insert_one(course_dict)

    course_dict2 = {"subject": " English","course_id": 23243,"students":["Akash","Kashi","James"]}
    course_dict3 = {"subject": "History","course_id":32432,"student":["Mondale","ferdinand","Anabel"]}
    subject.insert_one(course_dict2)
    subject.insert_one(course_dict3)

    data = get_course_by_subject()
    print (data)

#FETCHING DOCUMENT FROM COLLECTION
@app.route('/courses', methond = [GET])
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






































