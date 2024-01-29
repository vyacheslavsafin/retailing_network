from rest_framework import serializers

from retailing.models import Product, Dealer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'release_date', 'dealer')


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Dealer
        fields = ('title', 'supplier', 'debt', 'email', 'country', 'city', 'street', 'house')