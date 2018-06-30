# graphs
Playing with graphs a little.
I used dicts to store graphs which is probably a popular choice, as the key-value structure is very intuitive.

BFSearch.py is breadth-first search. 
Briefly, you could say it divides the connected component that contains the source vertex into different tiers (that are sets of vertices), based on the distance from the source, then scans the tiers in ascending order. An important feature of this algorithm is that it calculates the shortest distances from the source vertex to all the others in the same connected component, which is theoretically proven.
