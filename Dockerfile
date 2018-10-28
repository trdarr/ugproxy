from python:3.7-alpine

expose 8000
workdir /app

run mkdir -p /app/ugproxy
copy ugproxy ./ugproxy
copy run.py .
cmd python run.py
