from rest_framework import viewsets, permissions

from retailing.models import Product, Dealer
from retailing.serializers import ProductSerializer, SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)
