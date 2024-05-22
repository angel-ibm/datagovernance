import requests
from cp4d_token import get_bearer_token, urlRequest

# See the file cp4d_token.py to learn how to get an autorisation token

access_token = get_bearer_token()

# With the bearer token, we can issue requests 


print("---- Business Terms of MotoGP ----")

urlSuffix = "/v3/search"
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
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

r = requests.post(urlRequest(urlSuffix), headers=headers, data=data)

if r.status_code != 200:
    print("Error with the request. Code: ", r.status_code)
    print(r.text)
    exit()

try:
    for i in r.json()["rows"] :
        print(i["metadata"]["name"], end=": ")
        print(i["metadata"]["description"], end="\n\n")
except KeyError:
    print("Unexpected message format / keys / values")
    print(r.text)
    exit()