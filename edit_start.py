import tkinter

from edit_tab_files import FilesTab
from edit_tab_level import LevelTab
from pacworms_global import CONST, VAR
from extra_widgets import MyButton

class StartEdit:

    def __init__(self, master):
        """
        :param master:
        """

        #
        #   save master
        #
        self.master = master
        # self.frame = tkinter.Frame(self.master)

        #
        #   init. window editor
        #
        tkinter.Tk.wm_title(self.master, "Toplevel Window Editor")
        tkinter.Tk.geometry(self.master, "%dx%d%+d%+d" %
                            (CONST.WindowEditorSize.width, CONST.WindowEditorSize.height, 340, 200))
        tkinter.Tk.config(self.master, background=CONST.WidgetsColor.frame_tabs, pady=2)
        tkinter.Tk.columnconfigure(self.master, 0, weight=1)
        tkinter.Tk.rowconfigure(self.master, 1, weight=1)

        #
        #   frames bars left and right -> GRID(0, 0)
        #
        frame_bar_left = tkinter.Frame(self.master, background=CONST.WidgetsColor.frame_tabs)
        frame_bar_right = tkinter.Frame(self.master, background=CONST.WidgetsColor.frame_tabs)

        frame_bar_left.grid(column=0, row=0, padx=2, pady=0, sticky="nsw")
        frame_bar_right.grid(column=0, row=0, padx=2, pady=0, sticky="nse")

        #
        #   lefts buttons
        #
        self.button_files = MyButton(frame_bar_left, "FILES")
        self.button_level = MyButton(frame_bar_left, "LEVELS")

        self.button_files.config(command=lambda: self.action_button_files())
        self.button_level.config(command=lambda: self.action_button_level())

        self.button_files.grid(column=0, row=0, padx=2, pady=1)
        self.button_level.grid(column=1, row=0, padx=2, pady=1)

        #
        #   rights buttons
        #
        self.button_quit_editor = MyButton(frame_bar_right, "QUIT\nEDITOR")
        self.button_quit_editor.config(command=lambda: self.action_button_quit())
        self.button_quit_editor.grid(column=0, row=0, padx=2, pady=1)

        #
        #   frames files and level -> GRID(0, 1)
        #
        self.tab_files = FilesTab(self.master)
        self.tab_files.grid(column=0, row=1, padx=1, pady=1, sticky="nsew")

        self.tab_level = LevelTab(self.master)
        self.tab_level.grid(column=0, row=1, padx=1, pady=1, sticky="nsew")

        #
        #   par defaut frame tab files
        #
        self.action_button_files()

    def action_button_quit(self):
        """
        :return:
        """

        VAR.Windows.editor = False
        tkinter.Tk.destroy(self.master)

    def action_button_files(self):
        """
        :return:
        """

        self.tab_files.tkraise()
        self.button_level.set_state(0)
        self.button_files.set_state(1)

    def action_button_level(self):
        """
        :return:
        """

        self.tab_level.tkraise()
        self.button_files.set_state(0)
        self.button_level.set_state(1)
