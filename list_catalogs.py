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
except KeyError:
    print("Unexpected message format / keys / values")
    print(r.text)
    exit()

print("---- The catalog called Catalog-Angel ----")

mycatalog="Catalog-Angel"
urlSuffix = "/v2/catalogs?name=" + mycatalog
r = requests.get(urlRequest(urlSuffix), headers=headers)

if r.status_code != 200:
    print("Error with the request. Code: ", r.status_code)
    print(r.text)
    exit()

try:
    for i in r.json()["catalogs"] :
        print(i["metadata"]["guid"])
        print(i["entity"]["name"])
except KeyError:
    print("Unexpected message format / keys / values")
    print(r.text)
    exit()

mycatalog_id = i["metadata"]["guid"] 
print(f"---- The catalog with id = {mycatalog_id}  ----")

urlSuffix = "/v2/catalogs/" + mycatalog_id
r = requests.get(urlRequest(urlSuffix), headers=headers)
if r.status_code != 200:
    print("Error with the request. Code: ", r.status_code)
    print(r.text)
    exit()

try:
    print(r.json()["entity"]["name"])
except KeyError:
    print("Unexpected message format / keys / values")
    print(r.text)
    exit()

