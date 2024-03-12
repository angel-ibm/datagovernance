import requests
from cp4d_token import get_bearer_token, urlRequest

# See the file cp4d_token.py to learn how to get an autorisation token

access_token = get_bearer_token()

# With the bearer token, we can issue requests 

print("---- All Categories ----")

urlSuffix = "/v3/search"
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
data = '''{
    "query": {
        "match": {
            "metadata.artifact_type": "category"
        }
    }
}'''

r = requests.post(urlRequest(urlSuffix), headers=headers, data=data)

for i in r.json()["rows"] :
    print(i["metadata"]["name"])
