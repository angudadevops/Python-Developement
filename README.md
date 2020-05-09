# Welcome to Python Web Development. [![HitCount](http://hits.dwyl.com/angudadevops/Python-Developement.svg)](http://hits.dwyl.com/angudadevops/Python-Developement)

PreRequisites:
- Docker

Python Web Application can be developed 
- [Flask](#flask-app)
- [Django](#django-app)

## flask-app
If you want to build a light weight web application, you can choose flask module. 

Run the below command to create sample flask App

```
docker run -d -p 5000:5000 anguda/python-flask-app
```

Access above container like below 
```
localhost:8080/username
```

If you want to run a flask with MySQL DB connectivity, please run the below command
```
docker-compose up
```

No docker-compose installed? Don't worry, please follow the below steps with simple docker 

Run the below simple docker commands to spin up docker containers
```
docker run -d -p 3306:3306 --name db anguda/mysql
docker run -d -p 5000:5000 --name flaskweb --link db:db anguda/python-flask-app:web
```

Are you intersted to build the docker images and explore source code, then follow the below steps.

1. First build the Docker images for both flask app and MySQL DB

Run the below command to build flask app
```
cd flask/app
docker build -t flaskweb . --no-cache
```
Run the velow command to build MySQL image
```
cd flask/db
docker build -t mysqldb . --no-cache
```
2. It's time for to run the docker containers

Run the below commands to run the applications
```
docker run -d -p 3306:3306 --name db mysqldb
docker run -d -p 5000:5000 --name flaskweb --link db:db flaskweb
```

### Using Kubernets
Are you using kubernetes as a service, then here's commands to run your application as pods

```
kubectl create -f db-deployment.yaml

kubectl create -f app-deployment.yaml
```

To get nodeport of app deployment, run the below command 

```
kubectl get svc
```

### Usage

Access the web application with below url
```
localhost:5000/
```

## django-app
Django is help to use Advanced Web Development

Run the below command to create a django simple web application

```
cd django
docker build -t mydjango . --no-cache
```

Run the below command to run the docker container

```
docker run -d -p 8000:8000 --name django mydjango
```

### Usage

Access the web application with below url
```
localhost:8000/
```
