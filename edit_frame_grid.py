import tkinter

from extra_widgets import MyButton, MyLabel, MyOptionMenu, MyScrollbar
from extra_tools import GridCoords
from pacworms_global import CONST

toggle_button_scroll_erase = 0

class GridFrame(tkinter.LabelFrame):

    def __init__(self, parent, var_levels_elements):
        """
        creation cadre scrollable
        :param var_levels_elements:
        :param parent:
        """

        #
        #   initialisations
        #
        tkinter.LabelFrame.__init__(self, parent)
        self.parent = parent

        #
        #   récupérer le tableau des éléments a traiter
        #   walls ou gallery ou gums ou worms
        #   ex: -> self.grid_elements.show_foreground()
        #
        self.var_levels_elements = var_levels_elements

        #
        #   LabelFrame configure
        #
        self.config(foreground=CONST.WidgetsColor.grid_canvas_foreground, text="X = - Y = - (- x -)")
        self.config(relief=tkinter.FLAT)
        self.config(labelanchor="n")
        self.config(font="Monospace 8 bold italic")
        self.config(background=CONST.WidgetsColor.frame_grid_scroll)
        self.config(highlightthickness=CONST.WidgetsColor.frame_grid_highlight_thickness)
        self.config(highlightbackground=CONST.WidgetsColor.frame_grid_highlight_background)

        #
        #   init. variables
        #
        self.starting_drag_position = ()
        # self.starting_click_position = (1, 1)

        self.grid_pad = 1
        self.grid_width = CONST.GridEditor.width + self.grid_pad
        self.grid_height = CONST.GridEditor.height + self.grid_pad

        #
        #   creation objet : Grille
        #
        self.obj_grid_coords = GridCoords(self.grid_width, self.grid_height, CONST.GridEditor.size)

        #
        #   création du Canvas
        #
        self.canvas = tkinter.Canvas(self)

        #
        #   initialise scrollbars et canvas
        #   dessins de la grille et des regles
        #
        self.initialize()

    def initialize(self):
        """
        initialise scrollbars et canvas
        dessins de la grille et des guides
        :return:
        """

        #
        #   definition scrollbar vertical
        #
        vertical_scroll_bar = MyScrollbar(self, "SCROLLBAR_GRID", 'vertical')
        vertical_scroll_bar.config(command=self.canvas.yview, width=20)
        vertical_scroll_bar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)

        #
        #   definition scrollbar horizontal
        #
        horizontal_scroll_bar = MyScrollbar(self, "SCROLLBAR_GRID", 'horizontal')
        horizontal_scroll_bar.config(command=self.canvas.xview, width=20)
        horizontal_scroll_bar.pack(fill=tkinter.X, side=tkinter.BOTTOM, expand=tkinter.FALSE)

        #
        #   configure canvas
        #
        canvas_width = self.grid_width * CONST.GridEditor.size
        canvas_height = self.grid_height * CONST.GridEditor.size
        self.canvas.config(bd=0, highlightthickness=0)
        self.canvas.config(width=canvas_width, height=canvas_height)
        self.canvas.config(yscrollcommand=vertical_scroll_bar.set, xscrollcommand=horizontal_scroll_bar.set)
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
        self.canvas.pack(side=tkinter.LEFT, fill=tkinter.NONE, expand=tkinter.TRUE)
        self.canvas.config(background=CONST.WidgetsColor.grid_canvas_background)

        #
        #   views a 0
        #
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        #
        #   dragging canvas with mouse button 3
        #
        self.canvas.bind('<Motion>', self.show_mouse_coords)

        self.canvas.bind("<Button-3>", self.mouse_right_click)
        self.canvas.bind("<B3-Motion>", self.mouse_right_motion)
        self.canvas.bind("<ButtonRelease-3>", self.mouse_right_release)

        #
        #   dessin de la grille
        #
        for l in range(self.grid_pad, self.grid_height):
            for c in range(self.grid_pad, self.grid_width):
                self.canvas.create_rectangle(self.obj_grid_coords.x[c],
                                             self.obj_grid_coords.y[l],
                                             self.obj_grid_coords.x[c] + CONST.GridEditor.size - 1,
                                             self.obj_grid_coords.y[l] + CONST.GridEditor.size - 1,
                                             outline=CONST.WidgetsColor.grid_outline,
                                             fill=CONST.WidgetsColor.grid_background)

        #
        #   dessin des guides
        #
        offset = int(CONST.GridEditor.size / 2)
        text_color = ["#444444", "#888888"]
        for c in range(0, CONST.GridEditor.width):
            self.canvas.create_text(self.obj_grid_coords.x[c + self.grid_pad] + offset,
                                    self.obj_grid_coords.y[0] + offset,
                                    text="%d" % (c + 1),
                                    font="Monospace 6 bold",
                                    fill=text_color[c % 2])
        for l in range(0, CONST.GridEditor.height):
            self.canvas.create_text(self.obj_grid_coords.x[0] + offset,
                                    self.obj_grid_coords.y[l + self.grid_pad] + offset,
                                    text="%d" % (l + 1),
                                    font="Monospace 6 bold",
                                    fill=text_color[l % 2])

    def get_canvas(self):
        """
        :return: objet canvas
        """

        return self.canvas

    def get_grid_coords(self):
        """
        :return: objet grille
        """

        return self.obj_grid_coords

    def get_grid_position(self, x, y):
        """
        convertion (x, y) vers (colonne, ligne)
        :param x: position x
        :param y: positiom y
        :return: position dans la grille
        """

        column = int(self.canvas.canvasx(x) / CONST.GridEditor.size)
        line = int(self.canvas.canvasy(y) / CONST.GridEditor.size)
        return column, line

    def show_mouse_coords(self, event):
        """
        show mouse positions, column and line in the LabelFrame
        dans le LabelFrame
        :param event:
        :return:
        """

        column, line = self.get_grid_position(event.x, event.y)

        if self.test_mouse_coords(column, line):

            self.canvas.config(cursor="tcross")
            self.config(foreground=CONST.WidgetsColor.grid_canvas_foreground,
                        text="C = %d L = %d" % (column, line))

        else:

            self.canvas.config(cursor="")

    def mouse_right_click(self, event):
        """
        si toggle_button_scroll_erase = 0
            scroll de la grille
        si toggle_button_scroll_erase = 1
            effacer point par point dans la grille
                - column, line = self.get_grid_position(event.x, event.y)
                    recuperer les coordonnees colonne et ligne
                -  if self.test_mouse_coords(column, line)
                    si les coordonnees sont dans la grille
                - if self.grid_elements.get_foreground(column, line) == CONST.EditGridElements.walls_value
                    si le buffer level foreground vaut 1
                - self.draw_box_full(column, line, CONST.WidgetsColor.grid_background)
                - self.grid_elements.set_foreground(0, column, line)
                    effacer le point et fixer le buffer level a 0
        si toggle_button_scroll_erase = 2
            effacer une zone rectangulaire
        :param event:
        :return:
        """

        global toggle_button_scroll_erase

        if toggle_button_scroll_erase == 1:

            column, line = self.get_grid_position(event.x, event.y)

            if self.test_mouse_coords(column, line):

                if self.var_levels_elements.get_foreground(column, line) == CONST.EditGridElements.walls_value:

                    self.draw_box_full(column, line, CONST.WidgetsColor.grid_background)
                    self.var_levels_elements.set_foreground(0, column, line)

        elif toggle_button_scroll_erase == 2:

            pass

        else:

            self.canvas.config(xscrollincrement=3)
            self.canvas.config(yscrollincrement=3)
            self.starting_drag_position = (event.x, event.y)
            self.canvas.config(cursor="fleur")

    def mouse_right_motion(self, event):
        """
        :param event:
        :return:
        """

        global toggle_button_scroll_erase

        if toggle_button_scroll_erase == 0:

            delta_x = event.x - self.starting_drag_position[0]
            delta_y = event.y - self.starting_drag_position[1]
            self.canvas.xview('scroll', delta_x, 'units')
            self.canvas.yview('scroll', delta_y, 'units')
            self.starting_drag_position = (event.x, event.y)

        elif toggle_button_scroll_erase == 1:

            self.show_mouse_coords(event)

            column, line = self.get_grid_position(event.x, event.y)

            if self.test_mouse_coords(column, line):

                if self.var_levels_elements.get_foreground(column, line) == CONST.EditGridElements.walls_value:

                    self.draw_box_full(column, line, CONST.WidgetsColor.grid_background)
                    self.var_levels_elements.set_foreground(0, column, line)

        else:  # 2
            pass

    def mouse_right_release(self, event):
        """
        :param event:
        :return:
        """

        global toggle_button_scroll_erase

        if toggle_button_scroll_erase == 0:

            event.x = 0
            event.y = 0
            self.canvas.config(xscrollincrement=0)
            self.canvas.config(yscrollincrement=0)
            self.canvas.config(cursor="")

    def draw_box_outline(self, column, line, index):

        color = (CONST.WidgetsColor.grid_outline, "WHITE")
        self.canvas.create_rectangle(self.obj_grid_coords.x[column],
                                     self.obj_grid_coords.y[line],
                                     self.obj_grid_coords.x[column] + CONST.GridEditor.size - 1,
                                     self.obj_grid_coords.y[line] + CONST.GridEditor.size - 1,
                                     outline=color[index],
                                     fill='')

    def draw_box_full(self, column, line, color):

        self.canvas.create_rectangle(self.obj_grid_coords.x[column],
                                     self.obj_grid_coords.y[line],
                                     self.obj_grid_coords.x[column] + CONST.GridEditor.size - 1,
                                     self.obj_grid_coords.y[line] + CONST.GridEditor.size - 1,
                                     outline=CONST.WidgetsColor.grid_outline,
                                     fill=color)

    def draw_circle_full(self, column, line, color, size):

        self.canvas.create_oval(self.obj_grid_coords.x[column] + size,
                                self.obj_grid_coords.y[line] + size,
                                (self.obj_grid_coords.x[column] + CONST.GridEditor.size - 1) - size,
                                (self.obj_grid_coords.y[line] + CONST.GridEditor.size - 1) - size,
                                outline=CONST.WidgetsColor.grid_outline,
                                fill=color)

    def draw_worm_right(self):
        pass

    def draw_worm_left(self):
        pass

    def draw_worm_up(self):
        pass

    def draw_worm_down(self):
        pass

    @staticmethod
    def test_mouse_coords(column, line):
        """
        test if coords column and line is in the grid
        :param column:
        :param line:
        :return:
        """

        rules = [column > 0, line > 0, column <= CONST.GridEditor.width, line <= CONST.GridEditor.height]
        if all(rules):
            return True

        return False


