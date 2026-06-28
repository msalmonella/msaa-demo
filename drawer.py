from typing import Literal
import pygame
import definitions

renderer = definitions.Renderer()

# cell_size = renderer.cell_size

rect_values: list[int] = [0, 0, renderer.cell_size * 100, renderer.cell_size * 100]


""" responsible for drawing grid on the screen. """
def draw_grid(screen) -> None:
    x_starting_value = rect_values[0]
    y_starting_value = rect_values[1]
    for _ in range(20):
        for _ in range(20):
            pygame.draw.rect(screen, "red", rect_values, 2)
            rect_values[0] += 100
        rect_values[0] = x_starting_value
        rect_values[1] += 100
    rect_values[1] = y_starting_value
