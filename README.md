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

To run the backend you will need to create a file called 'credentials.py' in the backend root directory. 

This file will need to configure the DB to match the credentials in the docker-compose.yml file. You need to include:
- db_user
- db_password
- db_host
- db_port
- db_name

You also need to include a number for the API call limit:
- api_limit

As well as gmail credentials that line up with the utils.py send_email function:
- email_password

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

Since this project is open sourced we have kept the production docker-compose build hidden. However, you can see the build command in the Makefile and frontend prod.Dockerfile Steps to recreate a similar production build include:
- Create prod-docker-compose.yml
- Setup your db credentials in the prod docker-compoe file and then create a credentials.py file like in the dev build
- Point the frontend build to the prod.Dockerfile and link the ports correctly
- remove all volumes except the DB, because you want the DB data to persist between builds
- Setup NGINX on your server to route traffic to the frontend and backend ports exposed

## Continuous Integration

Using Github actions to build and run the app using our makefile. Configuration can be viewed at:

* [Push Workflow](.github/workflows/push.yml)

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

