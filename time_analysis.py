"""
Timing analysis to compare to our dijkstra implementation to import libraries algorithms.
"""

import time
import shortest_path  # Graph
import dijkstar  # Graph, find_path
import scipy.sparse #csr_matrix, csgraph.dijkstra

REPETITION = 10 

def time_analysis(graph, source, end):
    """
    Print the time analysis of multiple implementations of dijkstra algorithm

    Args:
        graph: A adjacency matrix representing a graph weighted edges
        source: an integer representing the starting vertex
        end: an integer representing the ending vertex
    """
    graph_self = shortest_path.Graph(graph)
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
    repetition = 10
    for _ in range(repetition):
        start_time = time.time()
        graph.dijkstra(source, end)
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / repetition
    return average

def get_average_dijkstar(graph, source, end):
    """
    Get the average time for shortest path implemented by dijkstar library
    credit: https://pypi.org/project/Dijkstar/
    """
    time_sum = 0
    #Create graph
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
    #Create graph
    graph_scipy = scipy.sparse.csr_matrix(graph)
    # Find path
    for _ in range(REPETITION):
        start_time = time.time()
        distance_matrix = scipy.sparse.csgraph.dijkstra(csgraph=graph_scipy, directed=False, indices=[source,end])
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / REPETITION
    return average

graph_1 = [
    [0, 2, 6, 0, 0, 0, 0],  # vertex 0
    [2, 0, 0, 5, 0, 0, 0],  # vertex 1
    [6, 0, 0, 8, 0, 0, 0],  # vertex 2
    [0, 5, 8, 0, 10, 15, 0],  # vertex 3
    [0, 0, 0, 10, 0, 6, 2],  # vertex 4
    [0, 0, 0, 15, 6, 0, 6],  # vertex 5
    [0, 0, 0, 0, 2, 6, 0],  # vertex 6
]  


time_analysis(graph_1, 0, 6)
