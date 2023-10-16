graph_1 = [[0,2,6,0,0,0,0], # vertex 0 
           [2,0,0,5,0,0,0], # vertex 1
           [6,0,0,8,0,0,0], # vertex 2
           [0,5,8,0,0,0,0], # vertex 3
           [0,0,0,10,0,6,2], # vertex 4
           [0,0,0,15,6,0,6], # vertex 5
           [0,0,0,0,0,0,0]] # vertex 6
           
           

Class Graph(): 
    """
    Dikjstra's algorithm 
    
    Attributes:
        graph: A matrix representing a graph                         weighted edges 
        vertex: An integer representing the number of vertices in the graph 
    """
    def __init__(self, graph):
    """
    Initialize the attributes of the class
    """
    
        self.graph = graph
        self.vertex = len(graph)
    def getWeights(self, vi, vj):
    """
    Given two vertices, return the weight between the two
    
    Args: 
        vi: 
    """
        weight = self.graph[vi][vj]
        return weight
    def dijkstra(self, source, end): 
        visited_nodes = []
        unvisited_nodes = []
        for i in range(0, len(graph)):
            unvisited_nodes.append(i)
        shortest_path = [inf] * self.vertex 
        shortest_path[source] = 0
        current_node = source
        while last not in visited_nodes: 
            threshold = 0
            all_edges = []
            edge_index = None
            for vertex in self.graph[current_node]:
                if (vertex > 0):
                    all_edges.append(vertex)
            min_edge = min(all_edges)
            visited_nodes.append(min_edge)
            unvisited_nodes.remove(current_node.index(min_edge))
            current_node = min_edge
            for v
