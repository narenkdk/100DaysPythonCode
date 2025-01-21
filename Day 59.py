#Day 59: Breadth-first search (BFS) algorithm


#Implement a breadth-first search (BFS) algorithm.

from collections import deque

def bfs(graph, start):
    """
    Perform a breadth-first search on a graph.

    Parameters:
        graph (dict): A dictionary representing the graph where keys are nodes
                      and values are lists of neighboring nodes.
        start (any): The starting node for the BFS.

    Returns:
        list: A list of nodes in the order they are visited.
    """
    visited = set()       # To keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node
    traversal = []        # To store the order of traversal

    while queue:
        node = queue.popleft()  # Remove and return the leftmost element in the queue

        if node not in visited:
            visited.add(node)    # Mark the node as visited
            traversal.append(node)  # Add to the traversal order

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node = 'A'
print("BFS Traversal:", bfs(graph, start_node))
