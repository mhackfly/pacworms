import tkinter

from extra_tools import color_scale_hexa
from extra_bitmaps import Icons
from pacworms_global import VAR, CONST

class MyWidgetsConfig:

    def __init__(self):

        self.my_widgets_datas = {

            # ===========
            #   BUTTONS
            # ===========

            "button_black_flat": {
                "color_foreground": CONST.Color.green_worm,
                "color_background": "BLACK",
                "color_active_foreground": "BLACK",
                "color_active_background": CONST.Color.green_worm,
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 1
            },
            "button_bitmap_icon": {
                "bitmap_color_foreground": "#B0E0E6",
                "color_foreground": "#000000",  # INOP
                "color_background": color_scale_hexa("#B0E0E6", 0.8),
                "color_active_foreground": "BLACK",  # INOP
                "color_active_background": CONST.Color.blue_medium,
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 1
            },
            "button_yellow_start": {
                "color_foreground": "YELLOW",
                "color_background": "BLACK",
                "color_active_foreground": "BLACK",
                "color_active_background": "YELLOW",
                "relief": "flat",
                "font": "Monospace 14 bold",
                "width": 1,
                "height": 1
            },
            "button_tabs": {
                "color_foreground": "BLACK",
                "color_background": CONST.WidgetsColor.frame_tabs,
                "color_active_foreground": "WHITE",
                "color_active_background": CONST.Color.green_worm,
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 10,
                "height": 2
            },
            "button_levels": {
                "color_foreground": "WHITE",
                "color_background": color_scale_hexa(CONST.Color.blue_medium, 0.7),
                "color_active_foreground": "WHITE",
                "color_active_background": CONST.Color.blue_medium,
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 2
            },
            "button_clear": {
                "color_foreground": "WHITE",
                "color_background": CONST.Color.red_warning,
                "color_active_foreground": "WHITE",
                "color_active_background": color_scale_hexa(CONST.Color.red_warning, 1.20),
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 2
            },
            "button_save": {
                "color_foreground": "BLACK",
                "color_background": CONST.Color.happy_yellow,
                "color_active_foreground": "BLACK",
                "color_active_background": color_scale_hexa(CONST.Color.happy_yellow, 1.20),
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 2
            },
            "button_test_level": {
                "color_foreground": "BLACK",
                "color_background": CONST.Color.happy_yellow,
                "color_active_foreground": "BLACK",
                "color_active_background": color_scale_hexa(CONST.Color.happy_yellow, 1.20),
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 2
            },
            "button_quit_editor": {
                "color_foreground": "WHITE",
                "color_background": CONST.WidgetsColor.frame_tabs,
                "color_active_foreground": "WHITE",
                "color_active_background": color_scale_hexa(CONST.WidgetsColor.frame_tabs, 1.20),
                "relief": "flat",
                "font": "Monospace 10 bold",
                "width": 1,
                "height": 2
            },

            # ===========
            #   LABELS
            # ===========

            "label_guides": {
                "color_foreground": "WHITE",
                "color_background": CONST.WidgetsColor.frame_grid_buttons,
                "relief": "flat",
                "font": "Monospace 10 bold",
                "justify": "right",
                "anchor": "e",  # n, ne, e, se, s, sw, w, nw, center
                "width": 7,
                "height": 2
            },

            # ===============
            #   OPTIONMENUS
            # ===============
            "option_menu_guides": {
                "relief": "flat",
                "font": "Monospace 10 bold",
                "color_foreground": "WHITE",
                "color_background": CONST.Color.special_color,
                "color_active_foreground": "WHITE",
                "color_active_background": color_scale_hexa(CONST.Color.special_color, 1.20),
                "highlight_thickness": 0,
                "color_highlight_background": CONST.Color.special_color,
                "width": 5,
                "height": 1,
                "menu_relief": "flat",
                "menu_font": "Monospace 10 bold",
                "menu_color_foreground": "WHITE",
                "menu_color_background": color_scale_hexa(CONST.Color.special_color, 0.70),
                "menu_color_active_foreground": "WHITE",
                "menu_color_active_background": CONST.Color.special_color
            },

            # ==============
            #   SCROLLBARS
            # ==============

            "scrollbar_grid": {
                "color_foreground": CONST.WidgetsColor.frame_grid_scroll,
                "color_background": color_scale_hexa(CONST.WidgetsColor.frame_grid_scroll, 1.00),
                "color_active_foreground": CONST.WidgetsColor.frame_tabs,
                "highlight_thickness": 1,
                "color_highlight_background": color_scale_hexa(CONST.WidgetsColor.frame_grid_scroll, 0.95),
                "relief": "flat",
            }

        }

        self.my_widgets_labels = {

            # ===========
            #   BUTTONS
            # ===========

            'DEFAULT': 'button_black_flat',

            'ICON': 'button_bitmap_icon',

            'EDITOR': 'button_black_flat',
            'OPTION': 'button_black_flat',
            'QUIT': 'button_black_flat',

            'START': 'button_yellow_start',
            'RANDOM': 'button_yellow_start',

            'FILES': 'button_tabs',
            'LEVELS': 'button_tabs',

            'WALLS': 'button_levels',
            'GALLERIES': 'button_levels',
            'WORMS': 'button_levels',
            'GUMS': 'button_levels',

            'CLEAR': 'button_clear',
            'CLEAR\nLEVEL': 'button_clear',
            'SAVE\nLEVEL': 'button_save',
            'TEST\nLEVEL': 'button_test_level',
            'QUIT\nEDITOR': 'button_quit_editor',

            # ==========
            #   LABELS
            # ==========

            'COLUMNS\nGUIDE': 'label_guides',
            'ROWS\nGUIDE': 'label_guides',

            # ===============
            #   OPTIONMENUS
            # ===============
            'GUIDES': 'option_menu_guides',
            'SERIES_NAME': 'option_menu_guides',

            # ==============
            #   SCROLLBARS
            # ==============
            'SCROLLBAR_GRID': "scrollbar_grid"

        }

    def get_datas(self, label):
        if label in self.my_widgets_labels:
            return self.my_widgets_datas[self.my_widgets_labels[label]]
        else:
            return self.my_widgets_datas[self.my_widgets_labels['DEFAULT']]

