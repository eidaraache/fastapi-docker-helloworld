# FastAPI-Docker-helloworld
This is a simple example on how to build a [FastAPI](https://fastapi.tiangolo.com/) application and encapsulate as a microservice using [Docker](https://www.docker.com/)

## How to run it
prerequisites:
- [Docker Engine](https://docs.docker.com/engine/install/)
The project was created and tested it with **Docker version 20.10.14**

After having all the prerequisites installed:
- Run the script **build_docker.sh** 
It will create the corresponding docker image
- Run the command **docker run --network host fastapi-docker-helloworld**
- Visit the page **http://localhost:8282/docs** and try out one of the endpoints


### Note:
The project was built using [Poetry](https://python-poetry.org/) to manage python dependencies 
