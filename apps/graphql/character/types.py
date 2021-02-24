import graphene
from graphene_django.types import DjangoObjectType

from ..node import DjangoNode
from ...character.models import Character, Favorite


class CharacterType(DjangoObjectType):
    """
    Character Object Type Definition
    """

    thumb_url = graphene.String()

    class Meta:
        model = Character
        interfaces = (DjangoNode,)


class FavoriteType(DjangoObjectType):
    """
    Favorite Object Type Definition
    """

    class Meta:
        model = Favorite
        interfaces = (DjangoNode,)
