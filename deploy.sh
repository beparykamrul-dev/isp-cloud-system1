#!/bin/bash

echo "STARTING ISP CLOUD..."

apt update -y

apt install docker.io docker-compose git -y

systemctl enable docker
systemctl start docker

docker compose up -d --build

echo "================================="
echo "ISP CLOUD SYSTEM LIVE"
echo "API: http://SERVER-IP:8000"
echo "POSTGRES: 5432"
echo "REDIS: 6379"
echo "================================="
