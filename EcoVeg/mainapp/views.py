from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from rest_framework import generics
from .models import Customer,Product,ProductCategory,Cart,Order
from .serializers import CustomerSerializer,ProductSerializer,CategorySerializer,CartSerializer,OrderSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=CategorySerializer

class CartDetail(generics.ListCreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class OrderDetail(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer