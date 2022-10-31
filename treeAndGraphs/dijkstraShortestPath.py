# dijkstra shortest path algorithm
# theory:
# create a distance array
# create a visited array
# create a parent array
# add the root to the distance array
# add the root to the visited array
# add the root to the parent array
# while the visited array is not empty
# find the node with the smallest distance
# remove the node from the visited array
# for each neighbor of the node
# if the distance to the neighbor is greater than the distance to the node plus the distance from the node to the neighbor
# update the distance to the neighbor
# update the parent of the neighbor
# return the distance array

def dijkstra(graph, root):
    # create a distance array
    distance = {}
    # create a visited array
    visited = []
    # create a parent array
    parent = {}
    # add the root to the distance array
    distance[root] = 0
    # add the root to the visited array
    visited.append(root)
    # add the root to the parent array
    parent[root] = None
    # while the visited array is not empty
    while len(visited) > 0:
        # find the node with the smallest distance
        node = min(visited, key=lambda x: distance[x])
        # remove the node from the visited array
        visited.remove(node)
        # for each neighbor of the node
        for neighbor in graph[node]:
            # if the distance to the neighbor is greater than the distance to the node plus the distance from the node to the neighbor
            if neighbor not in distance or distance[neighbor] > distance[node] + graph[node][neighbor]:
                # update the distance to the neighbor
                distance[neighbor] = distance[node] + graph[node][neighbor]
                # update the parent of the neighbor
                parent[neighbor] = node
                # add the neighbor to the visited array
                visited.append(neighbor)
    # return the distance array
    return distance

def main():
    # create a graph
    graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'D': 2, 'E': 4},
        'C': {'F': 3},
        'D': {},
        'E': {'F': 1},
        'F': {}
    }
    # call dijkstra
    print(dijkstra(graph, 'A'))

if __name__ == '__main__':
    main()