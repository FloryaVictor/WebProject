source ../conf.sh

docker exec -t $DB_DOCKER_CONTAINER pg_dumpall -c -U $DB_USER > backups/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql