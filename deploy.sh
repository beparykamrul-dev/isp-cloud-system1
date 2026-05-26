#!/bin/bash

echo "STARTING ISP CLOUD..."

apt update -y

apt install docker.io docker-compose git -y

docker compose up -d --build

echo "SYSTEM LIVE"
echo "http://SERVER-IP:8000"
