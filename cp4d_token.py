import json
import requests

FILE_CREDENTIALS = "ikcapikey.json"
URL_SERVER = "https://cpd-cpd.apps.ocp-1100005cc8-7fis.cloud.techzone.ibm.com"
    
def urlRequest(urlSuffix):
    return URL_SERVER + urlSuffix

def get_bearer_token():
    # Read the credentials from a file
    f = open(FILE_CREDENTIALS)
    data = json.load(f)
    username = data["username"]
    apikey = data["api_key"]

    # Get a bearer token with the API key - Cloud Pak for Data SaaS
    # url = "https://iam.cloud.ibm.com/identity/token"
    # headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    # data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=" + apikey
    # r = requests.post(url, headers=headers, data=data)
    # access_token = r.json()["access_token"]

    # Get a bearer token with the API key - Cloud Pak for Data Software
    urlSuffix = "/icp4d-api/v1/authorize"
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
    data = {"username" : username, "api_key" : apikey}
    r = requests.post(urlRequest(urlSuffix), headers=headers, data=json.dumps(data))

    try:
        access_token = r.json()["token"]
    except KeyError:
        print("Error with the request. Code: ", r.status_code)
        print("Hint: Did you specify the correct username and password?")
        print(r.text)
        exit()
        
    return access_token