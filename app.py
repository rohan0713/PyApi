from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def showProfile():
    result = {
        "name" : "rohan",
        "status" : "ok"
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
