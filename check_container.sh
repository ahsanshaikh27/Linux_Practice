#!/bin/bash

CONTAINER_NAME="myapp"
LOGFILE="/var/log/container_check.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Check if container is running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "$DATE - $CONTAINER_NAME is running." >> $LOGFILE
else
    echo "$DATE - $CONTAINER_NAME is NOT running. Restarting..." >> $LOGFILE
    docker start $CONTAINER_NAME
fi

