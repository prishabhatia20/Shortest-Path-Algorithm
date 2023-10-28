# Shortest-Path-Algorithm

## Introduction
Shortest path algorithms are algorithms that search for the shortest path between given nodes, taking into account the costs of taking different paths. These algorithms operate on an input graph G, which has V vertices and E edges. If the edges have weights, the graph is called a weighted graph. In our case, all the edges have weights. These edges can be bidirectional, creating what is called an undirected graph. There can be cycles in the graph, among other complexities. These complexities make a significant difference in what algorithms are best for a certain type of graph (Chumbley). There are many different types of shortest path algorithms, such as the A* Algorithm, the Bellman-Ford Algorithm, Dijkstra’s Algorithm, and more (Shortest Paths). The focus of our project is to code and analyze Dijkstra’s Algorithm. According to Dijkstra, this algorithm was a 20-minute invention that began with the question, “What’s the shortest way to travel from Rotterdam to Groningen?” (Navone). We are excited to be able to answer this question using Dijkstra’s methods. Dijkstra’s Algorithm is a breadth-first search shortest path algorithm that only works on positive weighted graphs. Finding the shortest path between two points has applications in computer networks and map systems.

## Project Description
Our goal is to implement Dijkstra’s algorithm in Python from scratch. We have used our prior coding knowledge along with the pseudocode in the Discrete Mathematics and Its Applications by Kenneth H. Rosen textbook to write an algorithm that we feel is efficient. We will then analyze how the speed and optimization compares to other already made algorithm implementations to deepen our understanding of this algorithm; it will force us to think about the design choices we used when writing our implementation and allow us to learn ways to write more efficient and optimal code.

## How the Program Works
We created a Graph class that is able to read an adjacency matrix and extract the number of nodes within the graph as well as the weights between any two nodes. This class includes a function called dijkstra() that has the source node and the destination node as its parameters, then outputs the length of the shortest path between the two points. The algorithm then outputs a visualization of the graph with labeled nodes and weights.

## Sources
Chumbley, Alex. “Shortest Path Algorithms.” Brilliant Math & Science Wiki, Brilliant , brilliant.org/wiki/shortest-path-algorithms/. Accessed 12 Oct. 2023.
Navone, Estefania Cassingena. “Dijkstra’s Shortest Path Algorithm - a Detailed and Visual Introduction.” freeCodeCamp.Org, freeCodeCamp.org, 3 Feb. 2022, www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/.
“Shortest Paths.” Shortest Paths, Discrete Mathematics, Optimization, and Convexity Department of Mathematics Technical University of Munich, algorithms.discrete.ma.tum.de/spp/#:~:text=Dijkstra’s%20Algorithm%20computes%20the%20shortest,adge%20weights%20are%20non%2Dnegative. Accessed 12 Oct. 2023. 
Rosen, Kenneth H. Discrete mathematics and its applications. The McGraw Hill Companies, 2007.

