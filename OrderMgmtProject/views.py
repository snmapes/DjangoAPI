from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from OrderMgmtApp.models import Customer, Address, Order, Product
from OrderMgmtApp.serializers import CustomerSerializer, AddressSerializer, OrderSerializer, ProductSerializer


# API Classes
def home(request):
    customers = Customer.objects.all()
    addresses = Address.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {'customers': customers,
                                         'addresses': addresses,
                                         'accounts': orders,
                                         'products': products})



class CustomerListCreate(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.create(serializer.validated_data)
            return Response(CustomerSerializer(customer).data)


class CustomerViewUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        customer = Customer.objects.get(id=pk)
        customerData = CustomerSerializer(customer)
        return Response(customerData.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            updated_customer = serializer.update(customer, serializer.validated_data)
        return Response(updated_customer)


class AddressListCreate(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.create(serializer.validated_data)
            return Response(AddressSerializer(address).data)


class AddressViewUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = AddressSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        address = Address.objects.get(id=pk)
        addressData = AddressSerializer(address)
        return Response(addressData.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        address = Address.objects.get(id=pk)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            updated_address = serializer.update(address, serializer.validated_data)
        return Response(updated_address)


class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.create(serializer.validated_data)
            return Response(OrderSerializer(order).data)


class OrderViewUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        order = Order.objects.get(id=pk)
        orderData = CustomerSerializer(order)
        return Response(orderData.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            updated_order = serializer.update(order, serializer.validated_data)
        return Response(updated_order)


class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.create(serializer.validated_data)
            return Response(OrderSerializer(product).data)


class ProductViewUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        product = Product.objects.get(id=pk)
        orderData = ProductSerializer(product)
        return Response(orderData.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            updated_product = serializer.update(product, serializer.validated_data)
        return Response(updated_product)
