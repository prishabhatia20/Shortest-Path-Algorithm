"""
Timing analysis to compare to our dijkstra implementation to import libraries algorithms.
"""

import time
import dijkstar  # Graph, find_path
import scipy.sparse  # csr_matrix, csgraph.dijkstra
import shortest_path  # Graph

REPETITION = 30


def time_analysis(graph, source, end):
    """
    Print the time analysis of multiple implementations of dijkstra algorithm

    Args:
        graph: A adjacency matrix representing a graph weighted edges
        source: an integer representing the starting vertex
        end: an integer representing the ending vertex
    """
    graph_self = shortest_path.Graph(graph)
    graph_self.visualize_graph()
    time_self = get_average_self(graph_self, source, end)
    time_dijkstar = get_average_dijkstar(graph, source, end)
    time_scipy = get_average_scipy(graph, source, end)

    print(f"self dijkstar average time = {time_self}")
    print(f"dijkstar dijkstar average time = {time_dijkstar}")
    print(f"Scipy dijkstar average time = {time_scipy}")


def get_average_self(graph, source, end):
    """
    Get the average time from implemented shortest path algorithm.
    """
    time_sum = 0
    for _ in range(REPETITION):
        start_time = time.time()
        graph.dijkstra(source, end)
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / REPETITION
    return average


def get_average_dijkstar(graph, source, end):
    """
    Get the average time for shortest path implemented by dijkstar library
    credit: https://pypi.org/project/Dijkstar/
    """
    time_sum = 0
    # Create graph
    graph_dijkstar = dijkstar.Graph()
    vertex = len(graph)
    for row in range(vertex):
        for column in range(vertex):
            edge_weight = graph[row][column]
            if edge_weight > 0:
                graph_dijkstar.add_edge(row, column, edge_weight)
    # Find path
    for _ in range(REPETITION):
        start_time = time.time()
        dijkstar.find_path(graph_dijkstar, source, end)
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / REPETITION
    return average


def get_average_scipy(graph, source, end):
    """
    Get the average time
    """
    time_sum = 0
    # Create graph
    graph_scipy = scipy.sparse.csr_matrix(graph)
    # Find path
    for _ in range(REPETITION):
        start_time = time.time()
        distance_matrix = scipy.sparse.csgraph.dijkstra(
            csgraph=graph_scipy, directed=False, indices=[source, end]
        )
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / REPETITION
    return average


six_nodes = [
    [0, 2, 6, 0, 0, 0, 0],  # vertex 0
    [2, 0, 0, 5, 0, 0, 0],  # vertex 1
    [6, 0, 0, 8, 0, 0, 0],  # vertex 2
    [0, 5, 8, 0, 10, 15, 0],  # vertex 3
    [0, 0, 0, 10, 0, 6, 2],  # vertex 4
    [0, 0, 0, 15, 6, 0, 6],  # vertex 5
    [0, 0, 0, 0, 2, 6, 0],  # vertex 6
]

nine_nodes = [
    [0, 15, 25, 0, 0, 0, 0, 0, 0],
    [15, 0, 0, 0, 10, 0, 0, 5, 25],
    [25, 0, 0, 10, 20, 0, 0, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0],
    [0, 10, 20, 0, 0, 10, 5, 0, 0],
    [0, 0, 0, 0, 10, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 15],
    [0, 25, 0, 0, 0, 0, 0, 15, 0],
]
sparse_graph = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 2, 10, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [1, 2, 0, 10, 0, 0, 0, 1],
    [1, 0, 5, 0, 0, 0, 1, 0],
]

large_halin_graph = [
    [0, 11, 7, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [11, 0, 11, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 11, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 42, 0, 0, 8, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 3, 1, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 9, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0, 7, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 7, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 10, 0, 0, 6, 0, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 10, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 5, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 1, 1, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 42, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 42, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 7, 0, 11],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 11, 0],
]
print("Seven Nodes:")
time_analysis(six_nodes, 0, 6)
print("Nine Nodes:")
time_analysis(nine_nodes, 0, 8)
print("Sparse Graph")
time_analysis(sparse_graph, 0, 4)
print("Large Halin Graph")
time_analysis(large_halin_graph, 0, 17)
