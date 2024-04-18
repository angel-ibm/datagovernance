import requests


url = "https://cpd-cpd.apps.ocp-1100005cc8-fsqw.cloud.techzone.ibm.com/v4/reference_data_sets/a9814ad7-7aea-469c-8d04-ca9d0dc5335e/versions/4b2fcf5d-2a78-49cc-991e-b1a3ce01023f_0/value_imports"

import_parameters = '{"artifact_id_mode": False,"code": "DEPARTMENT_CODE","first_row_header": True,"import_relationships_only": False,"skip_workflow_if_possible": False,"trim_white_spaces": True,"value": "DEPARTMENT_EN","value_conflicts": "OVERWRITE" }'
import_parameters = {
            "artifact_id_mode": False,
            "code": "DEPARTMENT_CODE",
            "first_row_header": True,
            "import_relationships_only": False,
            "skip_workflow_if_possible": False, 
            "trim_white_spaces": True,
            "value": "DEPARTMENT_EN",
            "value_conflicts": "OVERWRITE" 
        }

files={
    'import_csv_file'   :  ( 'import_csv_file', open('governance-reference-department.csv','rb') ),
    'import_parameters' : (None, str(import_parameters))   
}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx5aW0tNmlsNzVrZkdNYWEzRjRLc0xJQ0JuR1lOeUdwemMtNU9GUXRVRUEifQ.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6IkFkbWluIiwicGVybWlzc2lvbnMiOlsiYWRtaW5pc3RyYXRvciIsImNhbl9wcm92aXNpb24iLCJtb25pdG9yX3BsYXRmb3JtIiwiY29uZmlndXJlX3BsYXRmb3JtIiwidmlld19wbGF0Zm9ybV9oZWFsdGgiLCJjb25maWd1cmVfYXV0aCIsIm1hbmFnZV91c2VycyIsIm1hbmFnZV9ncm91cHMiLCJtYW5hZ2Vfc2VydmljZV9pbnN0YW5jZXMiLCJtYW5hZ2VfdmF1bHRzX2FuZF9zZWNyZXRzIiwic2hhcmVfc2VjcmV0cyIsImFkZF92YXVsdHMiLCJtYW5hZ2VfY2F0YWxvZyIsImNyZWF0ZV9wcm9qZWN0IiwiY3JlYXRlX3NwYWNlIiwiYXV0aG9yX2dvdmVybmFuY2VfYXJ0aWZhY3RzIiwibWFuYWdlX2dvdmVybmFuY2Vfd29ya2Zsb3ciLCJ2aWV3X2dvdmVybmFuY2VfYXJ0aWZhY3RzIiwibWFuYWdlX2NhdGVnb3JpZXMiLCJtYW5hZ2VfZGlzY292ZXJ5IiwiYWNjZXNzX2RhdGFfcXVhbGl0eV9hc3NldF90eXBlcyIsIm1lYXN1cmVfZGF0YV9xdWFsaXR5IiwibWFuYWdlX2RhdGFfcXVhbGl0eV9zbGFfcnVsZXMiLCJkYXRhX3F1YWxpdHlfZHJpbGxfZG93biIsIm1hbmFnZV9nbG9zc2FyeSIsImFjY2Vzc19jYXRhbG9nIl0sImdyb3VwcyI6WzEwMDAwXSwic3ViIjoiYWRtaW4iLCJpc3MiOiJLTk9YU1NPIiwiYXVkIjoiRFNYIiwidWlkIjoiMTAwMDMzMDk5OSIsImF1dGhlbnRpY2F0b3IiOiJkZWZhdWx0IiwiZGlzcGxheV9uYW1lIjoiYWRtaW4iLCJhcGlfcmVxdWVzdCI6ZmFsc2UsImlhdCI6MTcxMzM0NDY1MywiZXhwIjoxNzEzMzg3ODUzfQ.Q5QsuiiWMcS5-LOWPrCRN_H3IMYDhQOcq0vlVnad9WpVUfxIb4Sy6_rW5TX6n6LA5Ut4j0xDK3RF7e0cxcJuBL5HRcwrhbJhKCoxe2AMgwOqExYRr0mNbpKePnlfOLtRKIA2uoIYo8wwAw_mRUeUqGWY_EWRhDFNckgW0Q1eY5hhXtF9UCUC7yrnSQqFKvuM9pKyhdJ54k5XReCasouFcLY7ZOoBaoyXuEV61xJH-ShX3q0P3VMJrXWJovznvu_2CiyiWBzQDXTazteIMQ24MnbyzPGSm5LxfwdGVs9YJ4KlZq_gjV__29EO6YaYEQW87Hejhb3vGcUz6ibSQwz2IQ'
}

response = requests.post( url, headers=headers, files=files)

print(response.text)
