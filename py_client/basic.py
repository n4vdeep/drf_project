import requests

endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/

get_response = requests.get(endpoint, params={"product_id": 123}) # HTTP Request

#print(get_response.text) # Print raw text response
# print(get_response.url)
print(get_response.json()) # Print JSONresponse
