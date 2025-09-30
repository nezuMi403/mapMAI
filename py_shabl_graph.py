import sys


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def give_graph(self):
        for i in sorted(self.graph.keys(), key=lambda x: int(x)):
            print(f"\n{i}:")
            for j in sorted(self.graph[i].keys(), key=lambda x: int(x)):
                print(f"|---{j}\t{self.graph[i][j]}")

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes

    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}  # для сохранения пути

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print("\nНайден следующий лучший маршрут с длиной {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


nodes = [str(i) for i in range(1, 22)]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["1"]["2"] = 1
init_graph["2"]["4"] = 5
init_graph["2"]["3"] = 4
init_graph["2"]["5"] = 3
init_graph["5"]["6"] = 3
init_graph["6"]["21"] = 3
init_graph["21"]["8"] = 2
init_graph["6"]["7"] = 1
init_graph["3"]["7"] = 4
init_graph["7"]["11"] = 7
init_graph["7"]["9"] = 3
init_graph["9"]["10"] = 4
init_graph["9"]["12"] = 3
init_graph["12"]["13"] = 1
init_graph["12"]["14"] = 5
init_graph["14"]["19"] = 1
init_graph["14"]["18"] = 2
init_graph["14"]["15"] = 6
init_graph["15"]["20"] = 1
init_graph["15"]["16"] = 6
init_graph["16"]["17"] = 6

graph = Graph(nodes, init_graph)

start = input("Input number: ")
end = input("Output number: ")

# print(graph.get_nodes())
# graph.give_graph()
# print(graph.get_outgoing_edges("3"))
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start)

print_result(previous_nodes, shortest_path, start_node=start, target_node=end)
