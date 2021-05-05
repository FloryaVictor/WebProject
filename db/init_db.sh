#!/bin/bash

for name in $(docker ps -a --format "{{.Names}}")
do
  if [ "$name" == "$DB_DOCKER_CONTAINER" ]
  then
    docker container rm $DB_DOCKER_CONTAINER
    break
  fi
done;

for name in $(docker images --format "{{.Repository}}")
do
  if [ "$name" == "$DB_DOCKER_IMG" ]
  then
    docker image rm $DB_DOCKER_IMG
    break
  fi
done;

docker build -t "$DB_DOCKER_IMG" .