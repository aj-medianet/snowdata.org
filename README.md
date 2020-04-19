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

Install the node modules in the dev build after you've installed node and npm
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

The frontend is running on 
http://localhost:8083


The backend is running on 
http://localhost:7072


### Manually load database
Login to MySQL docker container
```
docker ps
```
```
docker exec -it <container ID> /bin/bash
```

Load the init.sql schema into the snow_db database
```
mysql -u root -p snow_db < init.sql
```
Password = root


### Deployment 

TODO

## Built With

### Frameworks 

* [React](https://reactjs.org/) - Frontend
* [Flask](https://flask.palletsprojects.com/) - Backend
* [MySQL](https://www.mysql.com/) - Database

### Docker Images:

* [Node](https://hub.docker.com/_/node/) - Frontend
* [Ubuntu](https://hub.docker.com/_/ubuntu) - Backend
* [Nginx](https://hub.docker.com/_/nginx) - Reverse Proxy Server

### Dependencies

* [Frontend npm installs](frontend/package.json)
* [Backend pip installs](backend/requirements.txt)
* [Frontend Docker Image](/frontend/Dockerfile)
* [Backend Docker Image](/backend/Dockerfile)
* [Nginx Docker Image](/nginx/Dockerfile)

### End to End App Workflow

![App Architecture](app-arch.png)
![Backend Architecture](backend-arch.png)

## Authors

* **Andrew Joseph** 
* **Rustin Winger** 
* **Robert Pfingsten** 

## License

This project is released under the MIT License - see the [license.md](license.md) file for details

