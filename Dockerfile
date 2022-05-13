FROM python:3.10.3-slim-buster

WORKDIR /bangkit-machine-learning

ADD . /bangkit-machine-learning

RUN apt-get update

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
