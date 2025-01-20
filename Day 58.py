#Day 58: Depth-first search (DFS) algorithm



#Implement a depth-first search (DFS) algorithm.

def dfs_recursive(graph, node, visited):
   if node not in visited:
      visited.add(node)
      print(node, end=" ") #process the node
      for neighbour in graph[node]:
         dfs_recursive(graph, neighbour, visited)


#DEF using a stack(interative)

def dfs_iterative(graph, start):
   visited = set()
   stack = [start]
   while stack:
      node = stack.pop()
      if node not in visited:
         print(node, end=" ") #process the node
         stack.extend(reversed(graph[node])) #Add neighbours to the stack




#Example graph represented as an adjacency list
graph = {
   'A': ['B', 'C'],
   'B': ['D', 'E'],
   'C': ['F'],
   'D': [],
   'E': ['F'],
   'F': []
}

#Perform DFS starting from node 'A'
print("DFS (recursive):")
dfs_recursive(graph, 'A', set())

print("\nDFS (iterative):")
dfs_iterative(graph, 'A')
