from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from rest_framework import generics
from .models import Customer,Product,ProductCategory
from .serializers import CustomerSerializer,ProductSerializer,CategorySerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=CategorySerializer