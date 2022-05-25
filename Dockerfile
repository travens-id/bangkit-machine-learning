FROM python:3.10

WORKDIR /bangkit-machine-learning

COPY . .

RUN apt-get update

RUN apt-get install protobuf-compiler

RUN protoc object_detection/protos/*.proto --python_out=. 

RUN cp object_detection/packages/tf2/setup.py . 

RUN python -m pip install . 

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]