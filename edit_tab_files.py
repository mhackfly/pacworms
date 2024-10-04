import tkinter

from pacworms_global import CONST

class FilesTab(tkinter.Frame):

    def __init__(self, parent):
        """
        :param parent:
        """
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(background=CONST.WidgetsColor.frame_level_buttons)
