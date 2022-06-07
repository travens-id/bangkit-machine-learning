# bangkit-machine-learning

The source code of machine learning model's API of Travens smart guide in order to complete Bangkit Capstone Project

![Landmark_Detection (1)](https://user-images.githubusercontent.com/86970816/170767622-24a48a85-b69c-40a3-93d4-510929cf357b.png)

# Model Building's Notebook
[Landmark Detection Notebook](https://colab.research.google.com/drive/1OEpz5uGPAbT-JtkYdCEv4If7UHgA_sF6?usp=sharing)

# API URL
[Flask API](https://travens-api.my.id/)

# Dataset Resources
- [Google Landmarks Dataset V2](https://storage.googleapis.com/gld-v2/web/index.html)
- [Traveloka](https://www.traveloka.com/id-id/explore/destination/famous-landmarks-in-indonesia-acc/28709)
- [Google Images](https://images.google.com/)
- [Wikipedia](https://id.wikipedia.org/wiki/Halaman_Utama)

# Detection Labels
[Label Map](https://github.com/travens-id/bangkit-machine-learning/blob/main/labels/label_map.pbtxt)

# API Endpoint
| Endpoint |   Method   | Body Sent (JSON) |              Description              |
| :------: | :--------: | :--------------: | :-----------------------------------: |
|     /    |     GET    |       None       |   HTTP GET REQUEST Testing Endpoint   |
|   /post  |    POST    |     Anything     |   HTTP POST REQUEST Testing Endpoint  |
|   /404   | GET & POST |     Anything     |         404 NOT FOUND Endpoint        |
| /predict |    POST    | file: Image file | HTTP POST REQUEST Prediction Endpoint |

# Algorithm of Machine Learning Service
![Travens Machine Learning-Page-1 drawio](https://user-images.githubusercontent.com/89571899/172442140-295be373-0687-4a76-90ec-59073aee4a66.png)

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
- Change key from form-data with file (it must be named `file`)
- Input the image that you want predict as a value of the key
- Send the request

## Architecture of SSD MobileNet V2 for Landmark Detection
![SSD_MobileNetV2](https://user-images.githubusercontent.com/86970816/171426257-99783098-4b49-48fe-b45c-99c8949738e9.png)

# References
- Cao B, Araujo A, Sim J. Unifying Deep Local and Global Features for Image Search. 2020. [Arxiv](https://arxiv.org/abs/2001.05027)
- Weyand T, Araujo A, Cao B, Sim J. Google Landmarks Dataset v2-A Large-Scale Benchmark for Instance-Level Recognition and Retrieval. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020. [Arxiv](https://arxiv.org/abs/2004.01804)
- A Howard, A Zhmoginov, LC Chen, M Sandler, M Zhu. MobileNetV2: Inverted Residuals and Linear Bottlenecks. The IEEE Conference on Computer Vision and Pattern Recognition. 2018. [Arxiv](https://arxiv.org/abs/1801.04381)
- Collection of models for landmark recognition [TensorFlow Hub](https://tfhub.dev/google/collections/landmarks)
