# Pub-Sub-Distributed-System-Using-Docker

Publish/Subscribe (or pub/sub for short) is a popular **indirect** communication system. `Pub/sub` systems disseminates events to multiple recipients (called subscribers) through an intermediary. Examples of successful pub/sub include `Twitter` and `Bloomberg terminal`-like financial systems. In this project, we will emulate a pub/sub system using `Docker` which is a computer program that performs operating-system-level virtualization, also known as "containerization".

# How to start with docker

You will need to at first install **docker** if you do not have it already.

```
$ sudo snap install docker
$ sudo snap services
$ sudo snap start docker

```
If you do not want to type sudo everytime you give a command in docker, please continue with the following commands.

```
$ whoami
$ sudo groupadd docker
$ sudo usermod -aG docker $USER

```
Now restart your OS. Start a terminal again.

```
$ docker --version   #checking if docker is installed perfectly
$ docker run hello-world # download an official image "hello-world" from docker hub and run it in a container

```

# How to run phase-01 (simple flask app and MyWayPoints django app)

###  Simple flask app

First go the `phase-01/Simple_Flask_App` directory. Then run the below commands:

```
docker build -t simple-flask-app .  # create a new image named "simple-flask-app" using the dockerfile in that directory
docker run -d -p 50:5000 --name flask-container simple-flask-app   # running the image in a new container named "flask-container"
```
Now, go to the url `127.0.0.1:50` to see the output of the app from docker. Here `50:5000` is port mapping from container to host where 50 is the port of host.


###  MyWayPoints django app

First go the `phase-01/MyWayPoints_v1` directory. Then run the below commands:

```
docker build -t simple-django-app .  # create a new image named "simple-django-app" using the dockerfile in that directory
docker run -d -p 80:8000 --name django-container simple-django-app   # running the image in a new container named "django-container"
```
Now, go to the url `127.0.0.1:80/map` to see the output of the app from docker. 



[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Pub-Sub-Distributed-System-Using-Docker/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
