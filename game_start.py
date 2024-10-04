import os
import pygame

from pacworms_global import CONST
from game_sprites import WormsSprites

class StartGame:

    def __init__(self):

        window_game_size_width = (CONST.GridGame.width * CONST.GridGame.size) + (2 * CONST.GridGame.border)
        window_game_size_height = (CONST.GridGame.height * CONST.GridGame.size) + (2 * CONST.GridGame.border)
        window_game_size_x = (CONST.ScreenSize.width - window_game_size_width) / 2
        window_game_size_y = (CONST.ScreenSize.height - window_game_size_height) / 2

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_game_size_x, window_game_size_y)
        pygame.init()
        self.screen = pygame.display.set_mode((window_game_size_width, window_game_size_height), 0, 32)
        pygame.display.set_caption('Pygame window.')
        self.screen.fill(CONST.Color.black)

        worms_sprites = WormsSprites()
        worms_sprites.show_elements(self.screen)

        CONST.WindowStart = True

        while CONST.WindowStart:

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Pygame window closed.')
                    CONST.WindowStart = False
                    pygame.display.quit()

        print('End of thread...')
