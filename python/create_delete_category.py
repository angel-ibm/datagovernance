import requests
import time
from cp4d_token import get_bearer_token, urlRequest


def create_category(category_name) :

    # See the file cp4d_token.py to learn how to get an autorisation token
    access_token = get_bearer_token()

    urlSuffix = '/v3/categories'
    headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    data='{"name":"' + category_name + '"}'

    r = requests.post(urlRequest(urlSuffix), headers=headers, data=data)

    if r.status_code != 201:
        print("Error with the request. Code: ", r.status_code)
        print(r.text)
        exit()

    try:
        category_id = r.json()["resources"][0]["artifact_id"]
    except KeyError:
        print("Unexpected message format / keys / values")
        print(r.text)
        exit()
        
    print(f"{category_name} category created with the id={category_id}")

    return category_id

def delete_category(category_guid) :

    # See the file cp4d_token.py to learn how to get an autorisation token
    access_token = get_bearer_token()

    urlSuffix = '/v3/categories/' +  category_guid
    headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}

    r = requests.delete(urlRequest(urlSuffix), headers=headers)

    if r.status_code != 200:
        print("Error with the request. Code: ", r.status_code)
        print(r.text)
        exit()
    
    print("Category deleted")

    return(0)

# Test:
# category_guid = create_category("MotoGP")
# delete_category(category_guid)

