import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    CLOCK = pygame.time.Clock()

    done = False
    game = Game()

    while not done:
        done = game.process_events()
        done = game.game_over
        game.run_logic()
        game.display_frame()

        CLOCK.tick(60)

    pygame.quit()
