from __future__ import annotations
from hash_table import HashTable


class Vertex:
    name: str
    distance: float
    predecessor_vertex: Vertex

    def __init__(self, name: str):
        self.name = name
        self.distance = float('inf')
        self.predecessor_vertex = None


class Graph:
    adjacency_list: HashTable
    edge_weights: HashTable

    def __init__(self):
        self.adjacency_list = HashTable()
        self.edge_weights = HashTable()

    def add_vertex(self, new_vertex_key):
        self.adjacency_list.add(new_vertex_key, [])

    def add_directed_edge(self, from_vertex_key, to_vertex_key, weight=1.0):
        self.edge_weights.add((from_vertex_key, to_vertex_key), weight)
        self.adjacency_list.find(from_vertex_key).append(to_vertex_key)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