class GridLeftToolsFrame(tkinter.Frame):

    def __init__(self, parent):
        """
        :param parent:
        """

        #
        #   initialisations
        #
        tkinter.Frame.__init__(self, parent)
        self.configure(background=CONST.WidgetsColor.frame_grid_buttons)

        #
        #   buttons CLEAR, ICON_ERASE_SCROLL, ICON_ERASE_POINT, ICON_ERASE_RECTANGLE
        #
        self.button_clear_grid = MyButton(self, "CLEAR")
        self.button_scroll = MyButton(self, "ICON_SCROLL")
        self.button_erase_point = MyButton(self, "ICON_ERASE_POINT")
        self.button_erase_rectangle = MyButton(self, "ICON_ERASE_RECTANGLE")

        self.button_clear_grid.config(command=lambda: self.action_button_clear_grid())
        self.button_scroll.config(command=lambda: self.action_button_scroll())
        self.button_erase_point.config(command=lambda: self.action_button_erase_point())
        self.button_erase_rectangle.config(command=lambda: self.action_button_erase_rectangle())

        self.button_clear_grid.grid(column=0, row=0, padx=2, pady=0)
        self.button_scroll.grid(column=1, row=0, padx=2, pady=0)
        self.button_erase_point.grid(column=2, row=0, padx=2, pady=0)
        self.button_erase_rectangle.grid(column=3, row=0, padx=2, pady=0)

        #
        #   par defaut erase scroll
        #
        self.action_button_erase_point()

    def action_button_clear_grid(self):
        """
        :return:
        """

        pass

    def action_button_scroll(self):
        """
        :return:
        """

        global toggle_button_scroll_erase

        self.button_erase_rectangle.set_state(0)
        self.button_erase_point.set_state(0)
        toggle_button_scroll_erase = 0
        self.button_scroll.set_state(1)

    def action_button_erase_point(self):
        """
        :return:
        """

        global toggle_button_scroll_erase

        self.button_erase_rectangle.set_state(0)
        self.button_scroll.set_state(0)
        toggle_button_scroll_erase = 1
        self.button_erase_point.set_state(1)

    def action_button_erase_rectangle(self):
        """
        :return:
        """

        global toggle_button_scroll_erase

        self.button_erase_point.set_state(0)
        self.button_scroll.set_state(0)
        toggle_button_scroll_erase = 2
        self.button_erase_rectangle.set_state(1)


