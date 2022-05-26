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


![Museum Sejarah Jakarta](https://user-images.githubusercontent.com/89571899/170517926-08c64baa-6dff-4e24-8e68-bdda09dfa997.jpeg)
![Garuda Wisnu Kencana](https://user-images.githubusercontent.com/89571899/170517941-8e95a071-8849-4eb9-8707-47f5cdf9bde3.jpeg)
![Pagoda Watu Gong](https://user-images.githubusercontent.com/89571899/170517932-d9ee25eb-2b27-4c8a-9af9-d5c7346a5078.jpeg)
![Tugu Yogyakarta](https://user-images.githubusercontent.com/89571899/170517937-9578268c-96bf-443c-a6ad-54d0ddb6585d.jpeg)

