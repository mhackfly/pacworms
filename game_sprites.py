import pygame
import pygame.gfxdraw

from extra_tools import GridCoords
from game_drawings import WormsSheet
from pacworms_global import CONST

class WormsSprites:

    def __init__(self):

        #
        # tableau des elements worms
        #
        self.worms_sprites_elements = []

        # creation de la feuille de dessin des worms
        # worms_sheet = WormsSheet()
        #
        worms_sheet_surface = WormsSheet().get_worms_sheet_surface().convert()

        #
        # creation d'une grille
        #
        self.grid_size = CONST.GridGame.size
        self.grid_width = CONST.SpriteSheetSize.width
        self.grid_height = CONST.SpriteSheetSize.height
        grid_coords = GridCoords(self.grid_width, self.grid_height, self.grid_size)

        #
        # creer les surfaces et blitter les elements worms
        #
        for line in range(self.grid_height):
            for column in range(self.grid_width):
                sprite = pygame.Surface((self.grid_size, self.grid_size))
                sprite.blit(worms_sheet_surface,
                            (0, 0),
                            (grid_coords.x[column], grid_coords.y[line], self.grid_size, self.grid_size))
                self.worms_sprites_elements.append(sprite)

    def show_elements(self, screen):
        """
        afficher tous les elements worms
        :param screen: screen
        :return:
        """
        indice_element = 0
        for line in range(self.grid_height):
            for column in range(self.grid_width):
                screen.blit(self.worms_sprites_elements[indice_element],
                            (0 + (self.grid_size * column),
                             0 + (self.grid_size * line)))
                indice_element += 1

    def get_element(self, worm_name, outline, element):
        """
        retourne un sprite worm
        :param worm_name: WORMY, BLINKY, PINKY, INKY, CLYDE, COBRA
        :param outline: true, false
        :param element: indice element 0 -> 24 ( self.grid_width = DefWorms.WIDTH )
        :return: sprite surface
        """
        indice_element = (((worm_name * 2) + outline) * self.grid_width) + element
        return self.worms_sprites_elements[indice_element]
