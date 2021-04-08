# A* path finding algorithm with visualization
## General info
Based on [Tech With Tim video](https://www.youtube.com/watch?v=JtiK0DOeI4A), I've coded along video to grasp how the A* algorithm works, and the cool way of visualizing it using pygame.

>A* is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.
[A* algorithm Wiki](https://en.wikipedia.org/wiki/A*_search_algorithm)

This is the final result.

![alt text](https://github.com/SSketcher/Python---Scripts/blob/master/Astar_path_finding_algorithm_with_visualization/pathfinding.PNG?raw=true)

Orange square and turquois square are respectively start and finish nodes. Black lines are barriers of the "maze". The red and green squares are results of the algorithm analyzing the "maze", the red squares represent nodes closed set of fully explored nodes, and the green ones represent open set of nodes for possible further exploration (at the time of algorithm working). A purple path is the shortest path from start to finish, that the algorithm established.

## Technologies
* Python 3.7.3

Libraries:
* pygame
* math
* queue

## Sources and helpful materials
[A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A)

[A* algorithm Wiki](https://en.wikipedia.org/wiki/A*_search_algorithm)
