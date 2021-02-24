import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    is_admin = django_filters.BooleanFilter()
    is_superuser = django_filters.BooleanFilter()

    class Meta:
        model = User
        fields = ["username", "email", "is_admin", "is_superuser"]
