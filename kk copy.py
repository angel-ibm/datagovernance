import requests

url = "https://cpd-cp4d.apps.6522a8d3368cb40016de15e7.cloud.techzone.ibm.com/v4/reference_data_sets/5ea64c73-e480-4933-92e7-0d5a5a4d74c1/versions/e49ca29d-7d2b-4bd1-aca6-44e2a0cd7a06_0/value_imports"

import_parameters = {"import_parameters": {
            "code": "DEPARTMENT_CODE",
            "value_conflicts": "OVERWRITE",
            "is_first_row_header": True,
            "trim_white_spaces": False,
            "skip_workflow_if_possible": False,
            "import_relationships_only": True,
            "start_immediately": True,
            "include_associated_terms": False,
            "artifact_id_mode": False,
            "custom_columns_mappings": [
                {
                    "csv_column_name": "DEPARTMENT_CODE",
                    "custom_column_name": "Code"
                },
                {
                    "csv_column_name": "DEPARTMENT_EN",
                    "custom_column_name": "Value"
                }
            ]
        }
    }
files=[
  ('import_csv_file',('governance-reference-department.csv',open('governance-reference-department.csv','rb'),'text/csv'))
]
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik90clNOcWRuQVAwYi1EWThuU3lRc25CbEMyc3N1X0dCcGdLODI2ZklELWMifQ.eyJ1c2VybmFtZSI6ImFuZ2VsaXRvIiwicm9sZSI6IlVzZXIiLCJwZXJtaXNzaW9ucyI6WyJhY2Nlc3NfY2F0YWxvZyIsInZpZXdfZ292ZXJuYW5jZV9hcnRpZmFjdHMiLCJtYW5hZ2VfY2F0YWxvZyIsImNyZWF0ZV9zcGFjZSIsIm1hbmFnZV9zcGFjZSIsIm1vbml0b3Jfc3BhY2UiLCJtYW5hZ2VfZGlzY292ZXJ5IiwiZ2xvc3NhcnlfYWRtaW4iLCJhdXRob3JfZ292ZXJuYW5jZV9hcnRpZmFjdHMiLCJtYW5hZ2VfZ2xvc3NhcnkiLCJtYW5hZ2VfY2F0ZWdvcmllcyIsImFjY2Vzc19kYXRhX3F1YWxpdHlfYXNzZXRfdHlwZXMiLCJjcmVhdGVfcHJvamVjdCIsIm1hbmFnZV9wcm9qZWN0IiwibW9uaXRvcl9wcm9qZWN0Iiwidmlld19wbGF0Zm9ybV9oZWFsdGgiLCJhZGRfdmF1bHRzIiwibWFuYWdlX3ZhdWx0c19hbmRfc2VjcmV0cyIsInNoYXJlX3NlY3JldHMiLCJtYW5hZ2VfZ292ZXJuYW5jZV93b3JrZmxvdyIsIm1lYXN1cmVfZGF0YV9xdWFsaXR5IiwibWFuYWdlX2RhdGFfcXVhbGl0eV9zbGFfcnVsZXMiLCJkYXRhX3F1YWxpdHlfZHJpbGxfZG93biJdLCJncm91cHMiOlsxMDAwMSwxMDAwMF0sInN1YiI6ImFuZ2VsaXRvIiwiaXNzIjoiS05PWFNTTyIsImF1ZCI6IkRTWCIsInVpZCI6IjEwMDAzMzEwOTgiLCJhdXRoZW50aWNhdG9yIjoiZGVmYXVsdCIsImRpc3BsYXlfbmFtZSI6ImFuZ2VsaXRvIiwiYXBpX3JlcXVlc3QiOmZhbHNlLCJpYXQiOjE3MTMyNjg5ODIsImV4cCI6MTcxMzMxMjE0Nn0.1GhhyuT0FxuaQUbIJNro77AGg4bxxRjMwb4dkwMYU7AoEnKdB6rhvSNPqWzQ8Hcr92K3pPuwcaDzS8iWRNLYzp7EXJ2EStKbWl3aJ2sRc0P2TsqDLMECJLdqzcdv_d_WowlHFyNpuGZGhoMXAYLPLzhkMW1mG3v34tkNx3YhUoeWcx0Ulxouwr8YnGgjZONQf2jcNe5O8M4f26GlkuLkAAjB8b3gu2imKC-A1fw-oWyjKCkU9PWQV6sDnOlgD5Xtx8Q4yXzT26tn_-CE5GNso505o0r-djs5ALj_kmFOaYZVavldSsz_HPp-RjJXhqyiZyG9BQpD2pz3glUMeic2sQ'
}

response = requests.request("POST", url, headers=headers, data=import_parameters, files=files)

print(response.text)
