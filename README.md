# Snowdata.org

### Prerequisites

You need to have docker and docker-compose installed on your machine. 

```
https://docs.docker.com/install/
```
```
https://docs.docker.com/compose/install/
```

## Deployment and Development 

### For development 

Install the node modules in the dev build
```
cd frontend && npm install && cd ..
```

Build and run the docker containers in detached mode:
```
make br
```

Build the docker containers:
```
make build
```

Run the app detached without building:
```
make rund
```

Run the app in the shell:
```
make run
```

To kill the app:

```
docker-compose down
```

### Manually load database
Login to MySQL docker container
```
docker ps
```
```
docker exec -it <container ID> /bin/bash
```
```
mysql -u root -p snow_db < init.sql
```
Password = root



### Deployment TODO

## Built With

### Web Frameworks 

* [React](https://reactjs.org/) - Frontend
* [Flask](https://flask.palletsprojects.com/) - Backend

### Docker Images:

* [Node](https://hub.docker.com/_/node/) - Frontend
* [Python](https://hub.docker.com/_/python) - Backend
* [Nginx](https://hub.docker.com/_/nginx) - Reverse Proxy Server

### Dependencies

* [Frontend npm installs](frontend/package.json)
* [Backend pip installs](backend/requirements.txt)
* [Frontend Docker Image](/frontend/Dockerfile)
* [Backend Docker Image](/backend/Dockerfile)
* [Nginx Docker Image](/nginx/Dockerfile)

### End to End App Workflow

TODO

![App Architecture](app-arch.png)
![Backend Architecture](backend-arch.png)

## Authors

* **Andrew Joseph** 
* **Rustin Winger** 
* **Robert Pfingsten** 

## License

This project is released under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

