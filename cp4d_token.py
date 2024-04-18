import json
import requests

class credentials:
    url_server = ""
    username = ""
    apikey = ""
    access_token = ""

    def __init__(self, file_credentials):
        try :
            with open(file_credentials) as f :
                data = json.load(f)
                self.url_server = data["url_server"]
                self.username = data["username"]
                self.apikey = data["api_key"]
        except :
            print("Cannot open the file ", file_credentials)
            exit()
   
    def urlRequest(self, urlSuffix):
        return self.url_server + urlSuffix

    def get_bearer_token(self):
        
        # Get a bearer token with the API key - Cloud Pak for Data SaaS
        # url = "https://iam.cloud.ibm.com/identity/token"
        # headers = {"Content-Type" : "application/x-www-form-urlencoded"}
        # data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=" + apikey
        # r = requests.post(url, headers=headers, data=data)
        # access_token = r.json()["access_token"]

        # Get a bearer token with the API key - Cloud Pak for Data Software
        urlSuffix = "/icp4d-api/v1/authorize"
        headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
        data = {"username" : self.username, "api_key" : self.apikey}
        r = requests.post(self.urlRequest(urlSuffix), headers=headers, data=json.dumps(data))

        if r.status_code != 200:
            print("Error with the request. Code: ", r.status_code)
            print(r.text)
            exit()

        try:
            self.access_token = r.json()["token"]
        except KeyError:
            print("Error with the request. Code: ", r.status_code)
            print("Hint: Did you specify the correct username and password?")
            print(r.text)
            exit()
            
        return self.access_token