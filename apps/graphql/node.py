from graphene.relay import Node


class DjangoNode(Node):
    """
    This class removes base64 unique ids and operates with plain Integer IDs
    """

    @classmethod
    def get_node_from_global_id(cls, info, global_id, only_type=None):
        node = super().get_node_from_global_id(info, global_id, only_type)
        if node:
            return node

        get_node = getattr(only_type, "get_node", None)

        if get_node:
            node = get_node(info, global_id)
            return node

    @classmethod
    def to_global_id(cls, type, id):
        return id
