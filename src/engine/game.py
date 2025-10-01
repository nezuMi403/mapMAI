import pygame

from src.engine.game_settings import GameSettings
from src.engine.scene_manager import SceneManager


class Game:
    def __init__(self):
        pygame.init()
        self._init_display()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = False
        self.scene_manager = SceneManager(self)  # Менеджер сцен

    def _init_display(self, fullscreen=False, resolution=(682, 512)):
        """Инициализирует окно"""
        width, height = resolution
        fullscreen = fullscreen

        GameSettings.resolution = width, height
        GameSettings.fullscreen = fullscreen

        if fullscreen:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption("mapMAI")

    def change_fullscreen(self, fullscreen):
        GameSettings.fullscreen = fullscreen
        self._init_display(fullscreen)

    def get_fullscreen(self):
        return GameSettings.fullscreen

    def run(self):
        self.running = True

        last_time = pygame.time.get_ticks()  # Время предыдущего кадра в миллисекундах
        while self.running:
            # Вычисляем dt
            current_time = pygame.time.get_ticks()
            dt = (current_time - last_time) / 1000.0  # Переводим в секунды
            last_time = current_time

            self.clock.tick(self.fps)
            self.scene_manager.current_scene.handle_events(pygame.event.get())
            self.scene_manager.current_scene.update(dt)
            self.scene_manager.current_scene.render()

            pygame.display.flip()
