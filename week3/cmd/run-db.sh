#!/usr/bin/env bash

# Clean up potential ungraceful shutdown remaining
docker system prune -f || echo "Failed to prune docker system"
docker volume prune -f || echo "Failed to prune docker volume"

docker run --rm -it -v $PWD/init.sql:/docker-entrypoint-initdb.d/init.sql -p5432:5432 -e POSTGRES_PASSWORD=password postgres:16.0-alpine
