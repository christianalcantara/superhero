import graphene
from ...character.models import Character
from .types import CharacterType
from graphene_file_upload.scalars import Upload


class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate(cls, root, info, name, description=None):
        character = Character(
            name=name,
            description=description
        )
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
            raise Exception('Argument name or description required.')
        if name:
            character.name = name
        if description:
            character.description = description
        character.save()
        return UpdateCharacter(character=character)


class CharacterMutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
