import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .filter import CharacterFilter
from .types import CharacterType, FavoriteType
from ..node import DjangoNode


class CharacterQueries(graphene.ObjectType):
    character = DjangoNode.Field(CharacterType, id=graphene.String())
    characters = DjangoFilterConnectionField(
        CharacterType, filterset_class=CharacterFilter
    )
    favorite = DjangoNode.Field(FavoriteType)
