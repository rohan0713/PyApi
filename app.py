from flask import Flask, jsonify
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

@app.route('/users', methods=['POST'])
def showUsers():
    dbs = client.myApp
    collection = dbs.users
    documents = collection.find()
    return json.dumps([users for users in documents], default=str)


if __name__ == "__main__":
    app.run(debug=True)
