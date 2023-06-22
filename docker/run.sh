#!/bin/bash

pushd /opt/fastapi_docker_helloworld/fastapi_docker_helloworld
exec uvicorn app:app --host 0.0.0.0 --port 8282 