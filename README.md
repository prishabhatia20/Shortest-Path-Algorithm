# Shortest-Path-Algorithm

## Introduction
Shortest path algorithms are algorithms that search for the shortest path between given nodes, taking into account the costs of taking different paths. These algorithms operate on an input graph G, which has V vertices and E edges. If the edges have weights, the graph is called a weighted graph. In our case, all the edges have weights. These edges can be bidirectional, creating what is called an undirected graph. There can be cycles in the graph, among other complexities. These complexities make a significant difference in what algorithms are best for a certain type of graph (Chumbley). There are many different types of shortest path algorithms, such as the A* Algorithm, the Bellman-Ford Algorithm, Dijkstra’s Algorithm, and more (Shortest Paths). The focus of our project is to code and analyze Dijkstra’s Algorithm. According to Dijkstra, this algorithm was a 20-minute invention that began with the question, “What’s the shortest way to travel from Rotterdam to Groningen?” (Navone). We are excited to be able to answer this question using Dijkstra’s methods. Dijkstra’s Algorithm is a breadth-first search shortest path algorithm that only works on positive weighted graphs. Finding the shortest path between two points has applications in computer networks and map systems.

## Project Description
Our goal is to implement Dijkstra’s algorithm in Python from scratch. We have used our prior coding knowledge along with the pseudocode in the Discrete Mathematics and Its Applications by Kenneth H. Rosen textbook to write an algorithm that we feel is efficient. We will then analyze how the speed and optimization compares to other already made algorithm implementations to deepen our understanding of this algorithm; it will force us to think about the design choices we used when writing our implementation and allow us to learn ways to write more efficient and optimal code.

We also made a visual representation of our project linked [here](https://www.canva.com/design/DAFx1Y7cJs0/_S5V7FahvZE7nDPIxJW7Yg/view?utm_content=DAFx1Y7cJs0&utm_campaign=designshare&utm_medium=link&utm_source=editor).

## How the Program Works
We created a Graph class that is able to read an adjacency matrix and extract the number of nodes within the graph as well as the weights between any two nodes. This class includes a function called dijkstra() that has the source node and the destination node as its parameters, then outputs the length of the shortest path between the two points. The algorithm then outputs a visualization of the graph with labeled nodes and weights.

## Timing Optimization Results
We compared our algorithm to an already-made Dikjstra library and a SciPy library.
![image](https://github.com/prishabhatia20/Shortest-Path-Algorithm/assets/67985548/e5aa6350-63f8-4f4f-be73-20ae719dc37a)

The percentages were created by Time/Self_Time * 100. For example, for the first row, if we set the standard so that our own algorithm operates at a time that represents 100%, then Dikjstra takes only 29.8% of that time and SciPy takes 788.0% of that time. In conclusion, the Dijkstra library operates more quickly than our algorithm, but SciPy was much slower though timing was reduced as the graph size increased.

The raw output from the time anaylsis function is below.

```
Seven Nodes:
self dijkstar average time = 1.220703125e-05
dijkstar dijkstar average time = 3.631909688313802e-06
Scipy dijkstar average time = 9.618600209554037e-05
Nine Nodes:
self dijkstar average time = 2.0694732666015624e-05
dijkstar dijkstar average time = 4.00543212890625e-06
Scipy dijkstar average time = 5.9262911478678385e-05
Sparse Graph
self dijkstar average time = 1.6927719116210938e-05
dijkstar dijkstar average time = 3.933906555175781e-06
Scipy dijkstar average time = 5.9096018473307293e-05
Large Halin Graph
self dijkstar average time = 8.931159973144532e-05
dijkstar dijkstar average time = 9.632110595703125e-06
Scipy dijkstar average time = 5.980332692464193e-05
```

NOTE: Timings differ slightly based on what computer the code is run on.

## Dependencies
In order to run this algorithm, you need to install the following libraries.
- time
- dijkstar 
- scipy
- math
- networkx
- matplotlib

## Source Image Links for Graphs
These graphs were used in our test cases.

Simple Graph: https://reginafurness.medium.com/representing-a-weighted-graph-with-an-adjacency-matrix-in-javascript-8a803bfbc36f

Large Graph with Nine Nodes: https://courses.cs.vt.edu/~cs3114/Fall10/Notes/T22.WeightedGraphs.pdf

Connected Nodes: https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/

Cycle with Bridge: http://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/shortest-path.pdf

## Sources
Baldwin, Wyatt. “Dijkstar · PyPI.” PyPI, https://pypi.org/project/Dijkstar/. Accessed 27 October 2023.

Chumbley, Alex. “Shortest Path Algorithms.” Brilliant Math & Science Wiki, Brilliant , brilliant.org/wiki/shortest-path-algorithms/. Accessed 12 Oct. 2023.

Navone, Estefania Cassingena. “Dijkstra’s Shortest Path Algorithm - a Detailed and Visual Introduction.” freeCodeCamp.Org, freeCodeCamp.org, 3 Feb. 2022, www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/.

“Shortest Paths.” Shortest Paths, Discrete Mathematics, Optimization, and Convexity Department of Mathematics Technical University of Munich, algorithms.discrete.ma.tum.de/spp/#:~:text=Dijkstra’s%20Algorithm%20computes%20the%20shortest,adge%20weights%20are%20non%2Dnegative. Accessed 12 Oct. 2023. 

Rosen, Kenneth H. Discrete mathematics and its applications. The McGraw Hill Companies, 2007.

“python - Labeling edges in networkx.” Stack Overflow, 3 November 2017, https://stackoverflow.com/questions/47094949/labeling-edges-in-networkx. Accessed 25 October 2023.

scipy.sparse.csgraph.dijkstra — SciPy v1.11.3 Manual, https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html. Accessed 27 October 2023.

Special thanks to Sarah and our CAs Alex, Isa, Cherry, and Jess for helping us with this implementation. 

