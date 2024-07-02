from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from rest_framework import generics
from .models import Customer,Product
from .serializers import CustomerSerializer,ProductSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer