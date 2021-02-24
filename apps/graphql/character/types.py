from graphql_jwt.decorators import login_required, superuser_required
from graphene_django.types import DjangoObjectType
import graphene
from ..node import DjangoNode
from ...character.models import (
    Character,
    Favorite
)


class CharacterType(DjangoObjectType):
    thumb_url = graphene.String()
    class Meta:
        model = Character
        interfaces = (DjangoNode,)


class FavoriteType(DjangoObjectType):
    class Meta:
        model = Favorite
        interfaces = (DjangoNode,)
