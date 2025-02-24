#!/bin/bash

SERVICE_NAME="flask_app"
PID_FILE="flask_app.pid"

start_service() {
    if [ -f "$PID_FILE" ]; then
        echo "Service is already running."
    else
        echo "Starting service..."
        nohup python app.py > flask_app.log 2>&1 &
        echo $! > "$PID_FILE"
        echo "Service started with PID $(cat $PID_FILE)."
    fi
}

status_service() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p $PID > /dev/null; then
            echo "Service is running with PID $PID."
        else
            echo "Service is not running, but PID file exists."
        fi
    else
        echo "Service is not running."
    fi
}

stop_service() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        echo "Stopping service with PID $PID..."
        kill $PID
        rm "$PID_FILE"
        echo "Service stopped."
    else
        echo "Service is not running."
    fi
}

case "$1" in
    start)
        start_service
        ;;
    status)
        status_service
        ;;
    stop)
        stop_service
        ;;
    *)
        echo "Usage: $0 {start|status|stop}"
        exit 1
        ;;
esac