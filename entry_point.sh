#!/bin/bash
#
# IMPORTANT: Change this file only in directory Standalone!

source /opt/bin/functions.sh

export GEOMETRY="$SCREEN_WIDTH""x""$SCREEN_HEIGHT""x""$SCREEN_DEPTH"

function shutdown {
  kill -s SIGTERM $NODE_PID
  wait $NODE_PID
}

if [ ! -z "$SE_OPTS" ]; then
  echo "appending selenium options: ${SE_OPTS}"
fi

SERVERNUM=$(get_server_num)

rm -f /tmp/.X*lock

xvfb-run -n $SERVERNUM --server-args="-screen 0 $GEOMETRY -ac +extension RANDR" \
  java ${JAVA_OPTS} -jar /opt/selenium/selenium-server-standalone.jar \
  ${SE_OPTS} &
NODE_PID=$!

while ! nc -z localhost 4444; do   
  sleep 0.1 # wait for 1/10 of the second before check again
done
echo "******************selelenium started*****************"
python /usr/src/app/bot.py

trap shutdown SIGTERM SIGINT
wait $NODE_PID

