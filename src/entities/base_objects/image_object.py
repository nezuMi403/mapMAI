#src/entities/base_objects/image_object.py
import pygame
from src.engine.renderer import Renderer
from src.engine.paths import resource_path
from src.entities.base_objects.game_object import GameObject


class ImageObject(GameObject):
    def __init__(self, x, y, width, height, image_path, is_scale=True):
        super().__init__(x, y, width, height)
        full_path = resource_path(image_path)
        self.image = pygame.image.load(full_path).convert_alpha()

        if is_scale:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        if not self.visible:
            return

        Renderer.blit(surface, self.image, (self.x, self.y))
