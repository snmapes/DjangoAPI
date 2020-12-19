"""OrderMgmtProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth import views as auth_views

from . import views
from .views import CustomerListCreate, AddressListCreate, AddressViewUpdate, \
    CustomerViewUpdate, OrderListCreate, OrderViewUpdate, ProductListCreate, ProductViewUpdate

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    path('admin/', admin.site.urls),
    url(r'^List_customers/$', CustomerListCreate.as_view(), name='list_customer_REST'),
    url(r'^Update_Customer/(?P<pk>\d+)/$', CustomerViewUpdate.as_view(), name='update_customer_REST'),
    url(r'^List_addresses/$', AddressListCreate.as_view(), name='list_address_REST'),
    url(r'^Update_Address/(?P<pk>\d+)/$', AddressViewUpdate.as_view(), name='update_address_REST'),
    url(r'^List_orders/$', OrderListCreate.as_view(), name='list_order_REST'),
    url(r'^Update_Orders/(?P<pk>\d+)/$', OrderViewUpdate.as_view(), name='update_order_REST'),
    url(r'^List_products/$', ProductListCreate.as_view(), name='list_product_REST'),
    url(r'^Update_Product/(?P<pk>\d+)/$', ProductViewUpdate.as_view(), name='update_product_REST'),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
]
