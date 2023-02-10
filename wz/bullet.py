import pygame
from object import Object

class Bullet(Object):
    def __init__(
        self, type, color, width, height, x_speed, y_speed, terrain_size, side, coord_x=None, coord_y=None
    ):
        super().__init__(
            type, color, width, height, x_speed, y_speed, terrain_size, coord_x, coord_y
        )

        self.side = side

    def update(self):

        if self.side == 'l':
            self.coord_x -= self.speed_x

        elif self.side == 'r':
            self.coord_x += self.speed_x

        elif self.side == 'u':
            self.coord_y -= self.speed_y

        elif self.side == 'd':
            self.coord_y += self.speed_y

        if self.coord_x > self.terrain_width or self.coord_x < 0:
            return False

        if self.coord_y > self.terrain_height or self.coord_y < 0:
            return False
        
        self.rect = pygame.Rect(
            (self.coord_x, self.coord_y, self.width, self.height),
        )

        return True

    def draw(self):
        self.rect = pygame.draw.rect(
            self.screen,
            self.color,
            (self.coord_x, self.coord_y, self.width, self.height),
        )
