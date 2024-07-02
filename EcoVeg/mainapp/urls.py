from .views import CustomerListCreate,ProductList
from django.urls import path




urlpatterns = [
    path('Customer/', CustomerListCreate.as_view(), name='item-list-create'),
    path('Product/', ProductList.as_view(), name='item-detail'),
]
