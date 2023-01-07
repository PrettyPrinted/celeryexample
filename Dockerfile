FROM python:latest

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apt-get update && apt-get install -y build-essentials

COPY requirements.txt requirements.txt 
RUN pip install flask celery redis flask-sqlalchemy flask-wtf

WORKDIR /app