import tkinter

from extra_widgets import MyButton
# from extra_tools import get_line_points

from edit_frame_grid import GridFrame, GridLeftToolsFrame, GridRightToolsFrame
from pacworms_global import CONST, VAR

class WallsFrame(tkinter.Frame):

    def __init__(self, parent):
        """
        :param parent:
        """
        tkinter.Frame.__init__(self, parent)
        # self.parent = parent
        self.configure(background=CONST.WidgetsColor.frame_grid_buttons)

        #
        #   centrer la grille -> GRID(0, 0)
        #
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        #
        #   init. variables
        #
        # self.mouse_left_right_pressed = False
        # self.walls_state_value = 0

        #
        #   frames bars left and right -> GRID(0, 0)
        #
        frames_bar_left = tkinter.Frame(self, background=CONST.WidgetsColor.frame_grid_buttons)

        frames_bar_left.grid(column=0, row=0, padx=0, pady=2, sticky="nsw")

        #
        #   lefts buttons
        #
        self.button_point = MyButton(frames_bar_left, "ICON_POINT")
        self.button_line = MyButton(frames_bar_left, "ICON_LINE")
        self.button_rectangle = MyButton(frames_bar_left, "ICON_RECTANGLE")
        self.button_filled_rectangle = MyButton(frames_bar_left, "ICON_FILLED_RECTANGLE")
        self.button_circle = MyButton(frames_bar_left, "ICON_CIRCLE")
        self.button_filled_circle = MyButton(frames_bar_left, "ICON_FILLED_CIRCLE")

        self.button_point.config(command=lambda: self.action_button_point())
        self.button_line.config(command=lambda: self.action_button_line())
        self.button_rectangle.config(command=lambda: self.action_button_rectangle())
        self.button_filled_rectangle.config(command=lambda: self.action_button_filled_rectangle())
        self.button_circle.config(command=lambda: self.action_button_circle())
        self.button_filled_circle.config(command=lambda: self.action_button_filled_circle())

        self.button_point.grid(column=0, row=0, padx=2, pady=1)
        self.button_line.grid(column=1, row=0, padx=2, pady=1)
        self.button_rectangle.grid(column=2, row=0, padx=2, pady=1)
        self.button_filled_rectangle.grid(column=3, row=0, padx=2, pady=1)
        self.button_circle.grid(column=4, row=0, padx=2, pady=1)
        self.button_filled_circle.grid(column=5, row=0, padx=2, pady=1)

        #
        #   right buttons
        #
        # ...

        #
        #   frames grid -> GRID(0, 1)
        #

        # create GridFrame with Walls
        self.obj_grid_frame = GridFrame(self, VAR.levels.walls)
        self.obj_grid_frame.grid(column=0, row=1)

        #
        #   frames bar left and right -> GRID(0, 2)
        #
        obj_grid_left_tools_frame = GridLeftToolsFrame(self)
        obj_grid_right_tools_frame = GridRightToolsFrame(self, self.obj_grid_frame)

        obj_grid_left_tools_frame.grid(column=0, row=2, sticky="nsw")
        obj_grid_right_tools_frame.grid(column=0, row=2, sticky="nse")

        #
        #   canvas mouses actions
        #
        self.canvas = self.obj_grid_frame.get_canvas()
        self.canvas.bind('<Button-1>', self.mouse_left_click)
        self.canvas.bind("<B1-Motion>", self.mouse_left_motion)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_left_release)

        # self.canvas.bind('<Button-3>', lambda event, arg1=0: self.mouse_left_right_click(event, arg1))
        # self.canvas.bind('<ButtonRelease-3>', self.mouse_left_right_release)

        #
        #   par defaut point button
        #
        self.action_button_point()

    def buttons_init(self):
        """
        :return:
        """

        self.button_point.set_state(0)
        self.button_line.set_state(0)
        self.button_rectangle.set_state(0)
        self.button_filled_rectangle.set_state(0)
        self.button_circle.set_state(0)
        self.button_filled_circle.set_state(0)

    def action_button_point(self):
        """
        :return:
        """

        self.buttons_init()
        self.button_point.set_state(1)

    def action_button_line(self):
        """
        :return:
        """

        self.buttons_init()
        self.button_line.set_state(1)

    def action_button_rectangle(self):
        """
        :return:
        """

        self.buttons_init()
        self.button_rectangle.set_state(1)

    def action_button_filled_rectangle(self):
        """
        :return:
        """

        self.buttons_init()
        self.button_filled_rectangle.set_state(1)

    def action_button_circle(self):
        """
        :return:
        """

        self.buttons_init()
        self.button_circle.set_state(1)

    def action_button_filled_circle(self):
        """
        :return:
        """

        self.buttons_init()
        self.button_filled_circle.set_state(1)

    def mouse_left_click(self, event):
        """
        - récuperer les coordonnées du clic gauche de la souris, colonne et ligne
        - 2 règles : les coordonnées colonne et ligne sont dans la grille et la case est vide
        - si ok : on affiche un point et on marque la case
        :param event:
        :return:
        """

        column, line = self.obj_grid_frame.get_grid_position(event.x, event.y)

        if self.obj_grid_frame.test_mouse_coords(column, line):

            if VAR.levels.walls.get_foreground(column, line) == 0:

                self.obj_grid_frame.draw_box_full(column, line, CONST.EditGridElements.walls_color_fg)
                VAR.levels.walls.set_foreground(CONST.EditGridElements.walls_value, column, line)

    def mouse_left_motion(self, event):
        """
        - afficher les coordonnées de la souris
        - récuperer les coordonnées du clic gauche de la souris, colonne et ligne
        - 2 règles : les coordonnées colonne et ligne sont dans la grille et la case est vide
        - si ok : on affiche un point et on marque la case
        :param event:
        :return:
        """

        self.obj_grid_frame.show_mouse_coords(event)

        column, line = self.obj_grid_frame.get_grid_position(event.x, event.y)

        if self.obj_grid_frame.test_mouse_coords(column, line):

            if VAR.levels.walls.get_foreground(column, line) == 0:

                self.obj_grid_frame.draw_box_full(column, line, CONST.EditGridElements.walls_color_fg)
                VAR.levels.walls.set_foreground(CONST.EditGridElements.walls_value, column, line)

    def mouse_left_release(self, event):
        """
        :param event:
        :return:
        """

        pass
