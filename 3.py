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


url = 'https://api.eu-de.dataplatform.cloud.ibm.com/v3/categories'
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
data='{"name":"MotoGP"}'

r = requests.post(url, headers=headers, data=data)
category_id = r.json()["resources"][0]["artifact_id"]
print(f"MotoGP category created with the id={category_id}")

