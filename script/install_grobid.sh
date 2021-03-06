#! /bin/bash
source ./variables.sh

PIPENV_PRESENT=$(which pipenv)
OSX=$(which brew)
if [ -z "$PIPENV_PRESENT" ]; then
  if [ -z "$OSX" ]; then
    brew install pipenv
  else
    PIP=$(which pip)
    if [ ! -z "$PIP" ]; then
      sudo pip3 install pipenv
    else
      echo "Cannot install pipenv. No suitable brew or pip environment found.";
      exit -1
    fi
  fi
fi

DOCKER_PRESENT=$(which docker)
if [ ! -z "$DOCKER_PRESENT" ]
then
  docker pull $IMAGE_ID:$IMAGE_VERSION
else
  echo "No docker installation present. Please install Docker before continuing"
fi

# install dependencies
pipenv install lxml bs4 requests
