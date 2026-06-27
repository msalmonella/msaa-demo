from typing import Literal
import pygame
import definitions

renderer = definitions.Renderer()

# cell_size = renderer.cell_size

rect_values: list[int] = [0, 0, renderer.cell_size * 100, renderer.cell_size * 100]


def draw_grid(screen) -> None:
    for _ in range(5):
        pygame.draw.rect(screen, "blue", rect_values, 1)
        rect_values[0] = rect_values[0] + renderer.cell_size * 100
        for _ in range(5):
            pygame.draw.rect(screen, "blue", rect_values, 1)
            rect_values[1] = rect_values[1] + renderer.cell_size * 100
