import pygame
from typing import List, Dict, Type
from src.entities.base_objects.game_object import GameObject


class BaseScene:
    def __init__(self, game):
        """
        Базовый класс для всех сцен

        :param game: Ссылка на основной объект игры
        """
        self.game = game
        self.objects: List[GameObject] = []
        self.next_scene = None  # Сцена для перехода
        self.background_color = (0, 0, 0)
        self.paused = False

    def add_object(self, obj: GameObject):
        """Добавляет объект на сцену"""
        self.objects.append(obj)
        return obj

    def remove_object(self, obj: GameObject):
        """Удаляет объект со сцены"""
        if obj in self.objects:
            self.objects.remove(obj)

    def find_objects_by_tag(self, tag: str) -> List[GameObject]:
        """Находит все объекты с указанным тегом"""
        return [obj for obj in self.objects if tag in obj.tags]

    def handle_events(self, events):
        """Обработка событий"""
        if self.paused:
            return

        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
                if event.key == pygame.K_F1:
                    self.game.change_fullscreen(not self.game.get_fullscreen())

            # Передаем события всем активным объектам
            for obj in self.objects:
                if obj.active:
                    obj.handle_event(event)

    def update(self, dt: float):
        """Обновление состояния сцены"""
        if self.paused:
            return

        # Обновляем все активные объекты
        for obj in self.objects:
            if obj.active:
                obj.update(dt)

    def render(self):
        """Отрисовка сцены"""
        # Очистка экрана
        self.game.screen.fill(self.background_color)

        # Отрисовка всех видимых объектов
        for obj in sorted(self.objects, key=lambda o: o.y):  # Сортировка по Y для псевдо-изометрии
            if obj.visible:
                obj.draw(self.game.screen)

    def on_enter(self):
        """Вызывается при входе в сцену"""
        print('Загружена сцена', self.__class__.__name__)
        pass

    def on_exit(self):
        """Вызывается при выходе из сцены"""
        pass

    def pause(self):
        """Приостанавливает сцену"""
        self.paused = True

    def resume(self):
        """Возобновляет сцену"""
        self.paused = False