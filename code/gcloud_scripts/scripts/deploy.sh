#!/bin/bash

# Create all the resources for our assignment using Deployment Manager.
# This is an IaC (Infrastructure as Code) service offered by Google, allowing us to create sets of resources based on pre-defined, reusable templates.
# ulysses.butler@nyu.edu

gcloud deployment-manager deployments create nyu-networking-course --config ./deploy/config.yaml
