# nodejs image
FROM node:12.6.0

WORKDIR /app
COPY . /app
RUN npm run build
RUN npm install -g serve
CMD serve -s build -p 3000