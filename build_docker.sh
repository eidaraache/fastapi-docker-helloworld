#!/bin/bash
BUILD_ID=latest
DOCKER_BUILDKIT=1 docker build -t fastapi-docker-helloworld:$BUILD_ID -f docker/DockerFile .