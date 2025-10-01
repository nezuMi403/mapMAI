import pygame
from src.entities.images_objects.drag_rect_object import DragRectObject
from src.scenes.base_scene import BaseScene

class TestScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.rect = DragRectObject(100, 100, 100, 100, (100, 240, 100, 100))
        self.background_color = (140, 140, 240)
        self.set_objects()


    def on_enter(self):
        print("Загружена тест сцена")

    def set_objects(self):
        self.add_object(self.rect)

    def handle_events(self, events):
        super().handle_events(events)


    def update(self, dt: float):
        super().update(dt)

    def render(self):
        super().render()
        #self.rect.draw(self.game.screen)