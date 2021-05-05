docker container run -d --name=$DB_DOCKER_CONTAINER -p $DB_PORT:5432 -e PGDATA=/pgdata $DB_DOCKER_IMG
