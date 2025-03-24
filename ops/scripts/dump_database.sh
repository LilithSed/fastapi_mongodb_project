#!/bin/bash
# Assign the first input argument to the DB_MAIN variable
DB_MAIN=$1
# Assign the two input argument to the DB_SRV_URI variable
DB_SRV_URI=$2

CONTAINER_NAME='BK_BACKUP_MONGODB'

mkdir "./ops/tmp/backup/${DB_MAIN}"

MAIN_DB_ARCHIVE="/app/ops/tmp/backup/${DB_MAIN}/main_db.gz"

LOGGER_DB_ARCHIVE="/app/ops/tmp/backup/${DB_MAIN}/logger.gz"

MAIN="main_db_$DB_MAIN";

LOGGER="logger_$DB_MAIN";
# dump database
docker exec ${CONTAINER_NAME} mongodump  --uri ${DB_SRV_URI} --db=${MAIN} --gzip --archive=${MAIN_DB_ARCHIVE}
docker exec ${CONTAINER_NAME} mongodump  --uri ${DB_SRV_URI} --db=${LOGGER} --gzip --archive=${LOGGER_DB_ARCHIVE}
## remove database
docker exec ${CONTAINER_NAME} mongosh "${DB_SRV_URI}" --eval "use ${MAIN};" --eval "db.dropDatabase()"
docker exec ${CONTAINER_NAME} mongosh "${DB_SRV_URI}" --eval "use ${LOGGER};" --eval "db.dropDatabase()"
