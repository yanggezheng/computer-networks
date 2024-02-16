#!/bin/bash

# Create a bucket with the project name, if it doesn't exist, then sync the contents of the ./src/ directory
# ulysses.butler@nyu.edu

SRC_DIR='./src/'
PROJECT=$(gcloud config get project 2>/dev/null)

if [ -z "$(gcloud storage buckets list 2>/dev/null | grep -w "$PROJECT")" ]; then
  echo "Bucket not found. Creating..."
  gcloud storage buckets create gs://$PROJECT/
else
  echo "Bucket found: $PROJECT"
fi

gcloud storage rsync -r --delete-unmatched-destination-objects ./src/ gs://$PROJECT/
