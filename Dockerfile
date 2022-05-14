FROM python:3.10

WORKDIR /bangkit-machine-learning

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]