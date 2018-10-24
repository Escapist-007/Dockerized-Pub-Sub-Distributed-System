# Pub-Sub-Distributed-System-Using-Docker
Publish/Subscribe (or pub/sub for short) is a popular indirect communication system. Pub/sub systems disseminates events to multiple recipients (called subscribers) through an intermediary. Examples of successful pub/sub include Twitter and “Bloomberg terminal”-like financial systems. In this project, we will emulate a pub/sub system using the lite weight virtualization or container technology in Docker technology.

# How to run the project
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
$ docker run hello-world
```

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Pub-Sub-Distributed-System-Using-Docker/Lobby?source=orgpage?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
