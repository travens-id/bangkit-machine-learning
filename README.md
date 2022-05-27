# bangkit-machine-learning

The source code of machine learning model's API of Travens smart guide in order to complete Bangkit Capstone Project

| Endpoint |   Method   | Body Sent (JSON) |              Description              |
| :------: | :--------: | :--------------: | :-----------------------------------: |
|     /    |     GET    |       None       |   HTTP GET REQUEST Testing Endpoint   |
|   /post  |    POST    |     Anything     |   HTTP POST REQUEST Testing Endpoint  |
|   /404   | GET & POST |     Anything     |         404 NOT FOUND Endpoint        |
| /predict |    POST    | file: Image file | HTTP POST REQUEST Prediction Endpoint |

# How to run this Flask app
- Clone this repo
- Open terminal and go to this project's root directory
- Type `python -m venv .venv` and hit enter
- In Linux, type `source .venv/bin/activate`
- In Windows, type `.venv\Scripts\activate`
- Type `pip install -r requirements.txt`
- Serve the Flask app by typing `flask run`
- It will run on `http://127.0.0.1:5000`

# How to predict image with Postman
- Open Postman
- Enter URL request bar with `http://127.0.0.1:5000/predict`
- Select method POST
- Go to Body tab and select form-data
- Change key from form-data with file (it must be named 'file')
- Input the image that you want predict as a value of the key
- Send the request

![Landmark_Detection (1)](https://user-images.githubusercontent.com/86970816/170767622-24a48a85-b69c-40a3-93d4-510929cf357b.png)
