import tkinter
from pacworms_start import StartPacworms

def main():

    root_window = tkinter.Tk()

    StartPacworms(root_window)
    # StartPacworms(root_window).action_open_window_editor()

    root_window.mainloop()

if __name__ == '__main__':
    main()
