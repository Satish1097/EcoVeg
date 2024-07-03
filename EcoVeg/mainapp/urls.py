from .views import CustomerListCreate,ProductList,CategoryList,CartDetail,OrderDetail
from django.urls import path




urlpatterns = [
    path('Customer/', CustomerListCreate.as_view(), name='item-list-create'),
    path('Product/', ProductList.as_view(), name='item-detail'),
    path('ProductCategory/',CategoryList.as_view(),name='CategoryList'),
    path('Cart/',CartDetail.as_view(),name='CartDetail'),
    path('Order/',OrderDetail.as_view(),name='OrderDetail')

]
