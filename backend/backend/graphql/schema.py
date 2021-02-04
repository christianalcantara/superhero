from .character.query import CharacterQueries
from .users.query import (
    UserQuerys
)
from .users.mutation import (
    AuthUserMutation,
    CreateUserMutation
)
import graphene


class Query(CharacterQueries, UserQuerys):
    ...


class Mutation(AuthUserMutation, CreateUserMutation):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