class GridRightToolsFrame(tkinter.Frame):

    def __init__(self, parent, grid_frame):
        """
        :param parent:
        """

        #
        #   initialisations
        #
        tkinter.Frame.__init__(self, parent)
        self.configure(background=CONST.WidgetsColor.frame_grid_buttons)
        self.obj_grid_frame = grid_frame

        #
        #   columns
        #
        self.column_numbers_guide = [0]
        self.get_guides_numbers(CONST.GridEditor.width, self.column_numbers_guide)
        self.column_guide = tkinter.StringVar()
        self.column_guide.set(self.column_numbers_guide[0])
        self.column_guide.trace('w', lambda *args: self.action_column_guide())

        #
        #   rows
        #
        self.row_numbers_guide = [0]
        self.get_guides_numbers(CONST.GridEditor.height, self.row_numbers_guide)
        self.row_guide = tkinter.StringVar()
        self.row_guide.set(self.row_numbers_guide[0])
        self.row_guide.trace('w', lambda *args: self.action_row_guide())

        #
        #
        #
        label_column_guide = MyLabel(self, "COLUMNS\nGUIDE")
        label_row_guide = MyLabel(self, "ROWS\nGUIDE")

        self.option_menu_column_guide = MyOptionMenu(self, "GUIDES", self.column_guide, *self.column_numbers_guide)
        self.option_menu_row_guide = MyOptionMenu(self, "GUIDES", self.row_guide, *self.row_numbers_guide)

        label_column_guide.grid(column=0, row=0, padx=2, pady=0)
        self.option_menu_column_guide.grid(column=1, row=0, padx=2, pady=0)

        label_row_guide.grid(column=2, row=0, padx=2, pady=0)
        self.option_menu_row_guide.grid(column=3, row=0, padx=2, pady=0)

    def action_column_guide(self):
        """

        :return:
        """
        nb_columns = int(self.column_guide.get())
        if nb_columns > 0:
            column_cursor = 1
            nb_spaces = int(self.get_spaces(CONST.GridEditor.width, nb_columns))
            print(nb_columns, nb_spaces)
            for column in range(nb_columns):
                column_cursor += nb_spaces + 1
                self.obj_grid_frame.draw_box_full(column_cursor, 2, CONST.EditGridElements.guides_color_fg)

    def action_row_guide(self):
        """

        :return:
        """

        """
        selection = int(self.row_guide.get())
        if selection > 0:
            step = int(CONST.GridEditor.height / (selection + 1)) - 1
        for number in self.row_numbers_guide:
            print(self.get_step_guide(CONST.GridEditor.height, number))
        """

        pass

    def set_vertical_line_guide(self):
        """

        :return:
        """

        for column_index in range(1, CONST.GridEditor.height):

            self.obj_grid_frame.draw_box_full(2, 2, CONST.EditGridElements.guides_color_fg)

    def set_horizontal_line_guide(self):
        pass

    def get_guides_numbers(self, size, guides_numbers):

        guide_number = 1

        while True:

            spaces = self.get_spaces(size, guide_number)
            if spaces == int(spaces):
                guides_numbers.append(guide_number)
            if spaces == 1:
                break
            guide_number += 1

    @staticmethod
    def get_spaces(grid_editor_size, guide_number):

        return (grid_editor_size - (guide_number + 2)) / (guide_number + 1)
