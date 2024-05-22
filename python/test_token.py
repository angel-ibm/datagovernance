import requests
from cp4d_token import credentials

FILE_CREDENTIALS = "ikcapikey.json"

myconn = credentials(FILE_CREDENTIALS)
access_token = myconn.get_bearer_token()

print(myconn.access_token)

urlSuffix='/v3/glossary_terms/heartbeat'
headers = {"accept": "application/json", "Authorization" : "Bearer " + access_token}
r = requests.get(myconn.urlRequest(urlSuffix), headers=headers)
print(myconn.urlRequest(urlSuffix))
print(r.text)

