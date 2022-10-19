from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class CustomerListCreateApi(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer()

# queryset using OR
qs=Orders.objects.filter(first_name_startswith='Kavin')|Orders.objects.all()

# queryset using NOT
qs1= qs.exclude(first_name='Kavin')

