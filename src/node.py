class Node:
    """Representation of a node."""

    def __init__(self, node):
        self.id = node # Id of the node.
        self.connections = {} # Neighbors of the node.

    def __iter__(self):
        return iter()

    def connect_node(self, neighbor, weight=0):
        """
        Connect this node with the given one.
        :param neighbor: Node to connect to.
        :param weight: Weight between them.
        """
        self.connections[neighbor] = weight

    def obtain_connections(self):
        """Returns the connections of this node."""
        return list(self.connections.keys())

    def obtain_id(self):
        """Returns the id of this node."""
        return self.id

    def obtain_weight(self, neighbor):
        """
        Returns the weight between this node and the given one.
        :param neighbor: Given node.
        """
        return self.connections[neighbor]
