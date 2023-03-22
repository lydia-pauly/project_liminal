FROM python:3.8.6-buster

COPY requirements.txt /requirements.txt
COPY liminal /liminal

RUN pip install --upgrade pip
COPY setup.py setup.py
RUN pip install .

CMD uvicorn liminal.app.api:app --host 0.0.0.0 --port $PORT
