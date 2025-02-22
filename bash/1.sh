#!/bin/bash 

# Read the API key from the file downloaded in the IBM Cloud

FILEAPIKEY=ikcapikey.json
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

# With the bearer token, we can issue requests 

echo "---- Projects ----"

url="https://api.eu-de.dataplatform.cloud.ibm.com/v2/projects"
flags=" -s -X GET"
header="-H content-type: application/json"  
curl $flags $url $header \
   -H "Authorization: Bearer ${token}" | jq  '.resources[].entity.name'

echo "---- Catalogs ----"

url="https://api.eu-de.dataplatform.cloud.ibm.com/v2/catalogs"
flags=" -s -X GET"
header="-H content-type: application/json" 

# all catalogs
curl $flags $url $header \
   -H "Authorization: Bearer ${token}" | jq '.catalogs[].entity.name' 

#  my catalog by name
CATALOG_NAME="Catalog-Angel"
params="?name=${CATALOG_NAME}"

echo ---- The catalog named $CATALOG_NAME ----

curl $flags $url$params $header \
   -H "Authorization: Bearer ${token}" | jq '.catalogs[] | [ .metadata.guid , .entity.name ]'

#  my catalog by id
mycatalog_id=$(curl $flags $url$params $header \
   -H "Authorization: Bearer ${token}" | jq -r '.catalogs[] | .metadata.guid ')

echo --- The catalog with id=$mycatalog_id ----

url="https://api.eu-de.dataplatform.cloud.ibm.com/v2/catalogs/$mycatalog_id"

curl $flags $url $header \
   -H "Authorization: Bearer ${token}" | jq '.entity.name '
