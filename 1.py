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

# With the bearer token, we can issue requests to the catalog

print("---- Catalogs ----")

url = "https://api.eu-de.dataplatform.cloud.ibm.com/v2/catalogs"
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}

r = requests.get(url, headers=headers)
for i in r.json()["catalogs"] :
    print(i["entity"]["name"])


# ... or, in general, to all services of Cloud Pak for Data

print("---- Projects ----")

url = "https://api.eu-de.dataplatform.cloud.ibm.com/v2/projects"
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}

r = requests.get(url, headers=headers)
for i in r.json()["resources"] :
    print(i["entity"]["name"])

