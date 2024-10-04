from extra_tools import color_scale_hexa

class CONST:

    class Color:

        green_worm = "#00B76E"
        blue_medium = "#4B92DB"
        red_warning = "#C36158"
        special_color = "#37474F"
        happy_yellow = "#FFE277"

        worm_color_key = color_scale_hexa(green_worm, 0.60)  # 74806C
        worm_wormy = "#60DA11"
        worm_blinky = "#E61920"
        worm_pinky = "#EF5496"
        worm_inky = "#6CCDDE"
        worm_clyde = "#F77B19"
        worm_cobra = "#23328D"

        black = (0, 0, 0)
        white = (255, 255, 255)
        snow2 = (238, 233, 233)
        snow3 = (205, 201, 201)
        snow4 = (139, 137, 137)
        royal_blue = (65, 105, 225)
        midnight_blue = (25, 25, 112)
        gray = (190, 190, 190)
        dark_slate_gray = (49, 79, 79)

    class ScreenSize:
        width = 1920
        height = 1080

    class WindowStartSize:
        width = 650
        height = 350

    class WindowEditorSize:
        width = 980
        height = 830

    class GridEditor:
        size = 19
        width = 41
        height = 25

    class GridGame:
        border = 0
        size = 19
        width = 30
        height = 20

    class SpriteSheetSize:
        width = 25
        height = 12

    class WidgetsColor:

        label_foreground = "WHITE"
        label_background = "BLACK"

        frame_tabs = "#808080"
        frame_level_buttons = color_scale_hexa(frame_tabs, 1.10)
        frame_grid_buttons = color_scale_hexa(frame_tabs, 1.20)

        frame_grid_scroll = color_scale_hexa(frame_tabs, 1.30)
        frame_grid_highlight_thickness = 1
        frame_grid_highlight_background = color_scale_hexa(frame_grid_scroll, 0.85)

        grid_scrollbar_background = color_scale_hexa(frame_grid_scroll, 0.95)
        grid_scrollbar_foreground = frame_grid_scroll
        grid_scrollbar_active_foreground = frame_tabs

        grid_canvas_foreground = "WHITE"
        grid_canvas_background = frame_grid_scroll

        # grid_foreground = color_scale_hexa(frame_grid_scroll, 1.40)
        grid_background = color_scale_hexa(frame_grid_scroll, 0.95)
        grid_outline = frame_grid_scroll

    class GumsDatas:
        ray = 4
        color_key = "#74806C"
        color_1 = "#60DA11"
        color_2 = "#E61920"
        color_3 = "#EF5496"
        color_4 = "#6CCDDE"
        color_5 = "#F77B19"
        color_6 = "#23328D"

    class WormsNames:
        (wormy, blinky, pinky, inky, clyde, cobra) = range(6)

    class WormsAttribute:
        (category, state, position, lenght, speed, direction, body) = range(7)

    class WormsState:
        (bad, good) = range(2)

    class Direction:
        (center, right, left, up, down,
         right_up, right_down,
         left_up, left_down,
         up_left, up_right,
         down_left, down_right) = range(13)

    class EditGridElements:

        walls_value = '1'
        walls_color_fg = "#E0E0E0"
        walls_color_bg = color_scale_hexa(walls_color_fg, 0.80)

        guides_value = '#'
        guides_color_fg = color_scale_hexa(walls_color_bg, 1.01)


class VAR:

    #
    #   dictionnaire configuration des widgets
    #
    my_widgets_config = None

    #
    #   objet levels : donnees des niveaux
    #
    levels = None

    #
    #   etat des fenetres : true ouverte false fermee
    #
    class Windows:

        game = False
        editor = False
