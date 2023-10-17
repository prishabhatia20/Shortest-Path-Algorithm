"""
This script does this...
"""
import math
   
class Graph():
    """
    Dikjstra's algorithm 
    
    Attributes:
        graph: A matrix representing a graph                         weighted edges 
        vertex: An integer representing the number of vertices in the graph 
    """

    INF = math.inf
    def __init__(self, graph):
        """
        Initialize the attributes of the class
        """
        self.graph = graph
        self.vertex = len(graph)
    def get_weights(self, vi, vj):
        """
        Given two vertices, return the weight between the two
    
        Args: 
            vi: 
        """
        weight = self.graph[vi][vj]
        return weight
    def dijkstra(self, source, end):
        """
        Dijkstra algorithm  
        """
        visited_nodes = []
        unvisited_nodes = []
        for i in range(self.vertex):
            unvisited_nodes.append(i)
        shortest_path = [self.INF] * self.vertex
        shortest_path[source] = 0
        current_node = source
        prev_node = current_node
        while end not in visited_nodes:
            print(f"current node : {current_node}")
            min_weight = 0
            next_node = current_node
            print(f"prev_node: {prev_node}")
            for vertex in range(self.vertex):
                weight = self.graph[current_node][vertex]
                print(weight)
                if weight != 0 and vertex != prev_node and vertex not in visited_nodes:
                    if min_weight == 0:
                        min_weight = weight 
                        next_node = vertex
                        prev_node = current_node
                        # print(min_weight, next_node)
                    elif min_weight != 0 and weight < min_weight:
                        
                        min_weight = weight
                        next_node = vertex
                        prev_node = current_node
                        # print(min_weight, next_node)   
            if min_weight == 0:
                next_node = prev_node
            print(f"next node: {next_node}")
            print(f"shortest edge: {min_weight}")
            if current_node in unvisited_nodes:
                visited_nodes.append(current_node)
                unvisited_nodes.remove(current_node)
            print(f"visted nodes: {visited_nodes}")
            print(f"unvisited nodes: {unvisited_nodes}")
            print(shortest_path)
            for node in unvisited_nodes:
                edge_weight = self.get_weights(current_node, node)
                if edge_weight != 0:
                    if shortest_path[current_node] + edge_weight < shortest_path[node]:
                        shortest_path[node] = shortest_path[current_node] + edge_weight
            print(shortest_path)
            current_node = next_node
        return shortest_path[end]
    
graph_1 = [[0,2,6,0,0,0,0], # vertex 0 
           [2,0,0,5,0,0,0], # vertex 1
           [6,0,0,8,0,0,0], # vertex 2
           [0,5,8,0,10,15,0], # vertex 3
           [0,0,0,10,0,6,2], # vertex 4
           [0,0,0,15,6,0,6], # vertex 5
           [0,0,0,0,2,6,0]] # vertex 6
    
g = Graph(graph_1)
p = g.dijkstra(0,6)
print(p)

    
