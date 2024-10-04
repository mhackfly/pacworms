import tkinter

from pacworms_global import CONST

class GalleryFrame(tkinter.Frame):

    def __init__(self, parent):
        """
        :param parent:
        """
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(background=CONST.WidgetsColor.frame_grid_buttons)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
