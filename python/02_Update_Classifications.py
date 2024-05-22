#!/usr/bin/env python3

import requests
import time
from cp4d_token import credentials

# See the file cp4d_token.py to learn how to get an autorisation token
FILE_CREDENTIALS = "ikcapikey.json"

myconn = credentials(FILE_CREDENTIALS)
access_token = myconn.get_bearer_token()

print("---- Update Classifications from CSV----")

IMPORT_CSV_FILE = "governance-classifications.csv" 

urlSuffix='/v3/governance_artifact_types/classification/import?merge_option=specified'
headers = {"accept": "application/json", "Authorization" : "Bearer " + access_token}
files = {'file': (IMPORT_CSV_FILE, open(IMPORT_CSV_FILE, 'rb'), 'text/csv')}

r = requests.post(myconn.urlRequest(urlSuffix), headers=headers, files=files)

if r.status_code == 200 :
    status = r.json()["status"]
    print("Import finished. Status = ", status)
    print(r.text)

elif r.status_code == 202 :
    process_id = r.json()["process_id"]
    print(f"----- Import process started: {process_id} ----- ")
    print("----- Entering wait loop ------")
    urlSuffix='/v3/governance_artifact_types/import/status/' + process_id
    headers = {"accept": "application/json", "Authorization" : "Bearer " + access_token}

    while True :
        r = requests.get(myconn.urlRequest(urlSuffix), headers=headers)
        if r.status_code != 200 :
            print("Error with the request. Code: ", r.status_code)
            print(r.text)
            break
        status = r.json()["status"]
        if status != "IN_PROGRESS" :
            break
        else :
            print ("Import in progess, please wait")
            time.sleep(5)
else :
    print("Error with the request. Code: ", r.status_code)
    print(r.text)

workflow_id = r.json()["workflow_id"]
print("Workflow Id = ", workflow_id)

urlSuffix='/v3/workflows/' + workflow_id + '?include_user_tasks=true'
headers = {"accept": "application/json", "Authorization" : "Bearer " + access_token}
r = requests.get(myconn.urlRequest(urlSuffix), headers=headers)
print(r.text)

user_tasks = r.json()["entity"]["user_tasks"]
for i in user_tasks :
    if i["metadata"]["workflow_id"] == workflow_id :
        task_id = i["metadata"]["task_id"]
print ("Task Id = ", task_id)


urlSuffix='/v3/workflow_user_tasks/' + task_id + '/actions'
headers = {"accept": "application/json", "Authorization" : "Bearer " + access_token}
payload = {'action': 'complete', 'form_properties': [{'id': 'action', 'value': '#publish'}]}
r = requests.post(myconn.urlRequest(urlSuffix), headers=headers, json=payload)

if r.status_code == 202 or r.status_code == 204 :
    print("Publish Successful, Code = ", r.status_code)
else :
    print("Error in publishing artifacts, Code = ", r.status_code)
    print(r.text)
    

