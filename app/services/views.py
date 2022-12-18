#from rest_framework.views import APIView
#from django.http import Http404
#from rest_framework.response import Response

from rest_framework import generics
from app.services.models import TypeServices
from app.services.serializers import TypeServicesSerializer


# Create your views here.

# This class is a generic view that returns all object from the TypeServices model
class ServicesList(generics.ListAPIView):
    queryset = TypeServices.objects.all()
    serializer_class = TypeServicesSerializer


# This class is a generic view that returns a single object from the TypeServices model
class ServicesDetail(generics.RetrieveAPIView):
    queryset = TypeServices.objects.all()
    serializer_class = TypeServicesSerializer
