"""
Testing Function
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
    Test that shortest path in a cycle graph choses the second path.
    Limitation of algorithm.
    """
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


def test_complete_graph():
    pass


def test_sparse_graph():
    test_graph = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 2, 10, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [1, 0, 5, 0, 0, 0, 1, 0],
    ]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 5)
    assert shortest_path == 15


def test_one_node():
    test_graph = [[0]]
    test = Graph(test_graph)
    shortest_path = test.dijkstra(0, 0)
    assert shortest_path == 0


def test_two_node():
    pass
