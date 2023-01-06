from graph import Graph

class TSPEncoding:
    """Encodes a specific text file to a graph."""

    def __init__(self, file):
        self.file = file
    
    def encode(self):
        file = open(self.file, "r")
        connections = []
        g = Graph()

        # We read the data passed in the .txt
        for line in file:
            connections.append(line.split())

        # The first line contains all cities
        for cities in connections[0]:
            g.add_nodes(cities)

        connections.remove(connections[0])

        # We form the graph with the data obtained
        for connection in connections:
            g.add_nodes(connection[0])
            g.add_nodes(connection[1])
            g.connect_nodes(connection[0], connection[1], int(connection[2]))
        
        return g
