import pygame
from object import Object

class Npc(Object):
    def __init__(
        self, type, color, width, height, x_speed, y_speed, terrain_size, player, coord_x=None, coord_y=None
    ):
        super().__init__(
            type, color, width, height, x_speed, y_speed, terrain_size, coord_x, coord_y
        )

        self.player = player


    def update(self):
        if self.coord_x > self.player.coord_x:
            self.coord_x -= self.speed_x
        if self.coord_x < self.player.coord_x:
            self.coord_x += self.speed_x

        if self.coord_y > self.player.coord_y:
            self.coord_y -= self.speed_y
        if self.coord_y < self.player.coord_y:
            self.coord_y += self.speed_y
        
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
