from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from retailing.filters import DealerFilter
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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DealerFilter

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'debt' in request.data and request.data['debt'] != instance.debt:
            return Response({'Ошибка': 'Вы не можете изменить поле задолженности'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)


