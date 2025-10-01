#src/entities/base_objects/game_object.py
from typing import Dict, Any
import pygame

from src.engine.renderer import Renderer


class GameObject:
    def __init__(self, x: int = 0, y: int = 0,
                 width: float = 32, height: float = 32,
                 visible: bool = True, active: bool = True):
        """
        Базовый класс для всех игровых объектов

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
        self.hovered = False
        self.tags = []  # Для идентификации объектов
        self.properties: Dict[str, Any] = {}  # Дополнительные свойства

        # Прямоугольник для коллизий
        self.rect = pygame.Rect(x, y, width, height)


    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y

    @position.setter
    def position(self, value: tuple[int, int]):
        self.x, self.y = value
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, dt: float):
        """Обновление состояния объекта"""
        if not self.active:
            return

        # Обновляем позицию прямоугольника
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface: pygame.Surface):
        """Отрисовка объекта"""
        #if not self.visible:
            #return

        #TODO: Для отладки - рисуем прямоугольник
        #pygame.draw.rect(surface, (255, 0, 0, 100), self.rect, 1)
        pass

    def handle_event(self, event: pygame.event.Event):
        """Обработка событий"""
        if not self.active:
            return
        if event.type == pygame.MOUSEMOTION:
            rect = Renderer.get_rect(self.rect)
            if rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered:
                self.on_click_left(event)
            elif event.button == 3 and self.hovered:
                self.on_click_right(event)


    def on_click_left(self, event: pygame.event.Event):
        """Обработка клика мышью левой кнопкой"""
        # print(f"Клик левой кнопкой по {self.__class__.__name__} ({event.pos})")
        pass

    def on_click_right(self, event: pygame.event.Event):
        """Обработка клика мышью правой кнопкой"""
        # print(f"Клик правой кнопкой по {self.__class__.__name__} ({event.pos})")
        pass

    def on_collision(self, other: 'GameObject'):
        """Вызывается при коллизии с другим объектом"""
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
