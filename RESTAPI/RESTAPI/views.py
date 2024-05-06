from django.http import JsonResponse
from .models import RESTAPI
from .serializers import RESTAPISerializer

def api_list (request):
    #get all the  apis
    #serialize them
    #return jsn
    
    apis= RESTAPI.objects.all()
    serializers = RESTAPISerializer (apis, many = True)
    return JsonResponse (serializers.data, safe=False)