import pygame

from src.engine.renderer import Renderer
from src.entities.base_objects.game_object import GameObject


class GameRect(GameObject):
    def __init__(self, x: float, y: float, width: float, height: float,
                 color: tuple[int, int, int, int] = (0, 0, 0, 0),
                 border_radius=0):
        super().__init__(x, y, width, height)
        self.color = color
        self.border_radius = border_radius
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, dt: float):
        super().update(dt)
        if self.rect != pygame.Rect(self.x, self.y, self.width, self.height):
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_event(self, event: pygame.event.Event):
        super().handle_event(event)

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        if not self.visible:
            return

        Renderer.draw_rect(surface, self.color, self.rect, border_radius=self.border_radius)
