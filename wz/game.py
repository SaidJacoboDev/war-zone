import sys
import pygame
from player import Player
from npc import Npc
import random
from graphics_manager import GraphicsManager

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0

class Game():

    def __init__(self):
        self.TERRAIN_SIZE = self.WIDTH, self.HEIGHT = 1080, 720
        self.SCREEN = pygame.display.set_mode(self.TERRAIN_SIZE)
        
        self.score = 0
        self.font = pygame.font.Font(None, 30)

        self.graphics_manager = GraphicsManager()

        self.player = Player(
            type='player',
            color=WHITE, 
            coord_x=self.WIDTH / 2, 
            coord_y=self.HEIGHT / 2, 
            width=10, 
            height=10, 
            x_speed=0, 
            y_speed=0, 
            terrain_size=self.TERRAIN_SIZE
        )
        
        self.graphics_manager.add_object(self.player)

        self.game_over = False


    def run_logic(self):

        ## draw zone
        create_npc = random.randint(0, 100)
        if create_npc < 2:
            npc = Npc(
                type='npc',
                color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)), 
                coord_x=None, 
                coord_y=None, 
                width=10, 
                height=10, 
                x_speed=1, 
                y_speed=1, 
                terrain_size=self.TERRAIN_SIZE,
                player=self.player
            )
            self.graphics_manager.add_object(npc)

        self.graphics_manager.update()

        hit_bullets, hit_npcs  = self.graphics_manager.check_collision('bullet','npc')
        if hit_npcs:
            self.graphics_manager.remove_object(hit_npcs)

        if hit_bullets:
            self.graphics_manager.remove_object(hit_bullets)

        if hit_npcs:
            self.score += len(hit_npcs)
            print(self.score)

        player, hit_npcs  = self.graphics_manager.check_collision('player','npc')
        if hit_npcs:
            self.graphics_manager.remove_object(hit_npcs)
        
        if player:
            self.player.lifes -= 1
            print(f'vidas: {self.player.lifes}')
            if self.player.lifes < 1:
                self.game_over = True
        

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.change_speed(-5, side='l', axis='x')

                if event.key == pygame.K_d:
                    self.player.change_speed(5, side='r', axis='x',)

                if event.key == pygame.K_w:
                    self.player.change_speed(-5, side='u', axis='y')

                if event.key == pygame.K_s:
                    self.player.change_speed(5, side='d', axis='y')

                if event.key == pygame.K_SPACE:
                    bullet = self.player.shut()
                    self.graphics_manager.add_object(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.change_speed(0, axis='x')

                if event.key == pygame.K_d:
                    self.player.change_speed(0, axis='x')

                if event.key == pygame.K_w:
                    self.player.change_speed(0, axis='y')

                if event.key == pygame.K_s:
                    self.player.change_speed(0, axis='y')
        return False

    def display_frame(self):
        text = f'Vidas: {self.player.lifes}  Score: {self.score}'
        render_text = self.font.render(text, 0, WHITE)

        self.SCREEN.fill(BLACK)
        self.SCREEN.blit(render_text, (self.WIDTH-300, self.HEIGHT-50))
        self.graphics_manager.draw()   
        pygame.display.flip()





