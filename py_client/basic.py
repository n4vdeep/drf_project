import requests

endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/

get_response = requests.get(endpoint) # HTTP Request

#print(get_response.text) # Print raw text response
print(get_response.json()['message']) # Print JSONresponse
