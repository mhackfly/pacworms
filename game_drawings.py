import pygame
import pygame.gfxdraw

from extra_tools import color_scale, filled_aacircle, GridCoords
from pacworms_global import CONST

class WormsSheet:

    def __init__(self):

        self.sprites_worms_outline = 2

        #
        # definition d'une grille
        #
        self.grid_size = CONST.GridGame.size
        self.grid_width = CONST.SpriteSheetSize.width
        self.grid_height = CONST.SpriteSheetSize.height
        self.grid_coords = GridCoords(self.grid_width, self.grid_height, self.grid_size)

        #
        # calcul des coordonnees de trace des worms
        #
        self.worms_drawing_coords = WormsDrawingCoords(self.grid_size, self.sprites_worms_outline)

        #
        # creation de la surface du dessin des worms
        #
        self.worms_sheet_surface = pygame.Surface((self.grid_width * self.grid_size,
                                                   self.grid_height * self.grid_size))

        #
        # trace d'une grille
        #
        self.draw_grid()

        #
        # definition des couleurs
        #
        self.color_key = color_scale(CONST.Color.worm_color_key, 1.0)
        worms_colors = [CONST.Color.worm_wormy,
                        CONST.Color.worm_blinky,
                        CONST.Color.worm_pinky,
                        CONST.Color.worm_inky,
                        CONST.Color.worm_clyde,
                        CONST.Color.worm_cobra]

        #
        # dessin des worms
        #
        for i in range(0, 6):
            self.color_head = color_scale(worms_colors[i], 1.4)
            self.color_tail = color_scale(worms_colors[i], 0.7)
            self.color_body = color_scale(worms_colors[i], 1)
            self.color_outline = color_scale(worms_colors[i], 0.4)
            self.color_eyes_stuffy = color_scale(worms_colors[i], 0.4)
            self.outline_size = 0
            self.draw_worms_elements(i * 2)
            self.outline_size = self.sprites_worms_outline
            self.draw_worms_elements((i * 2) + 1)

    # -------------------------------------------------------------
    # FUNCTION : get_worms_sheet_surface
    #   Retourne la surface feuille des sprites
    # -------------------------------------------------------------
    def get_worms_sheet_surface(self):
        return self.worms_sheet_surface

    # -------------------------------------------------------------
    # FUNCTION : draw_grid
    #   Dessin de la grille
    # -------------------------------------------------------------
    def draw_grid(self):
        for h in range(self.grid_height):
            for w in range(self.grid_width):
                pygame.draw.rect(self.worms_sheet_surface, CONST.Color.snow4,
                                 [self.grid_coords.x[w], self.grid_coords.y[h],
                                  self.grid_size, self.grid_size], 1)

    # -------------------------------------------------------------
    # FUNCTION : draw_background
    #   Peindre le fond
    # -------------------------------------------------------------
    def draw_background(self, column, line, color):
        pygame.gfxdraw.box(self.worms_sheet_surface,
                           [self.grid_coords.x[column], self.grid_coords.y[line], self.grid_size, self.grid_size], color)

    # -------------------------------------------------------------
    # FUNCTION : draw_rect
    #   Position :
    #       +-+-+  +-+-+
    #      0|   |  | | |
    #       +---+  | | |
    #      1|   |  | | |
    #       +-+-+  +-+-+
    #               2 3
    # -------------------------------------------------------------
    def draw_rect(self, column, line, position, color):
        pygame.gfxdraw.box(self.worms_sheet_surface,
                           (self.worms_drawing_coords.rect_coords[position][0] + self.grid_coords.x[column],
                            self.worms_drawing_coords.rect_coords[position][1] + self.grid_coords.y[line],
                            self.worms_drawing_coords.rect_coords[position][2],
                            self.worms_drawing_coords.rect_coords[position][3]),
                           color)

    # -------------------------------------------------------------
    # FUNCTION : draw_small_outline
    #   Position :
    #       0 1
    #      +-+-+
    #     7| | |2
    #      +---+
    #     6| | |3
    #      +-+-+
    #       5 4
    # -------------------------------------------------------------
    def draw_small_outline(self, column, line, position, color):
        if self.outline_size > 0:
            pygame.gfxdraw.box(self.worms_sheet_surface,
                               (self.worms_drawing_coords.small_outline_coords[position][0] + self.grid_coords.x[column],
                                self.worms_drawing_coords.small_outline_coords[position][1] + self.grid_coords.y[line],
                                self.worms_drawing_coords.small_outline_coords[position][2],
                                self.worms_drawing_coords.small_outline_coords[position][3]),
                               color)

    # -------------------------------------------------------------
    # FUNCTION : draw_outline
    #   Position :
    #       0
    #     +-+-+
    #     |   |
    #    3+   +1
    #     |   |
    #     +-+-+
    #       2
    # -------------------------------------------------------------
    def draw_outline(self, column, line, position, color):
        if self.outline_size > 0:
            pygame.gfxdraw.box(self.worms_sheet_surface,
                               (self.worms_drawing_coords.outline_coords[position][0] + self.grid_coords.x[column],
                                self.worms_drawing_coords.outline_coords[position][1] + self.grid_coords.y[line],
                                self.worms_drawing_coords.outline_coords[position][2],
                                self.worms_drawing_coords.outline_coords[position][3]),
                               color)

    # -------------------------------------------------------------
    # FUNCTION : draw_eyes
    # -------------------------------------------------------------
    def draw_eyes(self, column, line, direction, color):
        pygame.gfxdraw.box(self.worms_sheet_surface,
                           (self.worms_drawing_coords.eyes_coords[direction][0][0] + self.grid_coords.x[column],
                            self.worms_drawing_coords.eyes_coords[direction][0][1] + self.grid_coords.y[line],
                            self.worms_drawing_coords.eyes_coords[direction][0][2],
                            self.worms_drawing_coords.eyes_coords[direction][0][3]),
                           color)

        pygame.gfxdraw.box(self.worms_sheet_surface,
                           (self.worms_drawing_coords.eyes_coords[direction][1][0] + self.grid_coords.x[column],
                            self.worms_drawing_coords.eyes_coords[direction][1][1] + self.grid_coords.y[line],
                            self.worms_drawing_coords.eyes_coords[direction][1][2],
                            self.worms_drawing_coords.eyes_coords[direction][1][3]),
                           color)

    # -------------------------------------------------------------
    # FUNCTION : draw_stuffy
    # -------------------------------------------------------------
    def draw_stuffy(self, column, line, direction, color):
        pygame.gfxdraw.box(self.worms_sheet_surface,
                           (self.worms_drawing_coords.stuffy_coords[direction][0] + self.grid_coords.x[column],
                            self.worms_drawing_coords.stuffy_coords[direction][1] + self.grid_coords.y[line],
                            self.worms_drawing_coords.stuffy_coords[direction][2],
                            self.worms_drawing_coords.stuffy_coords[direction][3]),
                           color)

    # -------------------------------------------------------------
    # FUNCTION : draw_filled_circle
    # -------------------------------------------------------------
    def draw_filled_circle(self, column, line, color_outline, color_circle):
        grid_ray = int(self.grid_size / 2)
        x_center = self.grid_coords.x[column] + grid_ray
        y_center = self.grid_coords.y[line] + grid_ray
        if self.outline_size > 0:
            filled_aacircle(self.worms_sheet_surface, x_center, y_center, grid_ray, color_outline)
            filled_aacircle(self.worms_sheet_surface, x_center, y_center, grid_ray - self.outline_size, color_circle)
        else:
            filled_aacircle(self.worms_sheet_surface, x_center, y_center, grid_ray, color_circle)

    # -------------------------------------------------------------
    # FUNCTION : draw_worms_elements
    # -------------------------------------------------------------
    def draw_worms_elements(self, line):
        #
        # tete vers la droite
        #
        self.draw_background(0, line, self.color_key)
        self.draw_filled_circle(0, line, self.color_outline, self.color_head)
        self.draw_rect(0, line, 2, self.color_head)
        self.draw_small_outline(0, line, 0, self.color_outline)
        self.draw_small_outline(0, line, 5, self.color_outline)
        self.draw_eyes(0, line, 0, self.color_eyes_stuffy)
        
        #
        # tete vers la gauche
        #
        self.draw_background(1, line, self.color_key)
        self.draw_filled_circle(1, line, self.color_outline, self.color_head)
        self.draw_rect(1, line, 3, self.color_head)
        self.draw_small_outline(1, line, 1, self.color_outline)
        self.draw_small_outline(1, line, 4, self.color_outline)
        self.draw_eyes(1, line, 1, self.color_eyes_stuffy)
        
        #
        # tete vers le haut
        #
        self.draw_background(2, line, self.color_key)
        self.draw_filled_circle(2, line, self.color_outline, self.color_head)
        self.draw_rect(2, line, 1, self.color_head)
        self.draw_small_outline(2, line, 3, self.color_outline)
        self.draw_small_outline(2, line, 6, self.color_outline)
        self.draw_eyes(2, line, 2, self.color_eyes_stuffy)

        #
        # tete vers le bas
        #
        self.draw_background(3, line, self.color_key)
        self.draw_filled_circle(3, line, self.color_outline, self.color_head)
        self.draw_rect(3, line, 0, self.color_head)
        self.draw_small_outline(3, line, 7, self.color_outline)
        self.draw_small_outline(3, line, 2, self.color_outline)
        self.draw_eyes(3, line, 3, self.color_eyes_stuffy)

        #
        # queue vers la droite
        #
        self.draw_background(4, line, self.color_key)
        self.draw_filled_circle(4, line, self.color_outline, self.color_tail)
        self.draw_rect(4, line, 3, self.color_tail)
        self.draw_small_outline(4, line, 1, self.color_outline)
        self.draw_small_outline(4, line, 4, self.color_outline)

        #
        # queue vers la gauche
        #
        self.draw_background(5, line, self.color_key)
        self.draw_filled_circle(5, line, self.color_outline, self.color_tail)
        self.draw_rect(5, line, 2, self.color_tail)
        self.draw_small_outline(5, line, 0, self.color_outline)
        self.draw_small_outline(5, line, 5, self.color_outline)

        #
        # queue vers le haut
        #
        self.draw_background(6, line, self.color_key)
        self.draw_filled_circle(6, line, self.color_outline, self.color_tail)
        self.draw_rect(6, line, 0, self.color_tail)
        self.draw_small_outline(6, line, 7, self.color_outline)
        self.draw_small_outline(6, line, 2, self.color_outline)

        #
        # queue vers le bas
        #
        self.draw_background(7, line, self.color_key)
        self.draw_filled_circle(7, line, self.color_outline, self.color_tail)
        self.draw_rect(7, line, 1, self.color_tail)
        self.draw_small_outline(7, line, 3, self.color_outline)
        self.draw_small_outline(7, line, 6, self.color_outline)

        #
        # retour vers la droite
        #
        self.draw_background(8, line, self.color_key)
        self.draw_filled_circle(8, line, self.color_outline, self.color_body)
        self.draw_rect(8, line, 3, self.color_body)
        self.draw_small_outline(8, line, 1, self.color_outline)
        self.draw_small_outline(8, line, 4, self.color_outline)

        #
        # retour vers la gauche
        #
        self.draw_background(9, line, self.color_key)
        self.draw_filled_circle(9, line, self.color_outline, self.color_body)
        self.draw_rect(9, line, 2, self.color_body)
        self.draw_small_outline(9, line, 0, self.color_outline)
        self.draw_small_outline(9, line, 5, self.color_outline)

        #
        # retour vers le haut
        #
        self.draw_background(10, line, self.color_key)
        self.draw_filled_circle(10, line, self.color_outline, self.color_body)
        self.draw_rect(10, line, 0, self.color_body)
        self.draw_small_outline(10, line, 7, self.color_outline)
        self.draw_small_outline(10, line, 2, self.color_outline)

        #
        # retour vers le bas
        #
        self.draw_background(11, line, self.color_key)
        self.draw_filled_circle(11, line, self.color_outline, self.color_body)
        self.draw_rect(11, line, 1, self.color_body)
        self.draw_small_outline(11, line, 3, self.color_outline)
        self.draw_small_outline(11, line, 6, self.color_outline)

        #
        # coude bas vers droite
        #
        self.draw_background(12, line, self.color_key)
        self.draw_filled_circle(12, line, self.color_outline, self.color_body)
        self.draw_rect(12, line, 1, self.color_body)
        self.draw_rect(12, line, 3, self.color_body)
        self.draw_small_outline(12, line, 1, self.color_outline)
        self.draw_small_outline(12, line, 6, self.color_outline)

        #
        # coude bas vers gauche
        #
        self.draw_background(13, line, self.color_key)
        self.draw_filled_circle(13, line, self.color_outline, self.color_body)
        self.draw_rect(13, line, 1, self.color_body)
        self.draw_rect(13, line, 2, self.color_body)
        self.draw_small_outline(13, line, 0, self.color_outline)
        self.draw_small_outline(13, line, 3, self.color_outline)

        #
        # coude haut vers droite
        #
        self.draw_background(14, line, self.color_key)
        self.draw_filled_circle(14, line, self.color_outline, self.color_body)
        self.draw_rect(14, line, 0, self.color_body)
        self.draw_rect(14, line, 3, self.color_body)
        self.draw_small_outline(14, line, 4, self.color_outline)
        self.draw_small_outline(14, line, 7, self.color_outline)

        #
        # coude haut vers gauche
        #
        self.draw_background(15, line, self.color_key)
        self.draw_filled_circle(15, line, self.color_outline, self.color_body)
        self.draw_rect(15, line, 0, self.color_body)
        self.draw_rect(15, line, 2, self.color_body)
        self.draw_small_outline(15, line, 2, self.color_outline)
        self.draw_small_outline(15, line, 5, self.color_outline)

        #
        # corps vers la droite
        #
        self.draw_background(16, line, self.color_body)
        self.draw_outline(16, line, 0, self.color_outline)
        self.draw_outline(16, line, 2, self.color_outline)
        # self.draw_text(str(1), 16, line, DefColor.BLACK)

        #
        # corps vers la gauche
        #
        self.draw_background(17, line, self.color_body)
        self.draw_outline(17, line, 0, self.color_outline)
        self.draw_outline(17, line, 2, self.color_outline)
        # self.draw_text(str(2), 17, line, DefColor.BLACK)

        #
        # corps vers le haut
        #
        self.draw_background(18, line, self.color_body)
        self.draw_outline(18, line, 1, self.color_outline)
        self.draw_outline(18, line, 3, self.color_outline)
        # self.draw_text(str(3), 18, line, DefColor.BLACK)

        #
        # corps vers le bas
        #
        self.draw_background(19, line, self.color_body)
        self.draw_outline(19, line, 1, self.color_outline)
        self.draw_outline(19, line, 3, self.color_outline)
        # self.draw_text(str(4), 19, line, DefColor.BLACK)

        #
        # dessus vers la droite
        #
        self.draw_background(20, line, self.color_key)
        self.draw_filled_circle(20, line, self.color_outline, self.color_head)
        self.draw_eyes(20, line, 0, self.color_eyes_stuffy)
        self.draw_stuffy(20, line, 0, self.color_eyes_stuffy)

        #
        # dessus vers la gauche
        #
        self.draw_background(21, line, self.color_key)
        self.draw_filled_circle(21, line, self.color_outline, self.color_head)
        self.draw_eyes(21, line, 1, self.color_eyes_stuffy)
        self.draw_stuffy(21, line, 1, self.color_eyes_stuffy)

        #
        # dessus vers le haut
        #
        self.draw_background(22, line, self.color_key)
        self.draw_filled_circle(22, line, self.color_outline, self.color_head)
        self.draw_eyes(22, line, 2, self.color_eyes_stuffy)
        self.draw_stuffy(22, line, 2, self.color_eyes_stuffy)

        #
        # dessus vers le bas
        #
        self.draw_background(23, line, self.color_key)
        self.draw_filled_circle(23, line, self.color_outline, self.color_head)
        self.draw_eyes(23, line, 3, self.color_eyes_stuffy)
        self.draw_stuffy(23, line, 3, self.color_eyes_stuffy)

        #
        # dessous
        #
        self.draw_background(24, line, self.color_key)
        self.draw_filled_circle(24, line, self.color_outline, self.color_tail)

