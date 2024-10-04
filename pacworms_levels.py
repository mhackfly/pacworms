from pacworms_global import CONST

class Levels:

    def __init__(self):

        self.series = None
        self.number = None

        self.walls = GridElements()
        self.gallery = GridElements()
        self.worms = GridElements()
        self.gums = GridElements()

    def save(self):
        """

        :return:
        """
        pass

    def load(self):
        """

        :return:
        """
        pass

    def draw_walls_border(self):
        """
        bordure dans buffer walls
        :return:
        """

        for line in range(0, CONST.GridEditor.height):
            self.walls.set_foreground(CONST.EditGridElements.walls_value, 0, line)
            self.walls.set_foreground(CONST.EditGridElements.walls_value, CONST.GridEditor.width - 1, line)

        for column in range(0, CONST.GridEditor.width):
            self.walls.set_foreground(CONST.EditGridElements.walls_value, column, 0)
            self.walls.set_foreground(CONST.EditGridElements.walls_value, column, CONST.GridEditor.height - 1)

    def clear_walls(self):
        """
        éffacer le buffer walls
        :return:
        """

        for line in range(0, CONST.GridEditor.height):
            for column in range(0, CONST.GridEditor.width):
                self.walls.set_foreground(0, column, line)

class GridElements:

    def __init__(self):

        #
        #   initialisations
        #
        self.guides = [0] * (CONST.GridEditor.width * CONST.GridEditor.height)
        self.foreground = [0] * (CONST.GridEditor.width * CONST.GridEditor.height)
        self.background = [0] * (CONST.GridEditor.width * CONST.GridEditor.height)

    def show_foreground(self):
        """
        :return:
        """

        for l in range(0, CONST.GridEditor.height):
            print()
            for c in range(0, CONST.GridEditor.width):
                index = (l * CONST.GridEditor.width) + c
                print(self.foreground[index], end='')
        print()

    def set_foreground(self, value, column, line):
        """
        :param value:
        :param column:
        :param line:
        :return:
        """

        index = ((line - 1) * CONST.GridEditor.width) + (column - 1)
        self.foreground[index] = value

    def get_foreground(self, column, line):
        """
        :param column:
        :param line:
        :return:
        """

        index = ((line - 1) * CONST.GridEditor.width) + (column - 1)
        return self.foreground[index]

    def show_background(self):
        """
        :return:
        """

        for l in range(0, CONST.GridEditor.height):
            print()
            for c in range(0, CONST.GridEditor.width):
                index = (l * CONST.GridEditor.width) + c
                print(self.background[index], end='')
        print()

    def set_background(self, value, column, line):
        """
        :param value:
        :param column:
        :param line:
        :return:
        """

        index = ((line - 1) * CONST.GridEditor.width) + (column - 1)
        self.background[index] = value

    def get_background(self, column, line):
        """
        :param column:
        :param line:
        :return:
        """

        index = ((line - 1) * CONST.GridEditor.width) + (column - 1)
        return self.background[index]

    def show_guides(self):
        """
        :return:
        """

        for l in range(0, CONST.GridEditor.height):
            print()
            for c in range(0, CONST.GridEditor.width):
                index = (l * CONST.GridEditor.width) + c
                print(self.guides[index], end='')
        print()

    def set_guides(self, value, column, line):
        """
        :param value:
        :param column:
        :param line:
        :return:
        """

        index = ((line - 1) * CONST.GridEditor.width) + (column - 1)
        self.guides[index] = value

    def get_guides(self, column, line):
        """
        :param column:
        :param line:
        :return:
        """

        index = ((line - 1) * CONST.GridEditor.width) + (column - 1)
        return self.guides[index]
