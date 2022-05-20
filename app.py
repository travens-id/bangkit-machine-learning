import os
from flask import Flask, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import sys
sys.path.append("..")

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['DOWNLOAD_FOLDER'] = 'downloads/'

LABEL_FILENAME = 'labels/label_map.pbtxt'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

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
    data = request.get_json()
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Uploaded!"


@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Endpoint not found', 'status_code': 404})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')