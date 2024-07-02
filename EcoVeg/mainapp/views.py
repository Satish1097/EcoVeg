from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from rest_framework import generics
from .models import Customer
from .serializers import ItemSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = ItemSerializer