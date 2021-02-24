import django_filters

from ...character.models import Character


class CharacterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Character
        fields = ["name"]
