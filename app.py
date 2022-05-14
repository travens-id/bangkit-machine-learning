from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    hello_json = {
        'status_code': 200,
        'message': 'Success testing the API!',
        'data': [],
    }
    return jsonify(hello_json)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify(data)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found', 'status_code': 404})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')