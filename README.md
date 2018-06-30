# graphs
Playing with graphs a little.
I used dicts to store graphs which is probably a popular choice, as the key-value structure is very intuitive.


BFSearch.py is breadth-first search. 
Briefly, you could say it divides the connected component that contains the source vertex into different tiers (that are sets of vertices), based on the distance from the source, then scans the tiers in ascending order. An important feature of this algorithm is that it calculates the shortest distances from the source vertex to all the others in the same connected component, which is theoretically proven.


DFSearch.py is depth-first search. It allows us to get a lot of information about the graph, and it can be used to topologically sort an acyclic oriented graph (these can be used, for example, to describe a sequence of events).
