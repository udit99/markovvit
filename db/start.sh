#!/bin/sh

# Run the PG container, with a database named 'users' and credentials
# for a users-service user which can access it.
echo "Starting DB..."  
docker run --name pg-db  -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
alembic upgrade head

