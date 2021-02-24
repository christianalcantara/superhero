import django_filters
from ...character.models import Character


class CharacterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    id = django_filters.NumericRangeFilter()

    class Meta:
        model = Character
        fields = [
            'id',
            'name'
        ]
