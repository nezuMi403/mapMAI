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


class Graph(object):
    def __init__(self):
        self.init_params()
        self.add_to_nodes()
        self.init_graph = self.initialization_graph()
        # pprint(self.init_graph, width=1000, depth=3)
        self.graph = self.construct_graph(self.nodes, self.init_graph)

        self.dict_of_points_coordinates = self.make_dictionar_of_points()
        # pprint(dict_of_points_coordinates)

    def init_params(self):
        '''inicializating all constants for graph'''
        self.init_graph_connections = [
            "S_GA_2_|p1-p2/k218,p2-p3/k213,p3-p4/k216,p4-p5/k211,p5-p6/k214,p6-p7/k209,p7-p8/k212,p8-k207/p36,p36-t1/p9,p9-l1/p28,p28-p35/p29,p35-k200V/p34,p34-p33,p33-p37/p39/p32,p37-l4U,p32-p31,p31-k200/p30,p30-p29/p11,p11-l2/p38,p38-t2/p12,p12-k210/p13,p13-k205/p14,p14-k208/p15,p15-k203/p16,p16-p17/k206,p17-k204/p18,p18-k201/p19,p19-l3/p20,p20-k202,p29-p21,p21-p22/e3/e4,p22-p23/e1/e2",
            "S_GA_3_|p1-k10/p2,p2-k12A/p3,p3-p4/k9,p4-p5/k12,p5-k8/p6,p6-k12B/p7,p7-k7/p8,p8-k11/p9,p9-k6/p36,p36-p10/t1,p10-l1/p11,p11-p37/h1l,p37-p17/p12,p17-p18/p38/l4,p38-p16/p15,p18-p13/p14/p19,p13-p12,p12-e3,p14-p15,p15-e4,p19-e1/e2/p20,p16-h1r/p21,p21-l2/p39,p39-t2/p22,p22-k2/p23,p23-k14/k1/p25,p25-p26/k3,p26-p27/k4,p27-k13/p28,p28-k5/p29,p29-b15/p30,p30-l3/p31,p31-p32/p33,p33-p35,p35-a300,p32-p34,p34-a300",
            "S_GB_7_|p1-p2;2/p30/p17;4,p30-p4;3/k738,p4-l1;2/p5,p5-k740/p6,p6-tw/p7,p7-k731/p8;3,p8-k742/k733/p9;2,p9-k735/p10,p10-k737/p11;3,p11-k739/k744/p12;5,p12-k741/p13,p13-k743/k746/p14;7,p14-k748/p15;3,p15-k750/p16;2,p16-l3;2,p2-p3/e3;2/e4;2,p3-e1;2/e2;2,p17-k736/p18;2,p18-tm/p19;3,p19-k729/k734/p20;3,p20-k727/p21,p21-p22;3/k725/k732,p22-k723/k730/p23,p23-l2;2/p24,p24-p25,p25-p26,p26-k728/p27,p27-p29;3/p28;3,p29-k726,p28-k724",
            "S_GB_6_|p1-e1;2/e2;2/p2,p2-e3;2/e4;2/p3,p3-p4/p20;4,p4-k648/p5;3,p5-l1;2/p6;2,p6-k650/p7;2,p7-tw/p8,p8-k633/k652/p9;3,p9-p10;3/k635,p10-k637/k654/p11;3,p11-p12/k639/k656,p12-k658/p13;4,p13-k660/k641/p14;2,p14-p15;3/k643/k662,p15-p16;5/k645,p16-k647/k664/p17,p17-l3;2/p18,p18-p19;3,p19-l4;13,p20-k646/p21;2,p21-tm/p22;3,p22-p23;4/k631/k644,p23-k629/p24,p24-k627/k642/p25;3,p25-k640/p26,p26-l2;2/p27,p27-k638/p28,p28-p29,p29-k636/p30;3,p30-k632",
            "S_GA_7_|p1-p2;2/k722,p2-p3;2/k721,p3-k722/p4,p4-p5;2/k719,p5-p6/k720,p6-p7;3/k717,p7-p8/k715,p8-p9;3/k718,p9-p10/l1;2,p10-k716/p11;3,p11-p12/e1;2/e2;2,p12-k713/p13,p13-k714/p14;3,p14-k711/p15,p15-k712/p16,p16-e3;2/e4;2/p17;2/p17-p18/l2;2,p18-k712/p19,p19-k710/p20;2,p20-k709/p21,p21-k708/p22;3,p22-k707/p23;2,p23-k706/p24,p24-k705/p25,p25-k704/p26;3,p26-l3;2",
            "S_GV_3_|p1-p2/l1D,p2-p3,p3-b1/p4,p4-p5,p5-f1/p6,p6-l2D"]

        self.korpuses = ['1', '10', '11', '12', '14', '15', '16', '18', '19', '2', '21', '22', '24A', '24B', '24V', '2A', '2V', '3',
                '35', '4', '5', '57', '59', '60', '7', '70', '79', '82', '9', 'DK', 'GAK', 'GUKA', 'GUKB', 'GUKV']

        self.korpuses_tmp = ['GUKA', 'GUKB', 'GUKV']
        self.floors_tmp = {"GUK": 7}

        self.add_graph = ["S_GA_2_k_(200...214,216,218,200V)", "S_GA_2_p_(1...39)", "S_GA_2_e_(1...4)", "S_GA_2_l_1U",
                    "S_GA_2_l_1D", "S_GA_2_l_2U", "S_GA_2_l_2D", "S_GA_2_l_3D", "S_GA_2_l_3U", "S_GA_2_l_4U", "S_GA_2_t_1", "S_GA_2_t_2", "S_GA_3_l_(1...4)",
                    "S_GA_3_p_(1...39)", "S_GA_3_k_(1...14,12A,12B)", "S_GA_3_h_1l", "S_GA_3_t_1", "S_GA_3_t_2", "S_GA_3_h_1r",
                    "S_GA_3_a_300", "S_GA_3_b_15", "S_GA_3_e_(1...4)", "S_GA_2_l_4U", "S_GA_2_l_4D", "S_GA_2_l_5D",
                    "S_GA_2_l_5U", "S_GB_7_k_(723...744,746,748,750)", "S_GB_7_t_m", "S_GB_7_t_w", "S_GB_7_e_(1...4)",
                    "S_GB_7_l_(1...3)", "S_GB_7_p_(1...30)", "S_GB_6_p_(1...30)",
                    "S_GB_6_k_(631...633,635...648,650,652,654,656,658,660,662,664,629,627)", "S_GB_6_e_(1...4)",
                    "S_GB_6_l_(1...4)", "S_GB_6_t_m", "S_GB_6_t_w", "S_GV_2_p_(1...25)", "S_GV_2_l_(1...7)",
                    "S_GV_2_k_(221V,21V,202,212,228,231,240,240A,210,214)", "S_GV_2_e_(1...3)", "S_GA_7_p_(1...26)",
                    "S_GA_7_k_(704...722)", "S_GA_7_e_(1...4)", "S_GA_7_l_(1...3)", "S_GV_3_f_1", "S_GV_3_p_(1...6)", "S_GV_3_l_1D", "S_GV_3_l_2D", "S_GV_3_b_1",
                    "S_GV_7_p_(1...18)", "S_GV_7_k_(701...706)", "S_GV_7_l_1D", "S_GV_7_e_(1...3)", "S_GV_7_h_1",]
        self.nodes = []

        self.sp_s = ["S_GV_3_\nb_1: (4454, 4035)\np_3: (4454, 4192)\np_4: (4130, 4192)\np_2: (8470, 4192)\np_1: (8470, 4872)\nl_1D: (6934, 4872)\nl_2D: (4785, 7026)\np_5: (4130, 8518)\np_6: (4785, 8518)\nf_1: (4130, 8800)",
                     """S_GA_2_
p_23: (3812, 3156)
e_2: (4545, 3313)
e_1: (3055, 3315)
p_22: (3821, 3328)
l_3U: (7534, 3424)
l_3D: (7639, 3426)
l_2U: (4944, 3430)
l_2D: (4820, 3432)
l_1U: (2782, 3444)
l_1D: (2667, 3445)
e_4: (4541, 3495)
e_3: (3061, 3499)
p_21: (3829, 3514)
k_207: (1985, 3597)
k_209: (1510, 3603)
k_203: (6142, 3606)
k_211: (1017, 3607)
k_201: (7321, 3608)
k_213: (548, 3613)
k_205: (5636, 3622)
t_2: (5085, 3632)
t_1: (2481, 3673)
p_36: (2481, 3809)
p_29: (3822, 3791)
p_11: (4881, 3794)
p_19: (7561, 3796)
p_38: (5083, 3797)
p_20: (7617, 3798)
p_13: (5631, 3800)
p_14: (5688, 3800)
p_2: (530, 3801)
p_18: (7352, 3801)
p_15: (6135, 3802)
p_1: (266, 3803)
p_28: (3372, 3803)
p_4: (1023, 3805)
p_6: (1512, 3807)
p_8: (2005, 3807)
p_16: (6212, 3807)
p_12: (5209, 3808)
p_7: (1781, 3809)
p_9: (2713, 3809)
p_17: (7116, 3813)
p_30: (4261, 3814)
p_3: (827, 3818)
p_5: (1302, 3818)
k_212: (1774, 3962)
k_216: (812, 3966)
k_208: (5669, 3967)
k_214: (1299, 3969)
k_206: (6143, 3976)
k_204: (7108, 3976)
k_218: (265, 3977)
k_210: (5182, 3989)
k_202: (7585, 3989)
p_35: (3375, 4069)
l_4U: (3914, 4080)
k_200V: (3049, 4081)
l_4D: (3760, 4082)
p_37: (3835, 4213)
k_200: (4503, 4746)
p_31: (4259, 4772)
p_34: (3374, 5254)
p_33: (3823, 5255)
p_32: (4253, 5257)
p_39: (3826, 5598)""","""S_GA_3_
p_20: (3815, 4350)
p_34: (7945, 4455)
a_300: (7945, 4455)
p_32: (7810, 4455)
e_2: (4550, 4513)
e_1: (3056, 4513)
p_19: (3815, 4513)
p_18: (3815, 4620)
p_13: (3304, 4620)
p_14: (4317, 4620)
l_1U: (2725, 4656)
l_3D: (7600, 4657)
l_3U: (7600, 4657)
l_2D: (4890, 4665)
l_1D: (2725, 4656)
l_2U: (4890, 4665)
p_17: (3815, 4690)
e_3: (3056, 4707)
e_4: (4540, 4715)
p_12: (3304, 4707)
p_15: (4317, 4715)
k_11: (1985, 4897)
b_15: (7350, 4888)
t_1: (2490, 4891)
k_13: (6765, 4891)
k_12B: (1510, 4897)
k_12A: (561, 4898)
k_14: (5676, 4899)
k_12: (1056, 4902)
t_2: (5090, 4903)
p_10: (2725, 4991)
p_2: (561, 4991)
p_9: (2241, 4991)
p_3: (820, 4991)
p_36: (2490, 4991)
p_8: (1985, 4991)
p_1: (270, 4991)
p_11: (3425, 4991)
p_37: (3425, 4690)
p_38: (4180, 4690)
p_4: (1055, 4991)
p_6: (1510, 4991)
p_7: (1756, 4991)
p_5: (1280, 4991)
p_30: (7600, 4991)
p_21: (4890, 4991)
p_31: (7810, 4991)
l_4D: (3813, 5005)
p_39: (5090, 4991)
p_27: (6765, 4991)
p_28: (7140, 4991)
p_29: (7350, 4991)
p_16: (4180, 4991)
p_22: (5345, 4991)
p_26: (6635, 4991)
l_4U: (3813, 5005)
p_23: (5676, 4991)
p_25: (6145, 4991)
k_9: (820, 5087)
k_10: (270, 5093)
k_2: (5345, 5097)
k_5: (7140, 5097)
k_8: (1280, 5099)
k_7: (1756, 5103)
k_1: (5681, 5105)
k_4: (6635, 5105)
k_3: (6145, 5107)
k_6: (2241, 5114)
p_35: (7940, 5760)
a_300: (7940, 5760)
p_33: (7810, 5760)
h_1l: (3425, 5864)
h_1r: (4187, 5864)"""
]



    def give_graph(self):
        for i in sorted(self.graph.keys(), key=lambda x: x):
            # print(f"\n{i}:")
            for j in sorted(self.graph[i].keys(), key=lambda x: x):
                # print(f"|---{j}\t{self.graph[i][j]}")
                pass

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


    def dijkstra_algorithm(self, start_node: str):
        unvisited_nodes = list(self.get_nodes())
        # print(unvisited_nodes)
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

            neighbors = self.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)
        # print(previous_nodes)
        return previous_nodes, shortest_path


    def print_result(self, previous_nodes: list, shortest_path: list, start_node: str, target_node: str) -> None:
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        path.append(start_node)

        #print("\nНайден следующий лучший маршрут с длиной {}.".format(shortest_path[target_node]))
        #print(" -> ".join(reversed(path)))
        #print(type(shortest_path[target_node]))
        #print(type(reversed(path)))
        print([shortest_path[target_node]] + list(reversed(path)))
        return [shortest_path[target_node]] + list(reversed(path))


    def add_to_nodes(self) -> None:
        # making a list nodes with all points
        for node in self.add_graph:
            if "_l_" in node and "(" in node:
                do = node.split("(")[1].split(")")[0]
                sample_node = node.split("(")[0]
                for action in do.split(","):
                    if "..." in action:
                        start, stop = map(int, action.split("..."))
                        for i in range(start, stop + 1):
                            self.nodes.append(sample_node + str(i) + "U")
                            self.nodes.append(sample_node + str(i) + "D")
                    else:
                        self.nodes.append(sample_node + action + "U")
                        self.nodes.append(sample_node + action + "D")
            elif "(" in node:
                do = node.split("(")[1].split(")")[0]
                sample_node = node.split("(")[0]
                for action in do.split(","):
                    if "..." in action:
                        start, stop = map(int, action.split("..."))
                        for i in range(start, stop + 1):
                            self.nodes.append(sample_node + str(i))
                    else:
                        self.nodes.append(sample_node + action)
            else:
                self.nodes.append(node)


    def initialization_graph(self) -> dict:
        # Add connections, described in init_str to the init graph, initializated with [] for elems in nodes
        # print("!\t", init_str)
        init_graph = {i: {} for i in self.nodes}
        for num_el in range(1, 4 + 1):
            for floor in range(2, 3 + 1):
                point1 = f"S_GA_{floor}_e_{num_el}"
                if point1 in init_graph.keys():
                    for floor_2 in range(2, 3 + 1):
                        if floor_2 != floor:
                            point2 = f"S_GA_{floor_2}_e_{num_el}"
                            if point2 in init_graph.keys():
                                init_graph[point1][point2] = 1
                                init_graph[point2][point1] = 1

        for num_l in range(1, 5 + 1):
            for floor in range(2, 2 + 1):
                point_1 = f"S_GA_{floor}_l_{num_l}U"
                point_2 = f"S_GA_{floor + 1}_l_{num_l}D"
                if (point_1 in init_graph.keys()) and (point_2 in init_graph.keys()) and (point_2 in init_graph[point1].keys()) and (point_1 in init_graph[point2].keys()):
                    init_graph[point_1][point_2] = 2
                    init_graph[point_2][point_1] = 2

        for init_elem in self.init_graph_connections:
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
                        if elem_name[-1] not in "UD" and elem_name[0] == "l":
                            point_reverse = pref + elem_name[0] + "_" + elem_name[1:] + "U"
                            point_reverse2 = pref + elem_name[0] + "_" + elem_name[1:] + "D"
                            init_graph[point][point_reverse] = lenght
                            init_graph[point][point_reverse2] = lenght
                            init_graph[point_reverse][point] = lenght
                            init_graph[point_reverse2][point] = lenght
                        else:
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

    def make_dictionar_of_points(self) -> dict:
        '''Add coords of points to the dictionary'''

        sl = {}
        # print("sp_s:")
        # print(self.sp_s[0])
        for s in self.sp_s:
            list_toDo = s.strip().split("\n")
            prefix, points = list_toDo[0], list_toDo[1:]
            name_building = prefix[:len(prefix)-3].replace("G", "GUK_")

            name_building = name_building.replace("S_GUK_A", "guka")
            name_building = name_building.replace("S_GUK_B", "gukb")
            name_building = name_building.replace("S_GUK_V", "gukv")
            name_floor = int(prefix[-2])
            # print(name_floor, prefix)
            if name_building not in sl.keys():
                sl[name_building] = {}

            if name_floor not in sl[name_building].keys():
                sl[name_building][name_floor] = {'coordinates' : {}, 'connections':[]}
            # print(sl, points)
            # print(name_building)
            for point in points:
                point = point.split(": ")
                point_name = prefix + point[0]
                # print(point[1][1:][:len(point[1]) - 1].split(", "))
                point_coords = tuple(map(int, point[1][1:].split(")")[0][:len(point[1]) - 1].split(", ")))
                # print(point_coords)
                sl[name_building][name_floor]['coordinates'][point_name] = point_coords
            # print("points: ", points)
            for point in points:
                point_name = prefix + point.split(": ")[0]
                # print(point_name)
                for point_neightbor in self.init_graph[point_name].keys():
                    sl[name_building][name_floor]['connections'].append((point_name, point_neightbor))
        # print("SL:")
        # pprint(sl)
        return sl

    def return_shortest_path(self, input_point:str, output_point:str) -> list:
        '''Return the shortest route from input_point ti utput_point'''

        # graph.give_graph()
        previous_nodes, shortest_path = self.dijkstra_algorithm(start_node=input_point)
        sp_result = self.print_result(previous_nodes, shortest_path, start_node=input_point, target_node=output_point)
        return sp_result[1:]

    def get_all_points(self):
        all_points = []
        # print("!!! dict_of_points_coords")
        # pprint(self.dict_of_points_coordinates)
        for building, levels in self.dict_of_points_coordinates.items():
            for level, data in levels.items():
                if 'coordinates' in data:
                    for point_name, coords in data['coordinates'].items():
                        all_points.append({
                            'name': point_name,
                            'building': building,
                            'level': level,
                            'coordinates': coords
                        })

        # Сортируем точки по имени для удобного отображения
        all_points.sort(key=lambda x: x['name'])
        all_points = [i for i in all_points if "_p_" not in i]
        return all_points

    #"S_GV_7_|p1-p2/k701/p12,p2-k702/p3,p3-k702/p4,p4-p5/k703,p5-p6/k703,p6-k704/p7,p7-p18/k704,p18-h1/p8,p8-p9/k705,p9-k705/p10,p10-k706/p11,p11-p12/k701,p12-p13,p13-e1/p16,p16-e2/p14,p14-p15/p17,p17-e3,p15-l1D"]