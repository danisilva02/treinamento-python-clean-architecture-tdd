#!/bin/bash

# Atualizar e instalar pacotes necessários
sudo yum update -y
sudo yum install curl -y

# Instalar Docker
sudo yum install -y docker

# Iniciar o Docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# Aguarde o Docker iniciar
while ! sudo systemctl is-active --quiet docker; do
  sleep 1
done

# Adicionar usuário ao grupo Docker
sudo usermod -a -G docker ec2-user

# Instalar Docker Compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Faça login no ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ecr_image_uri}

# Puxe a imagem
docker pull ${ecr_image_uri}:latest

# Execute o container
docker run --platform linux/arm64 -d -p ${app_port} \
    ${env_vars} \
    ${ecr_image_uri}:latest
