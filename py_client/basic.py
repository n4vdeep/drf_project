import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "localhost:8000/" # http://127.0.0.1:8000/

get_response = requests.get(endpoint, data ={"query": "Hello Django Rest Framework"}) # HTTP Request
print(get_response.text) # Print raw text response
print(get_response.json()) # Print JSONresponse
print(get_response.status_code) # Print status_code

# HTTP Request -> HTML
# REST API  HTTP Request -> JSON
