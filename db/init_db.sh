#!/bin/bash


for name in $(docker images --format "{{.Repository}}")
do
  if [ "$name" == "$DB_DOCKER_IMG" ]
  then
    docker image rm $DB_DOCKER_IMG
    break
  fi
done;

docker build -t $DB_DOCKER_IMG .

PWD=$(pwd)
docker container run --rm -d --name=$DB_DOCKER_CONTAINER -p $DB_PORT:5432 -e PGDATA=/pgdata -v $PWD/pgdata:/pgdata $DB_DOCKER_IMG
