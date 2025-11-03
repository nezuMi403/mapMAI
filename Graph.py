'''S_(адрес)_GV_(здание)_3_(этаж)_k_(тип)_209(номер каб)
SGV_3_k_209
____________
Adresses:
S - Стрешнево
O - Оршанка

Korpuses:
1 10 11 12 14 15 16 18 19 2 21 22 24A 24B 24V 2A 2V 3 35 4 5 57 59 60 7 70 79 82 9 DK GAK GUKA GUKB GUKV

floors: int 1...n

Types:
k - kabinet
f - food
a - aud
l - ladder
e - elevator
t - toilet
i - input
p - point
o - others

Kabinets: int / -1 - like Teremok
'''
import sys
from pprint import pprint

korpuses = ['1', '10', '11', '12', '14', '15', '16', '18', '19', '2', '21', '22', '24A', '24B', '24V', '2A', '2V', '3',
            '35', '4', '5', '57', '59', '60', '7', '70', '79', '82', '9', 'DK', 'GAK', 'GUKA', 'GUKB', 'GUKV']

korpuses_tmp = ['GUKA', 'GUKB', 'GUKV']
floors_tmp = {"GUK": 7}

add_graph = ["S_GA_2_k_(200...214,216,218,200V)", "S_GA_2_p_(1...28)", "S_GA_2_e_(1...4)", "S_GA_2_l_1U",
             "S_GA_2_l_1D", "S_GA_2_l_2U", "S_GA_2_l_2D", "S_GA_2_l_3D", "S_GA_2_l_3U"]
add_points = {""}


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def give_graph(self):
        for i in sorted(self.graph.keys(), key=lambda x: x):
            print(f"\n{i}:")
            for j in sorted(self.graph[i].keys(), key=lambda x: x):
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


nodes = []


def add_to_nodes(l: list) -> None:
    global nodes
    for node in l:
        if "(" in node:
            do = node.split("(")[1].split(")")[0]
            sample_node = node.split("(")[0]
            for action in do.split(","):
                if "..." in action:
                    start, stop = map(int, action.split("..."))
                    for i in range(start, stop + 1):
                        nodes.append(sample_node + str(i))
                else:
                    nodes.append(sample_node + action)
        else:
            nodes.append(node)


def initialization_graph(init_str: str) -> dict:
    # Add connections, described in init_str to the init graph, initializated with [] for elems in nodes
    global nodes

    init_graph = {i: {} for i in nodes}
    pref = init_str.split("|")[0]
    add_connections = init_str.split("|")[1].split(",")

    for i in add_connections:
        where_to_add = i.split("-")[0]
        elems_add = i.split("-")[1].split("/")
        point = pref + where_to_add[0] + "_" + where_to_add[1:]
        for elem in elems_add:
            point_reverse = pref + elem[0] + "_" + elem[1:]
            init_graph[point][point_reverse] = 1
            init_graph[point_reverse][point] = 1

    return init_graph


init_graph_connections = "S_GA_2_|p24-p23,p23-k200/p22,p22-k200V/p10,p10-p9/p11/p18,p9-l1U/l1D/p8,p8-k207/p7,p7-k212/p6,p6-k209/p5,p5-k214/p4,p4-k211/p3,p3-k216/p2,p2-p1/k213,p1-k218,p11-l2U/l2D/p12,p12-k210/p13,p13-k205/k208/p14,p14-p15/k203/k206,p15-p16/k204,p16-p17/k201,p17-k202/l3U/l3D,p18-p26/p28/p19,p26-e3,p28-e4,p25-e1,p27-e2,p19-p25/p20/p27,p20-p21"
add_to_nodes(add_graph)
print(nodes)
init_graph = initialization_graph(init_graph_connections)
pprint(init_graph, width=1000, depth=3)

graph = Graph(nodes, init_graph)

start = input("Input number: ")
end = input("Output number: ")

print(graph.get_nodes())
graph.give_graph()
print(graph.get_outgoing_edges(start))
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start)

print_result(previous_nodes, shortest_path, start_node=start, target_node=end)
