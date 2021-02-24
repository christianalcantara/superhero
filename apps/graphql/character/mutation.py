import graphene
from graphene_file_upload.scalars import Upload

from .types import CharacterType
from ...character.models import Character


class CreateCharacter(graphene.Mutation):
    """
    Object Type Definition (mutation field)

    Mutation is a convenience type that helps us build a Field which takes Arguments and returns a
    mutation Output ObjectType.
    """

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate(cls, root, info, name, description=None):
        character = Character(name=name, description=description)
        character.save()
        return CreateCharacter(character=character)


class UpdateCharacter(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate(cls, root, info, pk, name=None, description=None):
        character = Character.objects.get(id=pk)
        if not any([name, description]):
            raise Exception("Argument name or description required.")
        if name:
            character.name = name
        if description:
            character.description = description
        character.save()
        return UpdateCharacter(character=character)


class UploadMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.String(required=True)
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, pk, file, **kwargs):
        character = Character.objects.get(id=pk)
        character.thumbnail = file
        character.save()
        return UploadMutation(success=True)


class CharacterMutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
    upload_thumbnail = UploadMutation.Field()
