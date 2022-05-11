FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "app.py"]