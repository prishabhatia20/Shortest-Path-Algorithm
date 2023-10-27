"""
Testing cases to test accuracy of our shortest path algorithm.
"""
from shortest_path import Graph


def test_cycle_adjacent():
    """
    Test that two adjacent vertex in a cycle graph have a shortest
    distance of the edge connecting them
    """
    test_graph = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 4)
    assert shortest_path == 1


def test_cycle_across():
    """
    Test that shortest path in a cycle graph choses the best
    path even if it is the second path.
    """
    # cycle edge case
    test_graph = [
        [0, 3, 0, 0, 0, 7],
        [3, 0, 4, 0, 0, 0],
        [0, 4, 0, 6, 0, 0],
        [0, 0, 6, 0, 1, 0],
        [0, 0, 0, 1, 0, 3],
        [7, 0, 0, 0, 3, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 3)
    assert shortest_path == 11

    # simple cycle
    # Graph credit:
    # https://reginafurness.medium.com/representing-a-weighted-graph-with-an-adjacency-matrix-in-javascript-8a803bfbc36f
    test_graph_simple = [[0, 2, 3, 0], [2, 0, 0, 2], [3, 0, 0, 6], [0, 2, 6, 0]]
    test = Graph(test_graph_simple)
    shortest_path = test.dijkstra(0, 3)
    assert shortest_path == 4


def test_complete_graph():
    """
    Test that a complete path picks a shortest.
    """
    test_graph = [
        [0, 1, 2, 4, 6],
        [1, 0, 3, 5, 1],
        [2, 3, 0, 6, 7],
        [4, 5, 6, 0, 9],
        [6, 1, 7, 9, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 3)
    assert shortest_path == 4


def test_sparse_graph():
    """
    Test that a sparse graph picks the shortest path
    """
    test_graph = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 2, 10, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [1, 2, 0, 10, 0, 0, 0, 1],
        [1, 0, 5, 0, 0, 0, 1, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 4)
    assert shortest_path == 15


def test_one_node():
    """
    Test that a graph with a single node to itself is 0.
    """
    test_graph = [[0]]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 0)
    assert shortest_path == 0


def test_two_nodes():
    """
    Test that a graph with two nodes, the shortest path is the weight
    of edge connecting them.
    """
    test_graph = [[0, 3], [3, 0]]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 1)
    assert shortest_path == 3


def test_nine_nodes():
    """
    Test a larger graph with nine nodes.
    Graph Credit: https://courses.cs.vt.edu/~cs3114/Fall10/Notes/T22.WeightedGraphs.pdf
    """
    test_graph = [
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
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 8)
    assert shortest_path == 35


def test_connected_nodes():
    """
    Test graph with multiple connections.
    Graph Credit: https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/
    """
    test_graph = [
        [0, 3, 0, 7, 8],
        [3, 0, 1, 4, 0],
        [0, 1, 0, 2, 0],
        [7, 4, 2, 0, 3],
        [8, 0, 0, 3, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 2)
    assert shortest_path == 4


def test_cycle_with_bridge():
    """
    Test a cycle graph with a single bridge.
    """
    test_graph = [
        [0, 1, 7, 4, 0, 0],
        [1, 0, 2, 0, 0, 0],
        [7, 2, 0, 0, 0, 3],
        [4, 0, 0, 0, 5, 0],
        [0, 0, 0, 5, 0, 6],
        [0, 0, 3, 0, 6, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 5)
    assert shortest_path == 6


def test_halin_graph():
    """
    Test large Halin graph with 20 nodes.
    Created with https://graphonline.ru/en/?graph=HalinGraph
    """
    test_graph = [
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
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 17)
    assert shortest_path == 23
