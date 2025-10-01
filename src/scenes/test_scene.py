import pygame
from src.entities.base_objects.game_rect import GameRect
from src.scenes.base_scene import BaseScene

class TestScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.rect = GameRect(100, 100, 100, 100, (255, 0, 0, 255))


    def on_enter(self):
        print("Загружена тест сцена")

    def set_objects(self):
        self.add_object(self.rect)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.running = False


    def update(self, dt: float):
        super().update(dt)

    def render(self):
        super().render()
        self.game.screen.fill((240, 240, 240))
        self.rect.draw(self.game.screen)