class GumsSheet:

    def __init__(self):
        #
        # definition d'une grille
        #
        self.grid_size = CONST.GridGame.size
        self.grid_width = 6
        self.grid_height = 1
        self.grille = GridCoords(self.grid_width, self.grid_height, self.grid_size)
        
        #
        # creation de la surface du dessin des worms
        #
        self.gums_sheet_surface = pygame.Surface((self.grid_width * self.grid_size,
                                                  self.grid_height * self.grid_size))
        
        #
        # definition des couleurs
        #
        self.color_key = color_scale(CONST.GumsDatas.color_key, 1.0)
        
        #
        # dessin des gums
        #
        self.draw_gums(0)

    def draw_gum(self, column, line, ray, color):
        grid_ray = int(self.grid_size / 2)
        x_center = self.grille.x[column] + grid_ray
        y_center = self.grille.y[line] + grid_ray
        filled_aacircle(self.gums_sheet_surface, x_center, y_center, ray, color)

    def draw_background(self, column, line, color):
        pygame.gfxdraw.box(self.gums_sheet_surface,
                           [self.grille.x[column], self.grille.y[line], self.grid_size, self.grid_size], color)

    def draw_gums(self, line):
        self.draw_background(0, line, self.color_key)
        self.draw_gum(0, line, CONST.GumsDatas.ray, color_scale(CONST.GumsDatas.color_1, 0.9))

        self.draw_background(1, line, self.color_key)
        self.draw_gum(1, line, CONST.GumsDatas.ray, color_scale(CONST.GumsDatas.color_2, 0.9))

        self.draw_background(2, line, self.color_key)
        self.draw_gum(2, line, CONST.GumsDatas.ray, color_scale(CONST.GumsDatas.color_3, 0.9))

        self.draw_background(3, line, self.color_key)
        self.draw_gum(3, line, CONST.GumsDatas.ray, color_scale(CONST.GumsDatas.color_4, 0.9))

        self.draw_background(4, line, self.color_key)
        self.draw_gum(4, line, CONST.GumsDatas.ray, color_scale(CONST.GumsDatas.color_5, 0.9))

        self.draw_background(5, line, self.color_key)
        self.draw_gum(5, line, CONST.GumsDatas.ray, color_scale(CONST.GumsDatas.color_6, 0.9))

    def get_gums_sheet_surface(self):
        return self.gums_sheet_surface

