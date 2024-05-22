import requests
from cp4d_token import get_bearer_token, urlRequest

EXPORT_ZIP_FILE = "all_artifacts.zip"

# See the file cp4d_token.py to learn how to get an autorisation token

access_token = get_bearer_token()

print("---- Export all as ZIP file----")

urlSuffix = "/v3/governance_artifact_types/export?include_custom_attribute_definitions=true"
headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
r = requests.get(urlRequest(urlSuffix), headers=headers)

if r.status_code != 200:
    print("Error with the request. Code: ", r.status_code)
    print(r.text)
    exit()

with open(EXPORT_ZIP_FILE, "wb") as zip_file:
    zip_file.write(r.content)
    zip_file.close()