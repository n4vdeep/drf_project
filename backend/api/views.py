from django.http import JsonResponse

# Define Function based view
def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "This is your Django API response!"})