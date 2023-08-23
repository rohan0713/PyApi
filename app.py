from flask import Flask, jsonify, request
from mConnection import client
import json

app = Flask(__name__)

@app.route('/')
def showProfile():
    result = {
        "name" : "rohan",
        "status" : "ok"
    }
    return jsonify(result)

@app.route('/meals', methods=['GET'])
def showMeals():

    dbs = client.Meals
    collection = dbs.lunch
    documents = collection.find()
    return json.dumps([meal for meal in documents], default=str)

@app.route('/users', methods=['GET'])
def showUsers():
    dbs = client.myApp
    collection = dbs.users
    documents = collection.find()
    return json.dumps([users for users in documents], default=str)

@app.route('/user/new', methods=['POST'])
def createUser():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if(content_type == 'application/json'):
        json = request.json
        
        dbs = client.myApp
        collection = dbs.users

        print(json['username'])
        print(json['email'])
        print(json['password'])
        print(json['status'])

        user = {
            "username": json['username'],
            "email": json['email'],
            "password": json['password'],
            "status": json['status']
        }

        collection.insert_one(user)

        return json
    else:
        return 'Content-Type not supported'    

@app.route('/user/update/<string:username>', methods=['POST', 'PUT'])
def updateUser(username):

    dbs = client.myApp
    collection = dbs.users

    myQuery = {"username": username}
    newValues = {"$set": {"status": 1, "password": "harry"}}

    response = collection.update_many(myQuery, newValues)
    if response.matched_count == 0:
        return "No user found"
    else:
        return "Profile updated successfully"

@app.route('/user/delete/<string:username>/<string:password>', methods=['DELETE'])
def deleteUser(username, password):

    dbs = client.myApp
    collection = dbs.users

    myQuery = {'username': username, 'password': password}
    response = collection.delete_many(myQuery)

    if response.deleted_count == 0:
        return "No data matched", 404
    else:
        return "User deleted successfully"

@app.route('/user/data/<string:email>/<string:newEmail>', methods=['PATCH'])
def updateData(email, newEmail):

    dbs = client.myApp
    collection = dbs.users

    myQuery = {'email': email}
    newValues = {'$set': {'email': newEmail}}

    response = collection.update_one(myQuery, newValues)
    if response.matched_count == 0:
        return 'No data found', 404
    else:
        return 'Email updated successfully'

@app.route('/api/headers', methods=['HEAD'])
def showHeaders():
    headers = {'Content-Type': 'application/json'}
    return 'Check headers', 200, headers

@app.route('/users/methods', methods=['OPTIONS'])
def callOptions():

    options = {'Alow': 'GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS'}
    return 'Check Headers', 200, options

if __name__ == "__main__":
    app.run(debug=True)
