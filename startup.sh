#!/bin/bash
#if [ "$PRODUCTION" = true ]; then
#source .env
gunicorn bin.start_app:start_app -t 0 -w 1 -k uvicorn.workers.UvicornWorker -b $HOST:$PORT --threads 8 --log-level debug --forwarded-allow-ips="*"
#else
#python -m debugpy --wait-for-client --listen $HOST:5678 -m uvicorn --factory bin.start_app:start_app --reload --host $HOST --port $PORT --lifespan on --log-level debug --forwarded-allow-ips '*' --workers 1
#fi