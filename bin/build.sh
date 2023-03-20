#! /bin/bash
# Build a docker image
cd ..
docker build -t pyengine/google-logging .
docker tag pyengine/google-logging pyengine/google-logging:1.0
docker tag pyengine/google-logging spaceone/google-logging:1.0
