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

if __name__ == "__main__":
    app.run(debug=True)
