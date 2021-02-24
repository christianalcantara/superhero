import graphene
import graphql_jwt

from .types import UserType


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        user = info.context.user
        return cls(user=user)


class UserQuerys(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return user
