import pygame
from object import Object
from bullet import Bullet

class Player(Object):
    def __init__(
        self, type, color, width, height, x_speed, y_speed, terrain_size, coord_x=None, coord_y=None
    ):
        super().__init__(
            type, color, width, height, x_speed, y_speed, terrain_size, coord_x, coord_y
        )
        self.lifes = 3
        self.side = None

    def change_speed(self, speed, side=None, axis="x"):
        if axis == "x":
            self.speed_x = speed
        if axis == "y":
            self.speed_y = speed
        
        if side:
            self.side = side
        

    def update(self):
        self.coord_x += self.speed_x
        self.coord_y += self.speed_y
        
        if self.coord_x > self.terrain_width:
            self.coord_x = 0

        if self.coord_x < 0:
            self.coord_x = self.terrain_width

        if self.coord_y > self.terrain_height:
            self.coord_y = 0

        if self.coord_y < 0:
            self.coord_y = self.terrain_height
        
        self.rect = pygame.Rect(
            (self.coord_x, self.coord_y, self.width, self.height),
        )

        return True
    
    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.coord_x, self.coord_y, self.width, self.height),
        )

    def shut(self):
        RED = 255, 0, 0
        bullet = Bullet(
            type='bullet',
            color=RED, 
            coord_x=self.center[0], 
            coord_y=self.center[1], 
            width=3, 
            height=3, 
            x_speed=5, 
            y_speed=5, 
            side=self.side,
            terrain_size=(self.terrain_width, self.terrain_height),
        )

        return bullet
