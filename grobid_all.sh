#!/bin/bash

set -euo pipefail
# source ./variables.sh

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


pdf_to_txt(){
    echo "pipenv run python full_text_extract.py --pdf-file $1 --output $1.out"
    # pipenv run python full_text_extract.py --pdf-file $1 --output $1.out

}


DOCKER_PRESENT=$(which docker)
if [ -z "$DOCKER_PRESENT" ]; then
  echo "Docker is not installed. Please follow instructions in README.grobid.md to install Docker first."
  exit 1
fi


echo "Starting grobid..."
start_grobid

echo "start convert pdfs to txt"
for f in $(find ./ -name '*.pdf'); do
    pdf_to_txt $f; 
done

echo "Stopping grobid..."
stop_grobid

