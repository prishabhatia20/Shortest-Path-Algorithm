"""
Implementation of Dijkstra Algorithm using Textbook Pseudo code 
"""
import math
import networkx as nx
import matplotlib.pyplot as plt
import time


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
                if edge_weight > 0:
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
        graph_time = time.time()
        graph_time = str(graph_time)[-4:]
        plt.show(block=False)
        plt.savefig(f"Graphs/graph_{graph_time}.PNG", format="PNG")

    def dijkstra(self, source, end):
        """
        Dijkstra algorithm that finds the shortest path from one vertex
        to another given all weights assigned to edges

        Args:
            self: an instance of the Graph class
            source: an integer representing the starting vertex
            end: an integer representing the ending vertex
        """

        visited_nodes = []
        unvisited_nodes = []

        # Append all nodes to unvisited list
        for i in range(self.vertex):
            unvisited_nodes.append(i)
            current_node = source

        # Create a list with the source and infinities
        shortest_path = [self.INF] * self.vertex
        shortest_path[source] = 0

        while end not in visited_nodes:
            min_value = self.INF
            min_value_index = None
            min_weight = 0
            for i, dist_value in enumerate(shortest_path):
                if dist_value < min_value and i not in visited_nodes:
                    min_value = dist_value  # length of shortest path neighbor
                    min_value_index = i  # index of shortest path neighbor
            for vertex in range(self.vertex):
                # Find the smallest weight within the row of the next node
                weight = self.graph[min_value_index][vertex]
                if weight != 0:
                    min_weight = weight
                elif min_weight != 0 and weight < min_weight:
                    min_weight = weight
            # Add current node to visited nodes list and remove it from unvisited nodes list
            if current_node in unvisited_nodes:
                visited_nodes.append(current_node)
                unvisited_nodes.remove(current_node)
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
            # Go to the next node
            current_node = min_value_index
            print(f"Shortest path: {shortest_path[end]}")
        return shortest_path[end]
