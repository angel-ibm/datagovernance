import requests
from cp4d_token import get_bearer_token, urlRequest

# See the file cp4d_token.py to learn how to get an autorisation token

access_token = get_bearer_token()

urlSuffix = '/v3/categories'
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
data='{"name":"MotoGP"}'

r = requests.post(urlRequest(urlSuffix), headers=headers, data=data)

category_id = r.json()["resources"][0]["artifact_id"]
print(f"MotoGP category created with the id={category_id}")