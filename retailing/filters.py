import django_filters

from retailing.models import Dealer


class DealerFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name="country")

    class Meta:
        model = Dealer
        fields = ("country",)