def DFS(adj, disc, parent, color, finish):
    global time
    for v in adj.keys(): # Initializing the graph (coloring all vertices white).
        color[v] = 'white'
        parent[v] = None
    time = 0
    for v in adj.keys():
        if color[v] == 'white':
            DFSVisit(adj, disc, parent, color, finish, v)
            # Found an undiscovered vertex! It'll become the root of a new DFS tree.
    print('Graph explored.')

def DFSVisit(adj, disc, parent, color, finish, v):
    global time
    time += 1 # Global time is ticking...
    disc[v] = time # Recording time of discovery.
    color[v] = 'gray' # The vertex is now active.
    print('{} was discovered at time {}.'.format(v, time))
    for u in adj[v]: # Let's check v's neighbors (explore all edges that v is incident on).
        if color[u] == 'white': # Is this an undiscovered neighbor of v?
            parent[u] = v # v was the vertex that led us to u.
            print('Exploring edge ({}, {}).'.format(v, u))
            DFSVisit(adj, disc, parent, color, finish, u) # Let's focus on u and try to dig deeper.
    color[v] = 'black' # We're done with v...
    time += 1 # Global time is ticking again...
    finish[v] = time # Recording time of having finished with v.
    print('Finished with {} at time {}.'.format(v, time))



def main():
    adj = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['D', 'A', 'F', 'B'],
         'D': ['C', 'B'],
         'E': ['F'],
         'F': ['C', 'E']}
    disc = {x: None for x in adj.keys()}
    parent = disc.copy()
    color = disc.copy()
    finish = disc.copy()
    DFS(adj, disc, parent, color, finish)
    input()

if __name__ == '__main__':
    main()