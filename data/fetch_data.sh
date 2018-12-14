#! /bin/bash

set -euo pipefail
IFS=$'\n\t'

source ./constants.sh

IP=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

echo -n "$TEAM_NAME Password: "
read -s PASSWORD
echo $PASSWORD
sshpass -p "$PASSWORD" scp -r -P $PORT $TEAM_NAME@$HADOOP_IP:$UNLABELED_DATA_PATH $(pwd)
