# nodejs image
FROM node:12.6.0

ADD package.json /tmp/package.json
RUN cd /tmp && npm install && npm install -g react-scripts && npm install bootstrap
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

WORKDIR /opt/app
ADD . /opt/app

# start the react app
CMD npm start

# port needed to expose - where the prod server should point to
EXPOSE 3000