import pygame

class Renderer:
    def __init__(
        self,
        width: int = 1600,
        height: int = 900,
        cell_size: int = 1,
        screen = pygame.display.set_mode((1600, 900))
    ):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = screen
