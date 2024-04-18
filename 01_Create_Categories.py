import requests
import time
from cp4d_token import credentials

# See the file cp4d_token.py to learn how to get an autorisation token
FILE_CREDENTIALS = "ikcapikey.json"

myconn = credentials(FILE_CREDENTIALS)
access_token = myconn.get_bearer_token()

print("---- Import Categories from CSV----")

IMPORT_CSV_FILE = "governance-categories.csv"
urlSuffix='/v3/governance_artifact_types/category/import?merge_option=all'
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
            exit()
        status = r.json()["status"]
        if status != "IN_PROGRESS" :
            break
        else :
            print ("Import in progess, please wait")
            time.sleep(5)
else :
    print("Error with the request. Code: ", r.status_code)
    print(r.text)




