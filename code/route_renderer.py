# route_renderer.py
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget


class RouteRenderer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_building = None
        self.current_level = None
        self.navigation_data = {}  # {building: {level: {coordinates: {}, connections: []}}}
        self.current_route = []

    def set_navigation_data(self, navigation_data):
        """Установить все данные навигации"""
        self.navigation_data = navigation_data

    def set_current_location(self, building, level):
        """Установить текущее здание и этаж"""
        self.current_building = building
        self.current_level = level
        self.draw_route()

    def set_route(self, route_nodes):
        """Установить текущий маршрут для отображения"""
        self.current_route = route_nodes
        print(route_nodes)
        self.draw_route()

    def draw_route(self):
        """Отрисовать маршрут на canvas"""
        self.canvas.clear()

        if not self.current_route or not self.current_building or not self.current_level:
            print("!")
            return

        # Получаем данные для текущего здания и этажа
        building_data = self.navigation_data.get(self.current_building, {})
        level_data = building_data.get(self.current_level, {})
        coordinates = level_data.get('coordinates', {})
        connections = level_data.get('connections', [])
        print("coordinates:", coordinates)
        if not coordinates:
            print("!")
            return

        # Рисуем линии маршрута
        with self.canvas:
            Color(0, 0, 1, 1)
            points = []

            for i in range(len(self.current_route) - 1):
                node1 = self.current_route[i]
                node2 = self.current_route[i + 1]
                print(self.current_route, node1, node2)

                if node1 in coordinates and node2 in coordinates:
                    x1, y1 = coordinates[node1]
                    x2, y2 = coordinates[node2]

                    # Координаты теперь относительно scatter_plane
                    points.extend([x1, y1, x2, y2])
                    print(points)

            if points:
                print("drawing line")
                Line(
                    points=points,
                    #width=1.1,
                    dash_length=5,
                    dash_offset=2,
                )

            # Рисуем точки маршрута
            Color(0, 0, 1, 0.6)
            for node in self.current_route:
                if node in coordinates:
                    x, y = coordinates[node]
                    r = 4
                    Ellipse(pos=(x - r//2, y - r//2), size=(r, r))