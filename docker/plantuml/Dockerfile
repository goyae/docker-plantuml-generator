FROM python:3.9.1-buster
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
COPY plantuml /usr/bin/
COPY plantuml.py /code/
WORKDIR /app
RUN set -x &&\
	pip install -r requirements.txt

RUN apt-get update &&\
	apt-get install default-jdk -y &&\
	apt-get install graphviz -y &&\
	apt-get install fonts-ipafont fonts-ipaexfont -y &&\
	wget 'https://downloads.sourceforge.net/project/plantuml/plantuml.jar?r=http%3A%2F%2Fplantuml.com%2Fstarting&ts=1538667739&use_mirror=jaist' &&\
	mv 'plantuml.jar?r=http:%2F%2Fplantuml.com%2Fstarting&ts=1538667739&use_mirror=jaist' /usr/local/bin/plantuml.jar

WORKDIR /code
