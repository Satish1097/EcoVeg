from .views import CustomerListCreate, ItemDetail
from django.urls import path




urlpatterns = [
    path('Customer/', CustomerListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
