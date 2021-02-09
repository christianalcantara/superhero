import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .filter import CharacterFilter
from .types import (
    CharacterType,
    FavoriteType
)
from ..node import DjangoNode
from ...character.models import Character


class CharacterQueries(graphene.ObjectType):
    character = graphene.Field(CharacterType, id=graphene.String())
    characters = DjangoFilterConnectionField(CharacterType, filterset_class=CharacterFilter)
    favorite = DjangoNode.Field(FavoriteType)

    def resolve_character(root, info, id):
        # Querying a single question
        return Character.objects.get(pk=id)
