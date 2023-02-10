import pygame
import random

class Object():
    def __init__(
        self, type, color, width, height, x_speed, y_speed, terrain_size, coord_x=None, coord_y=None
    ):
        self.type = type
        self.screen = pygame.display.get_surface()
        self.width = width
        self.height = height
        self.speed_x = x_speed
        self.speed_y = y_speed
        self.color = color
        self.terrain_width, self.terrain_height = terrain_size
        self.rect = None

        if coord_x == None and coord_y == None:
            side = random.randint(0,3)

            if side == 0:
                coord_x = 0
                coord_y = random.randint(0, self.terrain_height)
            elif side == 1:
                coord_x = self.terrain_width
                coord_y = random.randint(0, self.terrain_height)
            elif side == 2:
                coord_x = random.randint(0, self.terrain_width)
                coord_y = 0
            elif side == 3:
                coord_x = random.randint(0, self.terrain_width)
                coord_y = self.terrain_height
            
        self.coord_x = coord_x
        self.coord_y = coord_y

    @property
    def center(self):
        x = (self.coord_x + (self.width / 2))
        y = (self.coord_y + (self.height / 2))
        return (x, y)