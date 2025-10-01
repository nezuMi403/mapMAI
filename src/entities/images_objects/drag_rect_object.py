import pygame

from src.engine.renderer import Renderer
from src.entities.base_objects.game_object import GameObject


class DragRectObject(GameObject):
    def __init__(self, x: int, y: int, width: float, height: float,
                 color: tuple[int, int, int, int] = (0, 0, 0, 0),
                 border_radius=0):
        super().__init__(x, y, width, height)
        self.color = color
        self.border_radius = border_radius
        self.rect = pygame.Rect(x, y, width, height)

        self.dragging = False
        self.drag_start_pos = [0, 0]

    def update(self, dt: float):
        super().update(dt)
        if self.rect != pygame.Rect(self.x, self.y, self.width, self.height):
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_event(self, event: pygame.event.Event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.dragging = True
            self.drag_start_pos[0] = event.pos[0] - self.x
            self.drag_start_pos[1] = event.pos[1] - self.y
        if event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = False
        if event.type == pygame.MOUSEMOTION and self.dragging:
            self.x, self.y = self.get_new_position_drag(event.pos)

    def get_new_position_drag(self, event_pos):
        x = event_pos[0] - (self.drag_start_pos[0])
        y = event_pos[1] - (self.drag_start_pos[1])

        return x, y


    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        if not self.visible:
            return

        Renderer.draw_rect(surface, self.color, self.rect, border_radius=self.border_radius)
