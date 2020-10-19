from hash_table import HashTable
from package import Package
from graph import Graph, Vertex

hashTable = HashTable()
package1 = Package(1, 'asdf', 'now', 'here', 9, 9, 'in route')

graph = Graph()
vertex1 = Vertex('vertex1')
vertex2 = Vertex('vertex2')
vertex3 = Vertex('vertex3')
vertex4 = Vertex('vertex4')

graph.add_vertex(vertex1)
graph.add_vertex(vertex2)
graph.add_vertex(vertex3)
graph.add_vertex(vertex4)
graph.add_undirected_edge(vertex1, vertex2)
graph.add_undirected_edge(vertex1, vertex3, 2)
graph.add_undirected_edge(vertex3, vertex4)
graph.add_undirected_edge(vertex2, vertex4)


def dijkstra_shortest_path(graph, start_vertex):
    unvisited_vertecies = []
    print(type(graph.adjacency_list))
    for current_vertex in graph.adjacency_list:
        unvisited_vertecies.append(current_vertex)

    start_vertex.distance = 0

    while len(unvisited_vertecies) > 0:
        smallest_index = 0

        for i in range(1, len(unvisited_vertecies)):
            if unvisited_vertecies[i].distance < unvisited_vertecies[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_vertecies.pop(smallest_index)

        for adjacent_vertex in graph.adjacency_list.find(current_vertex):
            edge_weight = graph.edge_weights.find(
                (current_vertex, adjacent_vertex))
            alternative_path_distance = current_vertex.distance + edge_weight

            if alternative_path_distance < adjacent_vertex.distance:
                adjacent_vertex.distance = alternative_path_distance
                adjacent_vertex.predecessor_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    path = ''
    current_vertex = end_vertex
    path_length = 0

    while current_vertex is not start_vertex:
        path = ' -> ' + str(current_vertex.name) + path
        path_length += current_vertex.distance
        current_vertex = current_vertex.predecessor_vertex
    path = start_vertex.name + path
    return path + f'| Distance: {path_length}'


dijkstra_shortest_path(graph, vertex1)
print(get_shortest_path(vertex1, vertex4))
