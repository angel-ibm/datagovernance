import requests
from cp4d_token import get_bearer_token, urlRequest

# See the file cp4d_token.py to learn how to get an autorisation token

access_token = get_bearer_token()

print("---- Catalogs ----")

urlSuffix = "/v2/catalogs"
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
r = requests.get(urlRequest(urlSuffix), headers=headers)

if r.status_code != 200:
    print("Error with the request. Code: ", r.status_code)
    print(r.text)
    exit()

try:
    for i in r.json()["catalogs"] :
        print(i["entity"]["name"])
        print(i["metadata"]["guid"])
        print("---------")
except KeyError:
    print("Unexpected message format / keys / values")
    print(r.text)
    exit()