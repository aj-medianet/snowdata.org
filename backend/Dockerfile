# ubuntu image so we can install inkscape and spacy
FROM ubuntu

# install python & pip
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip python3-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && pip3 install --upgrade pip

# no interactive gui when installing packages
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common

RUN mkdir -p /app
WORKDIR /app
ADD . /app

# install pip libraries/dependencies
RUN pip3 install -r requirements.txt

# run the app through uwsgi server and go through app.ini settings
CMD [ "uwsgi", "app.ini" ]