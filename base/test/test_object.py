import pygame

from base.base_object import BaseObject


class TestObject(BaseObject):
    """
    Тестовый объект для примера
    """
    def __init__(self, x: float = 0, y: float = 0,
                 width: float = 32, height: float = 32,
                 visible: bool = True, active: bool = True):
        super().__init__(x, y, width, height, visible, active)
        self.color = (120, 240, 120)
        self.v = 100  # скорость

    def handle_event(self, event: pygame.event.Event):
        """Обработка событий"""
        super().handle_event(event)

        if self.hovered:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    print("Кликнулось")


    def update(self, dt: float):
        """Обновление состояния объекта"""
        super().update(dt)
        x_pos = self.x
        x_pos += self.v * dt  # v * t в секундах
        self.set_pos(x_pos, self.y)

        if x_pos > 736 or x_pos < 0:
            self.v *= -1

    def draw(self, surface: pygame.Surface):
        """Отрисовка объекта"""
        super().draw(surface)
        pygame.draw.rect(surface, self.color, self.rect)
