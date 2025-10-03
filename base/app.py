import pygame

from base.scene_manager import SceneManager


class App:
    """
    Главный класс всего приложения

    В нем находится главный цикл приложения (run),
    создаётся окно приложения (screen)
    и работает класс, управляющий всеми сценами (SceneManager)
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))  # Окно приложения
        pygame.display.set_caption("mapMAI")

        self.scene_manager = SceneManager(self)  # Менеджер сцен (передаём ему класс App)

        self.clock = pygame.time.Clock()  # Для плавного обновления кадров
        self.fps = 60


    def run(self):
        """Основной цикл приложения"""
        while True:
            dt = self.clock.tick(self.fps) / 1000  # время в секундах после последнего кадра

            # Обновление текущей сцены (current_scene)
            self.scene_manager.current_scene.handle_events(pygame.event.get())
            self.scene_manager.current_scene.update(dt)
            self.scene_manager.current_scene.render()

            pygame.display.flip()
