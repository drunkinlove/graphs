def BFS(adj, dist, parent, color, source):
    for v in adj.keys():
        color[v] = 'white'
        dist[v] = float('Inf')
        parent[v] = None
    color[source] = 'gray'
    dist[source] = 0
    parent[source] = None
    Q = [] # This is a queue
    Q.append(source)
    while Q:
        u = Q.pop(0) # Get the next vertex from queue, u
        print('Initialized {}. Its neighbors include {}.'.format(u, ', '.join(adj[u])))
        for v in adj[u]: # For every vertex that's adjacent to u...
            if color[v] == 'white': # If it hasn't already been discovered...
                color[v] = 'gray' # Mark it as an 'active' vertex
                dist[v] = dist[u] + 1 # It should be one edge farther from u
                parent[v] = u # And the vertex that led us to v is u.
                print('Discovered {}, distance to {} is {}, parent is {}.'.format(v, source, dist[v], parent[v]))
                Q.append(v) # Enqueue v to check its neighbors once we're done with this tier.
        color[u] = 'black' # Once we've checked all of u's neighbors, it's now both discovered and inactive.
    print('Graph explored.')

     
def main():
    adj = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['D', 'A', 'F', 'B'],
         'D': ['C', 'B'],
         'E': ['F'],
         'F': ['C', 'E']}
    dist = {x: None for x in adj.keys()}
    parent = dist.copy()
    color = dist.copy()
    BFS(adj, dist, parent, color, 'B')
    input()

if __name__ == '__main__':
    main()
