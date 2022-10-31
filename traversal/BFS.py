# Breadth first search
# theory:
# create a queue
# add the root to the queue
# while the queue is not empty
# remove the first element from the queue
# add the children of the element to the queue

def bfs(graph, root):
    # create a queue
    queue = []
    # add the root to the queue
    queue.append(root)
    # while the queue is not empty
    while len(queue) > 0:
        # remove the first element from the queue
        node = queue.pop(0)
        # add the children of the element to the queue
        for child in graph[node]:
            queue.append(child)
        print(node)

def main():
    # create a graph
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    # call bfs
    bfs(graph, 'A')

if __name__ == '__main__':
    main()