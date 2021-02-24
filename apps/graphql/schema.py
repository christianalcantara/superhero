import graphene

from .character.query import CharacterQueries
from .character.mutation import CharacterMutation
from .users.mutation import (
    AuthUserMutation,
    CreateUserMutation
)
from .users.query import (
    UserQuerys
)


class Query(CharacterQueries, UserQuerys):
    ...


class Mutation(AuthUserMutation, CreateUserMutation, CharacterMutation):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
