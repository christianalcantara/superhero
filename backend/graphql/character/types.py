from graphql_jwt.decorators import login_required, superuser_required
from graphene_django.types import DjangoObjectType
from ..node import DjangoNode
from ...character.models import (
    Character,
    Favorite
)


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        interfaces = (DjangoNode,)


class FavoriteType(DjangoObjectType):
    class Meta:
        model = Favorite
        interfaces = (DjangoNode,)
