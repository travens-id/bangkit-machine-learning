from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    hello_json = {
        "status_code": 200,
        "message": "Success testing the API!",
        "data": [],
    }
    return jsonify(hello_json)

if __name__ == '__main__':
    app.run()