class MyButton(tkinter.Button):

    def __init__(self, parent, label):
        """
        :param parent:
        :param label:
        """

        tkinter.Button.__init__(self, parent)

        if label.startswith("ICON"):

            self.widget_config = VAR.my_widgets_config.get_datas("ICON")

            bitmap = tkinter.BitmapImage(data=Icons.icons_dict.get(label))
            bitmap.config(foreground=self.widget_config['bitmap_color_foreground'])
            self.config(image=bitmap)
            self.config(highlightthickness=3)
            self.image = bitmap

        else:

            self.widget_config = VAR.my_widgets_config.get_datas(label)

            self.config(text=label)
            self.config(highlightthickness=0)

            if self.widget_config['width'] > 1:
                self.config(width=self.widget_config['width'])

            if self.widget_config['height'] > 1:
                self.config(height=self.widget_config['height'])

        self.config(borderwidth=0)

        self.config(relief=self.widget_config['relief'])
        self.config(font=self.widget_config['font'])
        self.config(foreground=self.widget_config['color_foreground'])
        self.config(background=self.widget_config['color_background'])
        self.config(activeforeground=self.widget_config['color_active_foreground'])
        self.config(activebackground=self.widget_config['color_active_background'])
        self.config(highlightbackground=self.widget_config['color_background'])

    def set_state(self, state):
        """
        :param state:
        :return:
        """

        if state == 0:

            self.config(foreground=self.widget_config['color_foreground'])
            self.config(background=self.widget_config['color_background'])

        elif state == 1:

            self.config(foreground=self.widget_config['color_active_foreground'])
            self.config(background=self.widget_config['color_active_background'])

        else:

            self.config(background=self.widget_config['color_background'])
            self.config(state=tkinter.DISABLED)

class MyLabel(tkinter.Label):

    def __init__(self, parent, label):
        """
        :param parent:
        :param label:
        """
        tkinter.Label.__init__(self, parent)
        widget_config = VAR.my_widgets_config.get_datas(label)

        if widget_config['width'] > 1:
            self.config(width=widget_config['width'])

        if widget_config['height'] > 1:
            self.config(height=widget_config['height'])

        self.config(text=label)
        self.config(borderwidth=0)
        self.config(highlightthickness=0)

        self.config(justify=widget_config['justify'])
        self.config(anchor=widget_config['anchor'])
        self.config(relief=widget_config['relief'])
        self.config(font=widget_config['font'])
        self.config(foreground=widget_config['color_foreground'])
        self.config(background=widget_config['color_background'])

class MyOptionMenu(tkinter.OptionMenu):

    def __init__(self, parent, label, ma_variable, *item):

        tkinter.OptionMenu.__init__(self, parent, ma_variable, *item)
        widget_config = VAR.my_widgets_config.get_datas(label)

        if widget_config['width'] > 1:
            self.config(width=widget_config['width'])

        if widget_config['height'] > 1:
            self.config(height=widget_config['height'])

        self.config(borderwidth=0)
        self.config(indicatoron=0)

        self.config(highlightthickness=widget_config['highlight_thickness'])
        self.config(highlightbackground=widget_config['color_highlight_background'])

        self.config(relief=widget_config['relief'])
        self.config(font=widget_config['font'])
        self.config(foreground=widget_config['color_foreground'])
        self.config(background=widget_config['color_background'])
        self.config(activeforeground=widget_config['color_active_foreground'])
        self.config(activebackground=widget_config['color_active_background'])

        self["menu"].config(activeborderwidth=0)

        self["menu"].config(relief=widget_config['menu_relief'])
        self["menu"].config(font=widget_config['menu_font'])
        self["menu"].config(foreground=widget_config['menu_color_foreground'])
        self["menu"].config(background=widget_config['menu_color_background'])
        self["menu"].config(activeforeground=widget_config['menu_color_active_foreground'])
        self["menu"].config(activebackground=widget_config['menu_color_active_background'])

class MyScrollbar(tkinter.Scrollbar):

    def __init__(self, parent, label, orient):
        """
        :param parent:
        :param orient:
        """
        tkinter.Scrollbar.__init__(self, parent)
        widget_config = VAR.my_widgets_config.get_datas(label)

        self.config(orient=orient)

        self.config(highlightthickness=widget_config['highlight_thickness'])
        self.config(highlightbackground=widget_config['color_highlight_background'])

        self.config(background=widget_config['color_foreground'])
        self.config(troughcolor=widget_config['color_background'])
        self.config(activebackground=widget_config['color_active_foreground'])
        self.config(elementborderwidth=0)
        self.config(relief=widget_config['relief'])
        self.config(activerelief=widget_config['relief'])

class MyScale(tkinter.Scale):

    def __init__(self, parent, orient, start, stop, step):
        """
        :param parent:
        :param orient:
        :param start:
        :param stop:
        :param step:
        """
        tkinter.Scale.__init__(self, parent)
        self.parent = parent
        self.config(from_=start, to=stop)
        self.config(resolution=step)
        self.config(relief=tkinter.FLAT)
        self.config(sliderrelief=tkinter.FLAT)
        self.config(font="Monospace 10 bold")
        self.config(borderwidth=0)
        self.config(highlightthickness=0)
        self.config(background="green")
        self.config(troughcolor="black")
        self.config(orient=orient)
