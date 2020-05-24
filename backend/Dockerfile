# ubuntu image 
FROM ubuntu:bionic

# install python & pip
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip python3-dev libpq-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && pip3 install --upgrade pip

# no interactive gui when installing packages
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common

# suppress some spaCy warning error logging
ENV SPACY_WARNING_IGNORE=W008

RUN mkdir -p /app
WORKDIR /app
ADD . /app

# install pip libraries/dependencies
RUN pip3 install -r requirements.txt
RUN pip uninstall psycopg2
RUN pip install --no-binary :all: psycopg2

# install spacy nlp library - sm for small library, if we need vectors install en_core_web_lg and change in nlp.py
RUN python3 -m spacy download en_core_web_sm

# run the app through uwsgi server and go through app.ini settings
CMD [ "uwsgi", "app.ini" ]