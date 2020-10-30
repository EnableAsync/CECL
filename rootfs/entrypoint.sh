#!/bin/bash

case_opt=$1

case ${case_opt} in
server)
    exec python /CECL/server/main.py
    ;;
data)
    exec python /CECL/data_manger/data_manger_server.py
    ;;
message)
    exec python /CECL/message_hub/message_hub_server.py
    ;;
controller)
    exec python /CECL/task_controller/task_controller_server.py
    ;;
runtime)
    exec python /CECL/task_runtime/task_runtime_server.py
    ;;
deploy_controller)
    python /CECL/task_controller/deploy_controller_server.py
    ;;
deploy_runtime)
    exec python /CECL/task_runtime/deploy_runtime_server.py
    ;;
esac

exec "$@"

