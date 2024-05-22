import requests
from cp4d_token import get_bearer_token, urlRequest

def list_all_categories() :

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

    if r.status_code != 200:
        print("Error with the request. Code: ", r.status_code)
        print(r.text)
        exit()

    try:
        for i in r.json()["rows"] :
            print(i["metadata"]["name"])
    except KeyError:
        print("Unexpected message format / keys / values")
        print(r.text)
        exit()

def list_one_category(category_name) :

    # See the file cp4d_token.py to learn how to get an autorisation token

    access_token = get_bearer_token()

    # With the bearer token, we can issue requests 

    print("---- One Category ----")

    urlSuffix = "/v3/search"
    headers = {"content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    data='''{
        "_source":[ "artifact_id"],
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "metadata.artifact_type": "category"
                        }
                    },
                    {
                        "match": {
                            "metadata.name":" ''' +  category_name + '''"
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
        artifact_id = r.json()["rows"][0]["artifact_id"]
        print(artifact_id)
    except KeyError:
        print("Unexpected message format / keys / values")
        print(r.text)
        exit()

    return(artifact_id)

# Test:
# list_all_categories()
# list_one_category("Locations")

  # Alternative expression without string concatenation but doubling the curl braces
    # data = f'''
    #         {{
    #             "_source": ["artifact_id"],
    #             "query": {{
    #                 "bool": {{
    #                     "must": [
    #                         {{
    #                             "match": {{
    #                                 "metadata.artifact_type": "category"
    #                             }}
    #                         }},
    #                         {{
    #                             "match": {{
    #                                 "metadata.name": "{category_name}"
    #                             }}
    #                         }}
    #                     ]
    #                 }}
    #             }}
    #         }}
    #     '''




