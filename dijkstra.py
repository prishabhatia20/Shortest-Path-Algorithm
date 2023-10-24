import math

class Graph:
  INF = math.inf

  def __init__(self,graph):
    self.graph = graph
    self.vertex = len(graph)

  def get_weights(self, vi, vj):
    weight = self.graph[vi][vj]
    return weight
  def dijkstra(self, source, end):
    visited_nodes = []
    unvisited_nodes = []

    # Append all nodes to unvisited list
    for i in range(self.vertex):
      unvisited_nodes.append(i)
      current_node = source

    # Create list of infinities
    shortest_path = [self.INF]*self.vertex
    shortest_path[source] = 0

    while end not in visited_nodes:
      min_value = self.INF
      min_value_index = None
      min_weight = 0
      for i, dist_value in enumerate(shortest_path):
        if dist_value < min_value and i not in visited_nodes:
          min_value = dist_value    # length of shortest path neighbor
          min_value_index = i       # index of shortest path neighbor
      for vertex in range(self.vertex):
          # Find the smallest weight within the row of the next node
          weight = self.graph[min_value_index][vertex]
          if weight != 0:
              min_weight = weight
          elif min_weight != 0 and weight < min_weight:
              min_weight = weight
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
      # Switch nodes
      current_node = min_value_index
      print(f'Shortest path: {shortest_path[end]}')
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
      
test_graph = [
    [0, 3, 0, 0, 0, 7],
    [3, 0, 4, 0, 0, 0],
    [0, 4, 0, 6, 0, 0],
    [0, 0, 6, 0, 1, 0],
    [0, 0, 0, 1, 0, 3],
    [7, 0, 0, 0, 3, 0],
]

# g = Graph(test_graph)
g = Graph(graph_1)
p = g.dijkstra(0, 5)

