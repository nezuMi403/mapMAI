import pygame

from typing import List, Dict, Type

from base.app import App
from base.base_object import BaseObject
from base.base_scene import BaseScene
from base.test.test_object import TestObject


class TestScene(BaseScene):
    """
    Тестовая сцена, для примера
    """
    
    def __init__(self, app):
        super().__init__(app)  # вызывает BaseScene.__init__

        self.move_rect = TestObject(100, 100, 64, 64)

        self.set_objects()

    def set_objects(self):
        """Добавление объектов на сцену"""
        # Если не добавить тут объекты, они не появятся
        self.add_object(self.move_rect)

    def handle_events(self, events):
        """
        Обработка событий

        Некоторые события event.type:
        # pygame.KEYDOWN (нажатие клавиши) / pygame.KEYUP (отпускание клавиши)
            event.key == pygame.K_ESCAPE
            event.key == pygame.K_a
        # pygame.MOUSEBUTTONDOWN (нажатие мыши) / pygame.MOUSEBUTTONUP (отпускание мыши)
            event.key == pygame.BUTTON_LEFT (левая кнопка мыши)
            event.key == pygame.BUTTON_MIDDLE (колёсико мыши)
            event.key == pygame.BUTTON_RIGHT (правая кнопка мыши)
        """
        # вызывает BaseScene.handle_events
        # это важно, тк там проверка на активность объекта и обработка событий объектов
        super().handle_events(events)
        for event in events:

            # Пример обработки события сцены:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit(0)
                elif event.key == pygame.K_a:
                    print('Нажата клавиша A')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    print('Отпущена клавиша A')

    def update(self, dt: float):
        """Обновление состояния сцены"""
        super().update(dt)

    def render(self):
        """Отрисовка сцены"""
        super().render()

    def on_enter(self):
        super().on_enter()
