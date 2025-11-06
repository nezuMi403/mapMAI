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
b - bosses of MAI
h - hall

Kabinets: int / -1 - like Teremok
'''
import sys
from pprint import pprint

korpuses = ['1', '10', '11', '12', '14', '15', '16', '18', '19', '2', '21', '22', '24A', '24B', '24V', '2A', '2V', '3',
            '35', '4', '5', '57', '59', '60', '7', '70', '79', '82', '9', 'DK', 'GAK', 'GUKA', 'GUKB', 'GUKV']

korpuses_tmp = ['GUKA', 'GUKB', 'GUKV']
floors_tmp = {"GUK": 7}

add_graph = ["S_GA_2_k_(200...214,216,218,200V)", "S_GA_2_p_(1...28)", "S_GA_2_e_(1...4)", "S_GA_2_l_1U",
             "S_GA_2_l_1D", "S_GA_2_l_2U", "S_GA_2_l_2D", "S_GA_2_l_3D", "S_GA_2_l_3U", "S_GA_3_l_1U", "S_GA_3_l_5U",
             "S_GA_3_l_5D", "S_GA_3_l_1D", "S_GA_3_l_2U", "S_GA_3_l_2D", "S_GA_3_l_3U", "S_GA_3_l_3D", "S_GA_3_l_4U",
             "S_GA_3_l_4D", "S_GA_3_p_(1...39)", "S_GA_3_k_(1...15,12A,12B)", "S_GA_3_h_1l", "S_GA_3_h_1r",
             "S_GA_3_a_300", "S_GA_3_b_15", "S_GA_3_e_(1...4)", "S_GA_2_l_4U", "S_GA_2_l_4D", "S_GA_2_l_5D",
             "S_GA_2_l_5U"]
add_points = {}
nodes = []


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


def dijkstra_algorithm(graph: Graph, start_node: str) -> (str, list):
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


def print_result(previous_nodes: list, shortest_path: list, start_node: str, target_node: str) -> None:
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print("\nНайден следующий лучший маршрут с длиной {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


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


def initialization_graph(init_str: list) -> dict:
    # Add connections, described in init_str to the init graph, initializated with [] for elems in nodes
    global nodes
    # print("!\t", init_str)
    init_graph = {i: {} for i in nodes}
    for num_el in range(1, 4 + 1):
        for floor in range(2, 3 + 1):
            point1 = f"S_GA_{floor}_e_{num_el}"
            for floor_2 in range(2, 3 + 1):
                if floor_2 != floor:
                    point2 = f"S_GA_{floor_2}_e_{num_el}"
                    init_graph[point1][point2] = 1
                    init_graph[point2][point1] = 1

    for num_l in range(1, 5 + 1):
        for floor in range(2, 2 + 1):
            point_1 = f"S_GA_{floor}_l_{num_l}U"
            point_2 = f"S_GA_{floor + 1}_l_{num_l}D"
            init_graph[point_1][point_2] = 2
            init_graph[point_2][point_1] = 2

    for init_elem in init_str:
        if "|" in init_elem:
            # print("!!   ", init_elem)
            pref = init_elem.split("|")[0]
            add_connections = init_elem.split("|")[1].split(",")

            for i in add_connections:
                where_to_add = i.split("-")[0]
                elems_add = i.split("-")[1].split("/")
                point = pref + where_to_add[0] + "_" + where_to_add[1:]
                for elem in elems_add:
                    if ";" in elem:
                        elem_name, lenght = elem.split(";")[0], int(elem.split(";")[1])
                    else:
                        elem_name, lenght = elem, 1
                    point_reverse = pref + elem_name[0] + "_" + elem_name[1:]
                    init_graph[point][point_reverse] = lenght
                    init_graph[point_reverse][point] = lenght
        else:
            for add_connection in init_elem.split(","):
                where_to_add, elems_add = add_connection.split("-")[0], add_connection.split("-")[1]
                if ";" in elems_add:
                    elems_add = elems_add.split(";")
                    elem, lenght = elems_add[0], elems_add[1]
                else:
                    elem, lenght = elems_add, 1
                init_graph[where_to_add][elem] = lenght
                init_graph[elem][where_to_add] = lenght

    return init_graph


init_graph_connections = [
    "S_GA_2_|p24-p23,p23-k200/p22/l5U/l5D,p22-k200V/p10,p10-p9/p11/p18,p9-l1U/l1D/p8,p8-k207/p7,p7-k212/p6,p6-k209/p5,p5-k214/p4,p4-k211/p3,p3-k216/p2,p2-p1/k213,p1-k218,p11-l2U/l2D/p12,p12-k210/p13,p13-k205/k208/p14,p14-p15/k203/k206,p15-p16/k204,p16-p17/k201,p17-k202/l3U/l3D,p18-p26/p28/p19,p26-e3,p28-e4,p25-e1,p27-e2,p19-p25/p20/p27,p20-p21",
    "S_GA_3_|p32-p31;6,p31-p30,p33-e1,p35-e3,p34-e2,p36-e4,p30-p35;5/p33;5/p29,p29-p28/p38;2/p39;2,p28-l5U;2/l5D;2,p38-p11;2/p34;2,p39-p12;2/p36;2,p11-p10;4/h1l,p10-l1U;2/l1D;2/p9;3,p9-k6;1/p8;2,p8-k11/p7,p7-p6;2/k7,p6-p5;2/k12B,p5-k8/p4;2,p4-p3/k12,p3-p2;2/k9,p2-k12A/p1;2,p1-k10,p12-p13;5/h1r,p13-l2U;2/l2D;2/p14;3,p14-k2/p15;2,p15-p16/k14,p16-k1/p17;2,p17-k3/p18;3,p18-k4/p19,p19-k13/p20;2,p20-p37/k5,p37-p21;2/b15,p21-l3U;2/l3D;2/p22,p22-p23;3/p27;5,p23-a300,p27-a300,a300-p24/p26,p26-p25;7,p25-p24/l4U;2/l4D;2"]

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
