from typing import Union

import pygame

from src.engine.game_settings import GameSettings


class Renderer:
    """Класс для рендера объектов"""
    @staticmethod
    def blit(surface: pygame.Surface, image: pygame.Surface, dest):
        x0, y0 = GameSettings.X0, GameSettings.Y0
        #если dist - tuple, то берем его как координаты
        if isinstance(dest, tuple):
            dest = pygame.Rect(dest[0]+x0, dest[1]+y0, image.get_width(), image.get_height())
        #если dist - Rect, то берем его как прямоугольник
        elif isinstance(dest, pygame.Rect):
            dest = pygame.Rect(dest.x+x0, dest.y+y0, dest.w, dest.h)
        else:
            raise TypeError('Неверный тип аргумента dest')

        surface.blit(image, dest)


    @staticmethod
    def draw_rect(surface: pygame.Surface, color, rect: pygame.Rect, width=0, border_radius=0):
        rect = pygame.Rect(rect.x+GameSettings.X0, rect.y+GameSettings.Y0, rect.w, rect.h)
        pygame.draw.rect(surface, color, rect, width, border_radius=border_radius)


    @staticmethod
    def get_rect(rect: Union[pygame.Rect, tuple[int, int, int, int]]):
        return pygame.Rect(rect[0]+GameSettings.X0, rect[1]+GameSettings.Y0, rect[2], rect[3])
    @staticmethod
    def render_text_with_outline(surface, line, x, y, color, font):

        text_surface = font.render(line, True, (0, 0, 0))
        Renderer.blit(surface, text_surface, (x + 2, y + 2))
        Renderer.blit(surface, text_surface, (x + 2, y - 2))
        Renderer.blit(surface, text_surface, (x - 2, y + 2))
        Renderer.blit(surface, text_surface, (x - 2, y - 2))
        Renderer.blit(surface, text_surface, (x - 1, y + 1))
        Renderer.blit(surface, text_surface, (x - 1, y - 1))
        Renderer.blit(surface, text_surface, (x + 1, y + 1))
        Renderer.blit(surface, text_surface, (x + 1, y - 1))
        Renderer.blit(surface, text_surface, (x + 2, y))
        Renderer.blit(surface, text_surface, (x - 2, y))
        Renderer.blit(surface, text_surface, (x, y + 2))
        Renderer.blit(surface, text_surface, (x, y  - 2))

        text_surface = font.render(line, True, color)
        Renderer.blit(surface, text_surface, (x, y))
