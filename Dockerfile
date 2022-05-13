FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install protobuf-compiler

RUN protoc object_detection/protos/*.proto --python_out=.

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "app.py"]
