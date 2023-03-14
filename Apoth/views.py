from django.shortcuts import render
from .models import Flower
from .serializers import FlowerSerializer
from rest_framework.renderers import JSONOpenAPIRenderer
from django.http import HttpResponse
# Model Object -Single Flower Data

def flower_detail(request,pk):
    flo = Flower.objects.get(id=pk)
    serializer = FlowerSerializer(flo)
    Json_data = JSONOpenAPIRenderer().render(serializer.data)
    return HttpResponse(Json_data,content_type='application/json')


# All Query set - All flower Data
def flower_list(request):
    flo = Flower.objects.all()
    serializer = FlowerSerializer(flo,many= True)
    Json_data = JSONOpenAPIRenderer().render(serializer.data)
    return HttpResponse(Json_data)


