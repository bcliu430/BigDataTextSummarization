#! /bin/bash

source ./variables.sh

start_grobid() {
  # Update image if needed
  docker pull $IMAGE_ID:$IMAGE_VERSION

  IS_RUNNING=$(docker ps -a | grep $CONTAINER_NAME)
  if [[ ! -z "$IS_RUNNING" ]]; then
    stop_grobid
  fi

  # Start grobid in the background
  docker run -d -t --rm --init --name $CONTAINER_NAME -p 8080:8070 -p 8081:8071 lfoppiano/grobid:0.5.1
}

stop_grobid() {
  docker stop $CONTAINER_NAME
}

DOCKER_PRESENT=$(which docker)
if [ -z "$DOCKER_PRESENT" ]; then
  echo "Docker is not installed. Please follow instructions in README.grobid.md to install Docker first."
  exit 1
fi

if [[ "$#" -ne 1 ]]; then
  echo "Run the program as ./grobid.sh start|stop"
  exit 2
fi

if [[ "$1" == "start" ]]; then
  echo "Starting grobid..."
  start_grobid
elif [[ "$1" == "stop" ]]; then
  echo "Stopping grobid..."
  stop_grobid
else
  echo "Invalid argument"
fi
