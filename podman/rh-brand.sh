#!/bin/bash

CMD=$1

if [ -z "${CMD}" ] || [ "${CMD}" == "start" ]; then
    podman run --rm -d --net=host --name=rh-brand-api quay.io/eformat/rh-brand-api:latest
    podman run --rm -d --net=host --name=rh-brand-ui quay.io/eformat/rh-brand-ui:latest
    podman run --rm -d --net=host --name=rh-brand-model --device nvidia.com/gpu=0 --security-opt label=type:nvidia_container_t -e INDEX_NAME=brand -e INDEX_ROOT=/opt/app-root/src -e PORT=8081 quay.io/eformat/rh-brand-model:latest
    echo; echo ">>> Browse to http://localhost:3000"
fi

if [ "${CMD}" == "stop" ]; then
    podman stop rh-brand-api
    podman stop rh-brand-ui
    podman stop rh-brand-model
    echo; echo ">>> stopped rh-brand apps"
fi
