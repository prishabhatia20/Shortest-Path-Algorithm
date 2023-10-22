"""
Summary of page
"""

import time
from shortest_path import Graph
#from dijkstar import Graph, find_path

def time_analysis(graph, source, end):
    """
    Doc String
    """
    graph_self = Graph(graph)
    time_self = get_average(graph_self, source,end)
    print(f"self dijkstar average time = {time_self}")


def get_average(graph, source, end):
    """
    Get the average time
    """
    time_sum = 0
    repetition = 3
    for _ in range(repetition):
        print(_)
        start_time = time.time()
        graph.dijkstra(source, end)
        end_time = time.time()
        total_time = end_time - start_time
        print(total_time)
        time_sum = total_time + time_sum
    average = time_sum/repetition
    return average



graph_1 = [
    [0, 2, 6, 0, 0, 0, 0],  # vertex 0
    [2, 0, 0, 5, 0, 0, 0],  # vertex 1
    [6, 0, 0, 8, 0, 0, 0],  # vertex 2
    [0, 5, 8, 0, 10, 15, 0],  # vertex 3
    [0, 0, 0, 10, 0, 6, 2],  # vertex 4
    [0, 0, 0, 15, 6, 0, 6],  # vertex 5
    [0, 0, 0, 0, 2, 6, 0],  # vertex 6
]  # vertex 6
g = Graph(graph_1)
start_time = time.time()
p = g.dijkstra(0, 6)
end_time = time.time()
total_time = end_time - start_time
print(f"Total Time: {total_time}")

time_analysis(graph_1, 0, 6)
