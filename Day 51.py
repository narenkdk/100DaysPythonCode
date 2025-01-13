#Day 51 - Graphs


#Implement a graph data structure.

class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a vertex if it doesn't already exist
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, bidirectional=True):
        # Add an edge between vertex1 and vertex2
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        # Add the edge
        self.adjacency_list[vertex1].append(vertex2)
        
        # If the graph is bidirectional, add the reverse edge
        if bidirectional:
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2, bidirectional=True):
        # Remove an edge between vertex1 and vertex2
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
        if bidirectional and vertex2 in self.adjacency_list and vertex1 in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        # Remove the vertex and all its edges
        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent].remove(vertex)
            del self.adjacency_list[vertex]

    def display(self):
        # Display the adjacency list
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex} -> {edges}")

# Example usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.display()

# Output:
# A -> ['B', 'C']
# B -> ['A', 'D']
# C -> ['A']
# D -> ['B']
