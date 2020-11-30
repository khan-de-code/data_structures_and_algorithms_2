from __future__ import annotations
from hash_table import HashTable
from misc import IllegalArgumentError


class Vertex:
    name: str
    distance: float
    predecessor_vertex: Vertex

    def __init__(self, name: str):
        """Initializes the vertex object.

        Args:
            name (str): The name of the object.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        self.name = name
        self.distance = float('inf')
        self.predecessor_vertex = None

    def __str__(self):
        """The string retured for this object.

        Returns:
            str: The string for this object.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        return '{\n' + f'name: {self.name},\ndistance: {self.distance},\npredecessor_vertex: {self.predecessor_vertex}' + '\n}'


class Graph:
    adjacency_list: HashTable
    edge_weights: HashTable
    vertecies_in_graph: [Vertex]

    def __init__(self):
        """Initializes the graph object.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        self.adjacency_list = HashTable()
        self.edge_weights = HashTable()
        self.vertecies_in_graph = []

    def add_vertex(self, new_vertex_key: Vertex):
        """Adds a verted to the graph

        Args:
            new_vertex_key (Vertex): The vertex to add.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(N)
        """

        self.adjacency_list.add(new_vertex_key, [])
        self.vertecies_in_graph.append(new_vertex_key)

    def add_directed_edge(self, from_vertex_key: Vertex, to_vertex_key: Vertex, weight: float):
        """Adds a directed edge to the graph.

        Args:
            from_vertex_key (Vertex): The vertex from which the edge starts.
            to_vertex_key (Vertex): The vertex to which the edge ends.
            weight (float): The weight of the edge.

        Raises:
            IllegalArgumentError: Raises an error if the from vertex is not in the graph.
            IllegalArgumentError: Raises an error if the to vertex is not in the graph.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        if from_vertex_key not in self.vertecies_in_graph:
            raise IllegalArgumentError(
                f"'{from_vertex_key.name}' does not exist in the graph")
        elif to_vertex_key not in self.vertecies_in_graph:
            raise IllegalArgumentError(
                f"'{to_vertex_key.name}' does not exist in the graph")

        self.edge_weights.add((from_vertex_key, to_vertex_key), weight)
        self.adjacency_list.find(from_vertex_key).append(to_vertex_key)

    def add_undirected_edge(self, vertex_a: Vertex, vertex_b: Vertex, weight=1.0):
        """Adds an undirected edge to the graph.

        Args:
            vertex_a (Vertex): One vertex for the edge.
            vertex_b (Vertex): The other vertex for the edge.
            weight (float, optional): The weight of the edge. Defaults to 1.0.

        Space & Time Complexity:
            Time Complexity:
                Big-O(1)
            Space Complexity:
                Big-O(1)
        """

        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
