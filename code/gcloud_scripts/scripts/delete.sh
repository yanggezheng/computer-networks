#!/bin/bash

# Delete all resources. Deployment manager will not empty a bucket. That must be done manually.
# ulysses.butler@nyu.edu

PROJECT=$(gcloud config get project 2>/dev/null)
gcloud storage rm -r gs://$PROJECT/*

gcloud deployment-manager deployments delete nyu-networking-course
