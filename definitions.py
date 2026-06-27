import pygame

class Renderer:
    def __init__(
        self,
        width: int = 1920,
        height: int = 1080,
        cell_size: int = 1,
        screen = pygame.display.set_mode((1280, 720))
    ):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = screen
