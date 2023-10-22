"""
This script contains the file for the Graph class
"""
import math
import time
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    """
    Dikjstra's algorithm

    Attributes:
        graph: A adjacency matrix representing a graph weighted edges
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
            vi: an integer representing the first vertex
            vj: an integer representing the second vertex
        Returns: The weight between the two vertices
        """

        # Assign and return the weight between the two vertices
        weight = self.graph[vi][vj]
        return weight

    def visualize_graph(self):
        """
        Visualize a graph in adjacency matrix form given the matrix and number of vertex
        """
        graph_viz = nx.DiGraph()
        for row in range(self.vertex):
            for column in range(self.vertex):
                edge_weight = self.get_weights(row, column)
                if edge_weight > 1:
                    graph_viz.add_edge(row, column, weight=edge_weight)

        pos = nx.spring_layout(graph_viz)
        nx.draw(graph_viz, pos, node_color="pink", with_labels=True)
        # specifiy edge labels explicitly
        edge_labels = dict(
            [
                (
                    (
                        u,
                        v,
                    ),
                    d["weight"],
                )
                for u, v, d in graph_viz.edges(data=True)
            ]
        )
        nx.draw_networkx_edge_labels(graph_viz, pos, edge_labels=edge_labels)
        plt.show()

    def dijkstra(self, source, end):
        """
        Dijkstra algorithm that finds the shortest path from one vertex
        to another given all weights assigned to edges

        Args:
            self: an instance of the Graph class
            source: an integer representing the starting vertex
            end: an integer representing the ending vertex
        """
        # Create an empty list to hold the visited and unvisited nodes
        visited_nodes = []
        unvisited_nodes = []

        # Append all nodes in the graph to unvisited_nodes
        for i in range(self.vertex):
            unvisited_nodes.append(i)

        # Create a list of infinity values
        shortest_path = [self.INF] * self.vertex
        shortest_path[source] = 0

        # Set current node to the first node
        current_node = source
        prev_node = current_node

        # Loop to run while the end vertex has not been reached
        while end not in visited_nodes:
            print(f"current node : {current_node}")
            # Set the minimum weight
            min_weight = 0
            next_node = current_node
            print(f"prev_node: {prev_node}")
            # Loop to run for every vertex in the graph
            for vertex in range(self.vertex):
                weight = self.graph[current_node][vertex]
                print(weight)

                # If the weight is not zero, the vertex is not the previous node, and the
                # vertex has not been added to visited_nodes
                if weight != 0 and vertex != prev_node and vertex not in visited_nodes:
                    # If the minimum weight is zero, assign the weight to min_weight
                    if min_weight == 0:
                        min_weight = weight
                        next_node = vertex
                        prev_node = current_node
                        # print(min_weight, next_node)
                    # If the minimum weight is not zero and the min weight is less than 0
                    # set min_weight to weight
                    elif min_weight != 0 and weight < min_weight:
                        min_weight = weight
                        next_node = vertex
                        prev_node = current_node
                        # print(min_weight, next_node)
            # If min_weight is zero, move nodes
            if min_weight == 0:
                next_node = prev_node
            print(f"next node: {next_node}")
            print(f"shortest edge: {min_weight}")
            # If the current node is in unvisited_nodes, append it to visited_nodes
            # and remove it from unvisited_nodes
            if current_node in unvisited_nodes:
                visited_nodes.append(current_node)
                unvisited_nodes.remove(current_node)
            print(f"visted nodes: {visited_nodes}")
            print(f"unvisited nodes: {unvisited_nodes}")
            print(shortest_path)
            # For every node in unvisited nodes...
            for node in unvisited_nodes:
                # Get edge weight
                edge_weight = self.get_weights(current_node, node)
                # If the weight is not zero...
                if edge_weight != 0:
                    # If the current shortest path plus the edge weight is less than
                    # the current path, update the shortest path
                    if shortest_path[current_node] + edge_weight < shortest_path[node]:
                        shortest_path[node] = shortest_path[current_node] + edge_weight
            print(shortest_path)
            # Switch nodes
            current_node = next_node
        return shortest_path[end]


graph_1 = [
    [0, 2, 6, 0, 0, 0, 0],  # vertex 0
    [2, 0, 0, 5, 0, 0, 0],  # vertex 1
    [6, 0, 0, 8, 0, 0, 0],  # vertex 2
    [0, 5, 8, 0, 10, 15, 0],  # vertex 3
    [0, 0, 0, 10, 0, 6, 2],  # vertex 4
    [0, 0, 0, 15, 6, 0, 6],  # vertex 5
    [0, 0, 0, 0, 2, 6, 0],  # vertex 6
]  # vertex 6

# start_time = time.time()
print("Starting Time...")
g = Graph(graph_1)
p = g.dijkstra(0, 6)
g.visualize_graph()
# print(p)
print("About to end time")
# end_time = time.time()
print("Ending time...")
# total_time = end_time - start_time
print(f"Total Time: {time.time()}")
