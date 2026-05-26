#!/bin/bash

apt update -y
apt install docker.io docker-compose git -y

docker compose up -d --build

echo "ISP SYSTEM LIVE"
