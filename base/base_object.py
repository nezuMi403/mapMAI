import pygame


class BaseObject:
    """
    Базовый класс для всех объектов
    """
    def __init__(self, x: float = 0, y: float = 0,
                 width: float = 32, height: float = 32,
                 visible: bool = True, active: bool = True):
        """
        :param x: Позиция по X
        :param y: Позиция по Y
        :param width: Ширина объекта
        :param height: Высота объекта
        :param visible: Видимость объекта
        :param active: Активность объекта (обновляется и обрабатывает события)
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        self.active = active

        self.hovered = False  # наведена ли мышка сейчас на этот объект

        # Прямоугольник для коллизий
        self.rect = pygame.Rect(x, y, width, height)

    def set_pos(self, x: float, y: float):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def handle_event(self, event: pygame.event.Event):
        """Обработка событий"""

        # если объект не активен, то ничего не делаем
        if not self.active:
            return

        self.check_hovered(event)  # проверка, наведена ли мышь

    def update(self, dt: float):
        """Обновление состояния объекта"""

        # если объект не активен, то ничего не делаем
        if not self.active:
            return

    def draw(self, surface: pygame.Surface):
        """Отрисовка объекта"""

        # если объект не виден, то ничего не делаем
        if not self.visible:
            return

        # Для отладки - рисуем прямоугольник
        # pygame.draw.rect(surface, (255, 0, 0, 100), self.rect, 1)

    def check_hovered(self, event: pygame.event.Event):
        """Проверка, наведена ли мышка сейчас на этот объект"""
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False
