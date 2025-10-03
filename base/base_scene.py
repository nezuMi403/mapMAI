import pygame

from typing import List, Dict, Type

from base.app import App
from base.base_object import BaseObject


class BaseScene:
    """
    Базовый класс для всех сцен
    От него наследуются все остальные сцены
    """
    
    def __init__(self, app):
        self.app: App = app
        self.objects: List[BaseObject] = []
        self.background_color = (0, 0, 0)

    def add_object(self, obj: BaseObject):
        """Добавляет объект на сцену"""
        self.objects.append(obj)
        return obj

    def remove_object(self, obj: BaseObject):
        """Удаляет объект со сцены"""
        if obj in self.objects:
            self.objects.remove(obj)

    def handle_events(self, events):
        """Обработка событий"""
        for event in events:
            # Передаем событиe всем активным объектам сцены
            for obj in self.objects:
                if obj.active:
                    obj.handle_event(event)

    def update(self, dt: float):
        """Обновление состояния сцены"""
        # Обновляем все активные объекты
        for obj in self.objects:
            if obj.active:
                obj.update(dt)

    def render(self):
        """Отрисовка сцены"""
        self.app.screen.fill(self.background_color)  # Очистка экрана

        # Отрисовка всех видимых объектов
        for obj in sorted(self.objects, key=lambda o: o.y):  # Сортировка по Y (так надо)
            if obj.visible:
                obj.draw(self.app.screen)

    def on_enter(self):
        """Вызывается при входе в сцену"""
        print('Загружена сцена', self.__class__.__name__)