class WormsDrawingCoords:

    def __init__(self, grid_step, outline):

        self.grid_step = grid_step
        self.outline = outline

        self.eyes_coords = []
        self.stuffy_coords = []
        self.rect_coords = []
        self.outline_coords = []
        self.small_outline_coords = []
 
        self.init_eyes_coords()
        self.init_stuffy_coords()
        self.init_rect_coords()
        self.init_outline_coords()
        self.init_small_outline_coords()

    def init_eyes_coords(self):
        eyes_pos = int(self.grid_step / 2)
        eyes_offset = int(self.grid_step / 4)
        eyes_size = int(self.grid_step / 10) + 0  # eyes zoom
        x1 = eyes_offset
        x2 = eyes_pos
        x3 = self.grid_step - (eyes_pos + eyes_size)
        x4 = self.grid_step - (eyes_offset + eyes_size)
        y1 = eyes_offset
        y2 = eyes_pos
        y3 = self.grid_step - (eyes_pos + eyes_size)
        y4 = self.grid_step - (eyes_offset + eyes_size)
        self.eyes_coords = [
            [[x3, y1, eyes_size, eyes_size], [x3, y4, eyes_size, eyes_size]],  # droite
            [[x2, y1, eyes_size, eyes_size], [x2, y4, eyes_size, eyes_size]],  # gauche
            [[x1, y2, eyes_size, eyes_size], [x4, y2, eyes_size, eyes_size]],  # haut
            [[x1, y3, eyes_size, eyes_size], [x4, y3, eyes_size, eyes_size]]  # bas
        ]

    def init_stuffy_coords(self):
        stuffy_offset = int(self.grid_step / 3)
        stuffy_outline = int(self.grid_step / 10)
        stuffy_lenght = self.grid_step - (stuffy_offset * 2)
        x1 = stuffy_offset
        x2 = self.grid_step - (stuffy_offset + stuffy_outline)
        y1 = stuffy_offset
        y2 = self.grid_step - (stuffy_offset + stuffy_outline)
        self.stuffy_coords = [
            [x2, y1, stuffy_outline, stuffy_lenght],  # droite
            [x1, y1, stuffy_outline, stuffy_lenght],  # gauche
            [x1, y1, stuffy_lenght, stuffy_outline],  # haut
            [x1, y2, stuffy_lenght, stuffy_outline],  # bas
        ]

    def init_rect_coords(self):
        grid_ray = int(self.grid_step / 2)
        x1 = 0
        x2 = grid_ray + 1
        y1 = 0
        y2 = grid_ray + 1
        self.rect_coords = [
            [x1, y1, self.grid_step, grid_ray],
            [x1, y2, self.grid_step, grid_ray],
            [x1, y1, grid_ray, self.grid_step],
            [x2, y1, grid_ray, self.grid_step]
        ]

    def init_outline_coords(self):
        x1 = 0
        x2 = self.grid_step - self.outline
        y1 = 0
        y2 = self.grid_step - self.outline
        self.outline_coords = [
            [x1, y1, self.grid_step, self.outline],
            [x2, y1, self.outline, self.grid_step],
            [x1, y2, self.grid_step, self.outline],
            [x1, y1, self.outline, self.grid_step]
        ]

    def init_small_outline_coords(self):
        grid_ray = int(self.grid_step / 2)
        x1 = 0
        x2 = grid_ray + 1
        x3 = self.grid_step - self.outline
        y1 = 0
        y2 = grid_ray + 1
        y3 = self.grid_step - self.outline
        self.small_outline_coords = [
            [x1, y1, grid_ray, self.outline],
            [x2, y1, grid_ray, self.outline],
            [x3, y1, self.outline, grid_ray],
            [x3, y2, self.outline, grid_ray],
            [x2, y3, grid_ray, self.outline],
            [x1, y3, grid_ray, self.outline],
            [x1, y2, self.outline, grid_ray],
            [x1, y1, self.outline, grid_ray]
        ]
