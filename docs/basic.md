# Basic Tasks

A graphical user interface is the way to get familiar with a vendor's data governance product line and even use it in production. For example, this is how you create a category with the GUI:

 ![type:video](videos/createcategory.mp4)

However, the use of a programatic API like the [Watson Data API](https://cloud.ibm.com/apidocs/watson-data-api), which is a [REST](https://en.wikipedia.org/wiki/Overview_of_RESTful_API_Description_Languages) interface,  can be very useful in the following situations:

- Automate common tasks or even one-time activities like backups and migrations
- Interface with other tools and programs that may use the REST interface
- Perform repetitive tasks involving a considerable amount of data

In general, a REST API exposes a series of endpoints (URLs), each one intended to perform an individual task that can be customized providing the parameters prescribed in the documentation. This tutorial aims at easing the learning curve when trying to implement programs (actually, python scripts) that handle the calls to the most common methds of the Watson Data API, which involve not only to choose the right endpoint but also the expressing with the right syntax the intended parameters.

The Watson Data API does not need to be installed explictitly. Anyone having access to a running Cloud Pak for Data deployment can use it, provided that he/she has the adequate privileges and, of course, the syntax is correct.

### How to use these snippets

It is recommendable to copy the content of the snippets using the small copy icon on the top corner of the code cells. It will appear when you click on the gray zones. Then, you can paste the contents on your own files. Howeever, I also provide some the actual scripts I used for testing: they are either in the [python](https://github.com/angel-ibm/datagovernance/tree/main/python) or [bash](https://github.com/angel-ibm/datagovernance/tree/main/bash) directories of the [git](https://github.com/angel-ibm/datagovernance) repository.

### Authentication -  The Bearer Token  

Before attempting to use any of the methods of the API, we need to get authenticated by Cloud Pak for Data. We usually type our userid/password in the user interface, which is good for humans, but it is certainly not optimized for programs. That is why the Watson Data API make use of the so called "Bearer Tokens" to assert our identity every time we try to perform a task.

Obtaining a bearer token and refreshing it when it expires are **mandatory pre-requisites** for all calls. The full process is explaned [here](https://cloud.ibm.com/apidocs/watson-data-api#creating-an-iam-bearer-token)  

!!! danger "Bearer tokens issued by the IBM Cloud expire after one hour. Remember to obtain a new one regularly"

The following snippets will generate a bearer token derived from the API key

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
If you are **not** working on the IBM Cloud, the endpoint of the call may be different. Look at the Level 4 PoX Section in this documentation and review the authentication cells provided in the notebooks.

## Common Tasks

Provided that the issuer of the call has been granted with the proper rights, the following tasks can be easily performed using the API and will be exercised in this chapter (click on the REST Call to get mor information):

|REST Call    | Description                          |
| ----------- | ------------------------------------ |
| [`GET /v2/projects`](https://cloud.ibm.com/apidocs/watson-data-api#projects-list) |   List the projects available for the issuer of the call in Cloud Pak for Data |
| [`GET /v2/catalogs`](https://cloud.ibm.com/apidocs/watson-data-api#get-catalogs) |   List the catalogs available in Cloud Pak for Data. Not only the list, but the specific information of one of them can be retrieved using parameter filtering |
| [`POST /v3/search`](https://cloud.ibm.com/apidocs/watson-data-api#searching) |   Search for any piece of information by using queries in Lucene or Elasticsearch syntax |
| [`GET /v3/governance_artifact_types/export`](https://cloud.ibm.com/apidocs/watson-data-api#zipped-artifact-export) |   Export the full set of artifacts to a ZIP file |
| [`GET /v3/governance_artifact_types/{artifact_type}/export`](https://cloud.ibm.com/apidocs/watson-data-api#artifact-export) |   Export just one kind of artifacts to a CSV file. The business terms (`glossary_term`) will be shown ind this chapter |
| [`POST /v3/governance_artifact_types/import`](https://cloud.ibm.com/apidocs/watson-data-api#zipped-artifact-import) |   Import all artifacts from a ZIP file.  |
| [`POST /v3/governance_artifact_types/{artifact_type}/import`](https://cloud.ibm.com/apidocs/watson-data-api#create-artifact-import) |   Import just one kind of artifacts from a CSV file. The business terms (`glossary_term`) will be shown in this chapter |

The following examples assume that the berarer token is already obtained, as described above. Note that the hostname part of the endpoint `api.eu-de.dataplatform.cloud.ibm.com` belongs to a system in the IBM Cloud.

### Projects and Catalogs  

This snippet obtains the name of all the projects and all the catalogs of the system.

!!! abstract "The number of projects and catalogs on a running system can be very large. Consider limiting the output "

*Click on the appropriate tab to get the `bash` or `python` code. The highlighted lines mark the actual call to Cloud Pak for Data.*

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

This snippet retrieves one catalog, identified either by its name or by its `guid`. Note that the former is passed as parameter of the REST call and the latter as part of the endpoint address.

!!! tip "The `for` loop is necessary in the python code is an iterable. Note that the bash code adresses it differently"  

*Click on the appropriate tab to get the `bash` or `python` code. The highlighted lines mark the actual call to Cloud Pak for Data or the important sentences.*

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

### Search Capability

There is an alternative way to retrieve an specific artifact (or a group of), which is the search call. It is fully described [here](https://cloud.ibm.com/apidocs/watson-data-api#searching). Instead of looking fo projects and catalogs as the previous snippets, the following examples search Categories and Business Terms (aka `glossary_term` for the API).

!!! example "The search syntax is known as Lucene query. Great for APIs... not so great for humans"

*No bash code this time... it is clearer in python and I think this kind of queries may be too cumbersome for bash. The highlighted lines mark the lucene query syntax.*

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

=== "bash"

    Too many fancy quotes, braces, escape backslashes... better in python

### Export Artifacts

This is one of the administrative tasks that everybody will do. It is about extracting all the information of the artifacts and export it to a file in order to keep a backup, transport them to another system, etc.

!!! abstract "Store all artifacts in a zip file"

*No python code is provided. This task is much more likely to be done with bash. The highlited line indicates the output file.*

=== "bash"

    ```bash title="export_all.sh" linenums="1" hl_lines="9"
        echo "---- Export ----"
        
        
        url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/export?include_custom_attribute_definitions=true"
        flags=" -s -X GET"
        header="-H content-type: application/json"  
        curl $flags $url $header \
           -H "Authorization: Bearer ${token}" \
           -o governance_artifacts.zip

    ```

=== "python"

    I think all these import/export will be more often run in shell scripts... better to use bash for it

!!! tip "Export only the business terms to a csv file"

*Another example: no zip file, but csv; not all artifacts, only business terms. Again, this task is much more likely to be performed in bash, not python. The highlited line indicates the output file.*
*

=== "bash"

    ```bash title="export.sh" linenums="1" hl_lines="7"
        echo "---- Export only the business terms to CSV----"
        
        url="https://api.eu-de.dataplatform.cloud.ibm.com/v3/governance_artifact_types/glossary_term/export"
        
        curl $flags $url $header \
           -H "Authorization: Bearer ${token}" \
           -o business_terms.csv

    ```

=== "python"

    I think all these import/export will be more often run in shell scripts... better to use bash for it

### Import Artifacts

The following examples are the counterparts of the export snippets. They are intended to ingest a large number of artifacts. `bash` is probably the best method to achive those tasks but, if you insist on doing with python, take a look at the jupyter notebooks on the Level 4 PoX section in this documentation.

!!! abstract "Import Business Terms"

*The highlited line indicates the input file.*

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

=== "python"

    I think all these import/export will be more often run in shell scripts... better to use bash for it

!!! abstract "Import all governance artifacts from a ZIP file"

*The highlited line indicates the input file. Note that this import can take a long time and it is asynchronous, that is why a wait loop is included.*

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

=== "python"

    I think all these import/export will be more often run in shell scripts... better to use bash for it
