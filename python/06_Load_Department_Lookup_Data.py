#!/usr/bin/env python3

import requests
import time, json
from cp4d_token import credentials

# See the file cp4d_token.py to learn how to get an autorisation token
FILE_CREDENTIALS = "ikcapikey.json"

myconn = credentials(FILE_CREDENTIALS)
access_token = myconn.get_bearer_token()

print("---- Load Department Lookup Data from CSV----")

IMPORT_CSV_FILE = "governance-reference-department.csv"

artifact_id = None
version_id = None
urlSuffix='/v3/governance_artifact_types/reference_data?workflow_status=published&limit=200'
headers = {"accept": "application/json" ,"Authorization" : "Bearer " + access_token}

r = requests.get(myconn.urlRequest(urlSuffix), headers=headers)

if r.status_code == 200 :
    for i in r.json()["resources"] :
        if i["name"] == "Department Lookup" :
            artifact_id = i["artifact_id"]
            version_id = i["version_id"]
            print("artifact_id = ", artifact_id, " version_id = " , version_id)
            break
else :
    print("Error in retrieving reference data artifacts, Code = ", r.status_code)
    print(r.text)

if artifact_id is None or version_id is None:
    print("Department Lookup not found")
else :    
    urlSuffix='/v4/reference_data_sets/' + artifact_id + '/versions/' + version_id + '/value_imports'
    headers = {"Authorization" : "Bearer " + access_token }
    import_parameters = {
        "artifact_id_mode": False,
        "code": "DEPARTMENT_CODE",
        "first_row_header": True,
        "import_relationships_only": False,
        "skip_workflow_if_possible": False, 
        "trim_white_spaces": True,
        "value": "DEPARTMENT_EN",
        "value_conflicts": "OVERWRITE" 
    }
    files={
        'import_csv_file'   : ('import_csv_file', open(IMPORT_CSV_FILE,'rb') ),
        'import_parameters' : (None, str(import_parameters))   
    }
    
    r = requests.post(myconn.urlRequest(urlSuffix), headers=headers, files=files)
    print("Status Code = ", r.status_code)
    print(r.text)


    
