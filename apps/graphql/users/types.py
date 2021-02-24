from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType

from ..node import DjangoNode

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (DjangoNode,)
