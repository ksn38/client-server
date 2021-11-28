FROM python:latest

RUN apt-get update && apt-get install -y iputils-ping\
    net-tools

ADD server.py /server/

WORKDIR /server/
