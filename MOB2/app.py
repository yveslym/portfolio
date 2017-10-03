import json
import pdb
from flask import Flask, request

app = Flask(__name__)

@app.route('/person')
def person_route():
    pdb.set_trace()
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

#Add a new route handler that receives POST requests to the route /pets with JSON data in the body(an array of
#pet objects) and returns that JSON data unmodified in the response body. Test the /pets route using Paw, Curl,
#Postman, or another tool to make HTTP POST requests to ensure it responds correctly with the same data given
#in the request.

@app.route('/pets')
def pet_route():
    pets = [{'name': "charlie", 'color': "Brow"}, {'name': "Bingo", 'color': "Blue"}]
    json_pets = json.dumps(pets)
    return (json_pets, 200, None)
if __name__ == '__main__':
    app.run()
