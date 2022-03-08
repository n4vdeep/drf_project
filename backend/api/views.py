import json
from django.http import JsonResponse

# Define Function based view
def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    # print(request.GET) # url query params
    # print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # Takes in a string of json data -> Python Dict
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    print(data['headers'])
    data['content_type'] = request.content_type
    return JsonResponse(data)