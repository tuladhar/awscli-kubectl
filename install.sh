#!/bin/sh

echo "-> Installing curl..."
apk --no-cache add curl

echo "-> Installing kubectl..."
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl

echo "-> Installing awscli..."
pip install awscli