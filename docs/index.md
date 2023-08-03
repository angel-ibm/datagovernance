# Data Governance Workshop  

## Watson Knowledge Catalog

Welcome to the workshop

## Provision the service

??? abstract "Show me a quick clip"

    ![type:video](videos/v1.mov)

### Get Token  

!!! danger "The token will expire after one hour"

=== "Python"

    ``` py title="token.py" linenums="1" hl_lines="5 14"
    
    import json
    import requests
    
    # Read the API key from the file downloaded in the IBM Cloud
    f = open("wkcapikey.json")
    data = json.load(f)
    apikey = data["apikey"]
    
    # Get a bearer token with the API key
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=" + apikey
    
    r = requests.post(url, headers=headers, data=data)
    access_token = r.json()["access_token"]
    ``` 
=== "Bash"

    ```bash title="token.sh" linenums="1" hl_lines="5 16 17 18"
    
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
    
    ```

### Projects and Catalogs  

!!! abstract "Inspect existing artifacts"

=== "Python"

    ``` py title="projects_and_catalogs.py" linenums="1" hl_lines="8 17"
    
    
        # With the bearer token, we can issue requests 
        
        print("---- Projects ----")
        
        url = "https://api.eu-de.dataplatform.cloud.ibm.com/v2/projects"
        headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
        
        r = requests.get(url, headers=headers)
        for i in r.json()["resources"] :
            print(i["entity"]["name"])
        
        print("---- Catalogs ----")
        
        url = "https://api.eu-de.dataplatform.cloud.ibm.com/v2/catalogs"
        headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
        
        r = requests.get(url, headers=headers)
        for i in r.json()["catalogs"] :
            print(i["entity"]["name"])
    ``` 
=== "Bash"

    ```bash title="projects_and_catalogs.sh" linenums="1" hl_lines="8 9 18 19"
    
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
    ```

### One specific item  

!!! tip "Get only one artifact"  

=== "Python"

    ``` py title="only_one_item.py" linenums="1" hl_lines="2 5 11 14"
    
            print("---- The catalog called Catalog-Angel ----")
            mycatalog="Catalog-Angel"
            url="https://api.eu-de.dataplatform.cloud.ibm.com/v2/catalogs?name=" + mycatalog
            
            r = requests.get(url, headers=headers)
            for i in r.json()["catalogs"] :
                print(i["metadata"]["guid"])
                print(i["entity"]["name"])
            
            mycatalog_id = i["metadata"]["guid"] 
            print(f"---- The catalog with id = {mycatalog_id}  ----")
            
            url="https://api.eu-de.dataplatform.cloud.ibm.com/v2/catalogs/" + mycatalog_id
            r = requests.get(url, headers=headers)
            print(r.json()["entity"]["name"])
    ``` 
=== "Bash"

    ```bash title="only_one_item.sh" linenums="1" hl_lines="8 9 18 19"
        
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
    ```

### Everything together  

!!! example "Retrieve specfic assets"

=== "Python"

    ``` py title="projects_and_catalogs.py" linenums="1" hl_lines="23-29 38-56"
    
            
            import json
            import requests
            
            # Read the API key from the file downloaded in the IBM Cloud
            f = open("wkcapikey.json")
            data = json.load(f)
            apikey = data["apikey"]
            
            # Get a bearer token with the API key
            url = "https://iam.cloud.ibm.com/identity/token"
            headers = {"Content-Type" : "application/x-www-form-urlencoded"}
            data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=" + apikey
            
            r = requests.post(url, headers=headers, data=data)
            access_token = r.json()["access_token"]
            
            # With the bearer token, we can issue requests 
            
            print("---- All Categories ----")
            
            url = "https://api.eu-de.dataplatform.cloud.ibm.com/v3/search"
            headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
            data = '''{
                "query": {
                    "match": {
                        "metadata.artifact_type": "category"
                    }
                }
            }'''
            
            r = requests.post(url, headers=headers, data=data)
            
            for i in r.json()["rows"] :
                print(i["metadata"]["name"])
            
            print("---- Business Terms of MotoGP ----")
            
            data='''{
                "_source":[ "metadata.name", "metadata.description"],
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match": {
                                    "metadata.artifact_type": "glossary_term"
                                }
                            },
                            {
                                "match": {
                                    "categories.primary_category_name": "MotoGP"
                                }
                            }
                        ]
                    }
                }
            }'''
            
            r = requests.post(url, headers=headers, data=data)
            for i in r.json()["rows"] :
                print(i["metadata"]["name"], end=": ")
                print(i["metadata"]["description"], end="\n\n")

    ```

### Export Artifacts

!!! abstract "Store all artifacts in a zip file"

=== "Bash"

    ```bash title="export_all.sh" linenums="1" hl_lines="9"
        echo "---- Export ----"
        
        
        url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/export?include_custom_attribute_definitions=true"
        flags=" -s -X GET"
        header="-H content-type: application/json"  
        curl $flags $url $header \
           -H "Authorization: Bearer ${token}" \
           -o governance_artifacts.zip

    ```

!!! tip "Change this to export only the business terms in a csv file"

=== "Bash"

    ```bash title="export.sh" linenums="1" hl_lines="7"
        echo "---- Export only the business terms to CSV----"
        
        url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/glossary_term/export"
        
        curl $flags $url $header \
           -H "Authorization: Bearer ${token}" \
           -o business_terms.csv

    ```

### Import Artifacts

!!! abstract "Import Business Terms"

=== "Bash"

    ```bash title="import_business_terms.sh" linenums="1" hl_lines="9"

        echo "---- Import business terms from CSV----"
        
        flags=' -X POST '
        url=' https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/glossary_term/import?merge_option=all '
        header=' -H Content-Type:multipart/form-data '
        
        curl $flags $url $header \
           -H "Authorization:Bearer ${token}" \
           -F "file=@\"mybusiness_terms.csv\";type=text/csv"

    ```

!!! abstract "Import all governance artifacts from a ZIP file"

=== "Bash"

    ```bash title="import_all.sh" linenums="1" hl_lines="8"
        
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


    ```
