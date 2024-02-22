import json
import requests

# Read the API key from the file downloaded in the IBM Cloud
f = open("ikcapikey.json")
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





