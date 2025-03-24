#!/bin/bash
# Assign the first input argument to the BB_TOKEN variable
BB_TOKEN=$1
# Assign the second input argument to the BB_REPO variable
BB_REPO=$2
# Assign the third input argument to the BB_STATE variable
BB_STATE=$3
# Assign the third input argument to the TRIGGER_URL variable
TRIGGER_URL=$4
# Obtain the current commit hash using git rev-parse command
BB_COMMIT=$(git rev-parse --short HEAD)
# Obtain the current commit hash using git show -s --format='%ae' command
EMAIL_AUTHOR=$(git show -s --format='%ae')
# Build the location for the request to reach
# The location includes the BB_REPO and BB_COMMIT variables as part of the URL
LOCATION=https://api.bitbucket.org/2.0/repositories/elevatusdev/${BB_REPO}/commit/${BB_COMMIT}/statuses/build
# Send a request to Bitbucket API using the curl command
# The request includes:
#   - The location variable as the URL to reach
#   - Two headers:
#       - "Content-Type: application/json" to specify the request's data type
#       - "Authorization: Bearer ${BB_TOKEN}" to include the Bitbucket token for authentication
#   - A JSON data object in the request body
curl -s --location $LOCATION \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${BB_TOKEN}" \
--data "{
    \"state\": \"${BB_STATE}\",
    \"key\": \"gcp\",
    \"name\": \"Google CI/CD Pipeline for ${BB_REPO}\",
    \"url\": \"https://console.cloud.google.com/cloud-build/builds;${TRIGGER_URL}\",
    \"description\": \"Changes by ${EMAIL_AUTHOR} commit | ${BB_COMMIT}\"
}"
