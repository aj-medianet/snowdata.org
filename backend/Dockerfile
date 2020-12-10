# ubuntu image 
FROM ubuntu:bionic

# install python & pip
 RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip python3-dev libpq-dev && cd /usr/local/bin && ln -s /usr/bin/python3 python && pip3 install --upgrade pip

# install geckodriver
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb


RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

# install firefox
RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    apt-get purge firefox && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP

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

# install selenium
RUN pip3 install selenium

# install spacy nlp library - sm for small library, if we need vectors install en_core_web_lg and change in nlp.py
RUN python3 -m spacy download en_core_web_sm

# run the app through uwsgi server and go through app.ini settings
CMD [ "uwsgi", "app.ini" ]