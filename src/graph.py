from node import Node

class Graph:
    """Representation of a graph."""

    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.nodes.values())

    def add_nodes(self, node):
        """
        Add a node to the graph.
        :param node: Node to add.
        """
        if node not in self.nodes:
            self.nodes[node] = Node(node)
            self.num_nodes += 1

    def connect_nodes(self, node_from, node_to, weight=0):
        """
        Connect two nodes. Both sides are connected, that is, they are undirected edges.
        :param from: Node to connect.
        :param to: Node to connect.
        :param weight: Weight between both nodes.
        """
        if node_from not in self.nodes or node_to not in self.nodes:
            print('Make sure to add the nodes first. Could not connect ' + node_from + ' with ' + node_to)
            return None

        self.nodes[node_from].connect_node(self.nodes[node_to], weight)
        self.nodes[node_to].connect_node(self.nodes[node_from], weight)

    def obtain_node(self, node):
        """
        Returns a desired node.
        :param node: Desired node.
        """
        return self.nodes[node]
