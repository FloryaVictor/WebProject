source ../conf.sh

PWD=$(pwd)
docker container run -d --name=$DB_DOCKER_CONTAINER -p $DB_PORT:5432 -e PGDATA=/pgdata -v $PWD/pgdata:/pgdata $DB_DOCKER_IMG
