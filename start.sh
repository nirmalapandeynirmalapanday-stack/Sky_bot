#!/bin/bash
pulseaudio --start \
    --daemonize=no \
    --log-target=stderr \
    --exit-idle-time=-1 \
    --disable-shm=true &
sleep 3
python main.py
