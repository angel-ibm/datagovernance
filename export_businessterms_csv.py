import requests
from cp4d_token import get_bearer_token, urlRequest

EXPORT_CSV_FILE = "all_business_terms.csv"

# See the file cp4d_token.py to learn how to get an autorisation token
access_token = get_bearer_token()

print("---- Export only the business terms to CSV----")

urlSuffix="/v3/governance_artifact_types/glossary_term/export"
headers = {"content-type" : "multipart/form-data", "Authorization" : "Bearer " + access_token}
r = requests.get(urlRequest(urlSuffix), headers=headers)

with open(EXPORT_CSV_FILE, "w") as csv_file:
    csv_file.write(r.text)
    csv_file.close()
