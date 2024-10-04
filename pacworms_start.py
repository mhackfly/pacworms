import tkinter

from tkinter.messagebox import askyesno
from pacworms_global import CONST, VAR
from pacworms_levels import Levels
from extra_widgets import MyWidgetsConfig, MyButton, MyOptionMenu, MyScale
from threading import Thread
from edit_start import StartEdit
from game_start import StartGame

class StartPacworms:

    def __init__(self, master):
        """

        :param master:
        """

        #
        #   initialiser variables globales
        #
        VAR.my_widgets_config = MyWidgetsConfig()
        VAR.levels = Levels()

        self.background_color = "BLACK"
        self.window_editor = None

        #
        #   init. serie, numero du tableau et fonction
        #   du widget option menu
        #
        self.level_series_name = tkinter.StringVar()
        self.level_number = ["Easy", "Medium", "Hard"]
        self.level_series_name.set(self.level_number[0])
        self.level_series_name.trace('w', lambda *args: self.action_change_series())

        #
        #
        # main window
        #
        self.master = master
        tkinter.Tk.title(self.master, "Root Window Start")
        tkinter.Tk.resizable(self.master, width=True, height=True)
        tkinter.Tk.geometry(self.master, "%dx%d%+d%+d" % (CONST.WindowStartSize.width,
                                                          CONST.WindowStartSize.height,
                                                          100,
                                                          100))
        tkinter.Tk.protocol(self.master, "WM_DELETE_WINDOW", self.action_quit_pacworms)

        # tkinter.Tk.rowconfigure(self.master, 0, weight=1)
        tkinter.Tk.rowconfigure(self.master, 1, weight=1)
        tkinter.Tk.rowconfigure(self.master, 2, weight=1)
        # tkinter.Tk.rowconfigure(self.master, 3, weight=1)
        # tkinter.Tk.rowconfigure(self.master, 4, weight=1)

        tkinter.Tk.columnconfigure(self.master, 0, weight=1)
        tkinter.Tk.columnconfigure(self.master, 1, weight=1)
        tkinter.Tk.columnconfigure(self.master, 2, weight=1)

        tkinter.Tk.config(self.master, background=self.background_color)

        #
        #   chargement des images
        #
        image_pacworms_title = tkinter.PhotoImage(file="pacwormstitle.gif")
        image_pacworms_logo = tkinter.PhotoImage(file="pacwormslogo.gif")

        #
        #   widgets label image PACWORMS title, LOGO
        #
        label_image_title = tkinter.Label(self.master, image=image_pacworms_title, background=self.background_color)
        label_image_title.image = image_pacworms_title

        label_image_logo = tkinter.Label(self.master, image=image_pacworms_logo, background=self.background_color)
        label_image_logo.image = image_pacworms_logo

        #
        #   widget button EDITOR, START, RANDOM, OPTION, QUIT
        #
        button_editor = MyButton(self.master, "EDITOR")
        button_editor.config(command=lambda: self.action_open_window_editor())

        button_start = MyButton(self.master, "START")
        button_start.config(command=lambda: self.action_open_window_game())

        button_random = MyButton(self.master, "RANDOM")
        button_option = MyButton(self.master, "OPTION")
        button_exit = MyButton(self.master, "QUIT")
        button_exit.config(command=lambda: self.action_quit_pacworms())

        #
        #   widget option menu series
        #
        option_menu_level_name = MyOptionMenu(self.master, "SERIES_NAME", self.level_series_name, *self.level_number)

        #
        #   widget scale level number
        #
        scale_level_number = MyScale(self.master, 'horizontal', 1, 16, 1)

        #
        #   placement des widgets -> GRID()
        #
        label_image_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsw")
        button_editor.grid(row=0, column=2, padx=10, pady=10, sticky="nse")

        label_image_logo.grid(row=1, column=0, columnspan=3)

        button_start.grid(row=2, column=0, columnspan=3)

        option_menu_level_name.grid(row=3, column=0, sticky="nse")
        scale_level_number.grid(row=3, column=1)
        button_random.grid(row=3, column=2, sticky="nsw")

        button_option.grid(row=4, column=0, padx=10, pady=10, sticky="nsw")
        button_exit.grid(row=4, column=2,  padx=10, pady=10, sticky="nse")

    def action_change_series(self):
        """

        :return:
        """

        print(self.level_series_name.get())

    def action_quit_pacworms(self):
        """

        :return:
        """

        result = tkinter.messagebox.askyesno("Confirmation :", "Quitter PACWORMS ?    ")
        if result:
            tkinter.Tk.quit(self.master)

    @staticmethod
    def action_open_window_game():
        """

        :return:
        """

        if VAR.Windows.game is False:
            wgt = WindowGameThread()
            wgt.daemon = True
            wgt.start()

    def action_open_window_editor(self):
        """
        Création d'une fenêtre fille Toplevel()
            -> window_editor
        :return:
        """

        if VAR.Windows.editor is False:
            VAR.Windows.editor = True
            self.window_editor = tkinter.Toplevel(self.master)
            self.window_editor.protocol("WM_DELETE_WINDOW", self.action_close_window_editor)
            StartEdit(self.window_editor)
        else:
            self.window_editor.focus_force()
            self.window_editor.deiconify()

    def action_close_window_editor(self):
        """

        :return:
        """

        VAR.Windows.editor = False
        self.window_editor.destroy()

class WindowGameThread(Thread):

    def __init__(self):
        """
        initialisation
        """

        Thread.__init__(self)

    def run(self):
        """

        :return:
        """

        StartGame()
