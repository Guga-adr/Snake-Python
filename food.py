import pygame
import random


class Food:
    def __init__(self, cell_size, width, height):
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.position = self.generate_food_position()

    def generate_food_position(self):
        x = (
            random.randint(10, (self.width - self.cell_size) // self.cell_size)
            * self.cell_size
        )
        y = (
            random.randint(10, (self.height - self.cell_size) // self.cell_size)
            * self.cell_size
        )
        return x, y

    def draw(self, screen, color):
        pygame.draw.rect(
            screen,
            color,
            (self.position[0], self.position[1], self.cell_size, self.cell_size),
        )
