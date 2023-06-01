#!/usr/bin/env bash

echo "Deploying ..."

# apply configmap
kubectl apply -f configmap.yml

# apply deployment
kubectl apply -f deployment.yml

# apply service
kubectl apply -f service.yml

# apply ingress
kubectl apply -f ingress.yml

echo "Deployed!"