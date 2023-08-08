#!/bin/bash

# Read the API key from the file downloaded in the IBM Cloud

FILEAPIKEY=wkcapikey.json
apikey=$(jq -r .apikey $FILEAPIKEY)

# Get a bearer token with the API key

url="https://iam.cloud.ibm.com/identity/token"
header=" -H Content-Type: application/x-www-form-urlencoded "
flags=" -s -X POST"
data=" -d grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey="
data=${data}${apikey}

token=$( \
    curl $flags $url $header $data \
    | jq -r .access_token)

# Create Category

url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/categories"
flags=' -s -X POST'
header='-H content-type:application/json' 
data='{"name":"MotoGP"}'

category_id=$(curl $flags $url $header \
   -H "Authorization:Bearer ${token}" \
   -d $data \
   | jq -r '.resources[0].artifact_id')

echo MotoGP Category created with id=$category_id


