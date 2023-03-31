FROM python:3.11.2-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt