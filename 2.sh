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


# With the bearer token, we can issue requests 

echo "---- Export all as ZIP file----"

url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/export?include_custom_attribute_definitions=true"

flags=" -s -X GET"
header="-H content-type: application/json"  
curl $flags $url $header \
   -H "Authorization: Bearer ${token}" \
   -o governance_artifacts.zip

echo "---- Export only the business terms to CSV----"

url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/glossary_term/export"

curl $flags $url $header \
   -H "Authorization: Bearer ${token}" \
   -o business_terms.csv

echo "---- Import business terms from CSV----"

flags=' -X POST '
url=' https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/glossary_term/import?merge_option=all '
header=' -H Content-Type:multipart/form-data '

curl $flags $url $header \
   -H "Authorization:Bearer ${token}" \
   -F "file=@\"mybusiness_terms.csv\";type=text/csv" 

echo "---- Import all artifact from a ZIP File ----"

flags=' -s -X POST '
url=' https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/import?merge_option=specified '
header=' -H Content-Type:multipart/form-data '
import_process=$(curl $flags $url $header \
   -H "Authorization:Bearer ${token}" \
   -F "file=@\"governance_artifacts.zip\""  \
   | jq -r .process_id)

echo "----- Import process started: $import_process ----- "

flags=' -s -X GET '
url=" https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/import/status/${import_process} "

while true
do
    import_status=$(curl $flags $url \
    -H "Authorization: Bearer ${token}" \
    | jq -r .status)


    if [ $import_status != "IN_PROGRESS" ]
    then
        break
    fi
    
    echo Import job in process. Please wait...
    sleep 5
done

curl $flags $url \
    -H "Authorization: Bearer ${token}"









