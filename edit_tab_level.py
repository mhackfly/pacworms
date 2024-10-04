import tkinter

from extra_widgets import MyButton
from pacworms_global import CONST, VAR
from edit_frame_walls import WallsFrame
from edit_frame_gallery import GalleryFrame
from edit_frame_worms import WormsFrame
from edit_frame_gums import GumsFrame

class LevelTab(tkinter.Frame):

    def __init__(self, parent):
        """
        :param parent:
        """
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(background=CONST.WidgetsColor.frame_level_buttons)

        #
        #   centrer les cadres walls, galleries, worms, gums -> GRID(0, 0)
        #
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        #
        #   frames bars left and right -> GRID(0, 0)
        #
        frame_bar_left = tkinter.Frame(self, background=CONST.WidgetsColor.frame_level_buttons)
        frame_bar_right = tkinter.Frame(self, background=CONST.WidgetsColor.frame_level_buttons)

        frame_bar_left.grid(column=0, row=0, padx=1, pady=0, sticky="nsw")
        frame_bar_right.grid(column=0, row=0, padx=1, pady=0, sticky="nse")

        #
        #   lefts buttons
        #
        self.button_walls = MyButton(frame_bar_left, "WALLS")
        self.button_gallery = MyButton(frame_bar_left, "GALLERIES")
        self.button_worms = MyButton(frame_bar_left, "WORMS")
        self.button_gums = MyButton(frame_bar_left, "GUMS")

        self.button_walls.config(command=lambda: self.action_button_walls())
        self.button_gallery.config(command=lambda: self.action_button_gallery())
        self.button_worms.config(command=lambda: self.action_button_worms())
        self.button_gums.config(command=lambda: self.action_button_gums())

        self.button_walls.grid(column=0, row=0, padx=2, pady=1)
        self.button_gallery.grid(column=1, row=0, padx=2, pady=1)
        self.button_worms.grid(column=2, row=0, padx=2, pady=1)
        self.button_gums.grid(column=3, row=0, padx=2, pady=1)

        #
        #   rights buttons
        #
        self.button_test = MyButton(frame_bar_right, "TEST\nLEVEL")
        self.button_save = MyButton(frame_bar_right, "SAVE\nLEVEL")
        self.button_clear = MyButton(frame_bar_right, "CLEAR\nLEVEL")

        self.button_test.config(command=lambda: self.action_button_test())
        self.button_save.config(command=lambda: self.action_button_save())
        self.button_clear.config(command=lambda: self.action_button_clear())

        self.button_test.grid(column=0, row=0, padx=2, pady=1)
        self.button_save.grid(column=1, row=0, padx=2, pady=1)
        self.button_clear.grid(column=2, row=0, padx=2, pady=1)

        #
        #   frames walls, gallery, worms, gums -> GRID(0, 1)
        #
        self.walls_frame = WallsFrame(self)
        self.gallery_frame = GalleryFrame(self)
        self.worms_frame = WormsFrame(self)
        self.gums_frame = GumsFrame(self)

        self.walls_frame.grid(column=0, row=1, padx=3, pady=1, sticky="nsew")
        self.gallery_frame.grid(column=0, row=1, padx=3, pady=1, sticky="nsew")
        self.worms_frame.grid(column=0, row=1, padx=3, pady=1, sticky="nsew")
        self.gums_frame.grid(column=0, row=1, padx=3, pady=1, sticky="nsew")

        #
        #   par defaut walls button
        #
        self.action_button_walls()

    def action_button_walls(self):
        """
        :return:
        """

        self.walls_frame.tkraise()
        self.button_gallery.set_state(0)
        self.button_worms.set_state(0)
        self.button_gums.set_state(0)
        self.button_walls.set_state(1)

    def action_button_gallery(self):
        """
        :return:
        """

        self.gallery_frame.tkraise()
        self.button_walls.set_state(0)
        self.button_worms.set_state(0)
        self.button_gums.set_state(0)
        self.button_gallery.set_state(1)

    def action_button_worms(self):
        """
        :return:
        """

        self.worms_frame.tkraise()
        self.button_walls.set_state(0)
        self.button_gallery.set_state(0)
        self.button_gums.set_state(0)
        self.button_worms.set_state(1)

    def action_button_gums(self):
        """
        :return:
        """

        self.gums_frame.tkraise()
        self.button_walls.set_state(0)
        self.button_gallery.set_state(0)
        self.button_worms.set_state(0)
        self.button_gums.set_state(1)

    def action_button_test(self):
        """
        :return:
        """

        VAR.levels.walls.show_foreground()

    def action_button_save(self):
        """
        :return:
        """

        pass

    def action_button_clear(self):
        """
        :return:
        """

        pass
