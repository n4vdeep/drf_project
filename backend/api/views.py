import json
from django.http import JsonResponse

from products.models import Product

# Define Function based view
# def api_home_OLD(request, *args, **kwargs):
#     # request -> HttpRequest -> Django
#     # print(dir(request))
#     # request.body
#     # print(request.GET) # url query params
#     # print(request.POST)
#     body = request.body # byte string of JSON data
#     data = {}
#     try:
#         data = json.loads(body) # Takes in a string of json data -> Python Dict
#     except:
#         pass
#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     print(data['headers'])
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}

    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        # print(data)

        # Essentially what we are trying to do:
        # model instance (model_data)
        # turn to into a python dict
        # return JSON to my client
        
    return JsonResponse(data)