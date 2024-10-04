# from game_defines import DefWorms
from pacworms_global import CONST

class Worm:

    def __init__(self, worm_datas):
        """
        initialisation de l'objet worm
        :param worm_datas: donnees d'un worm dans une liste
        """
        self.category = worm_datas[0]
        self.state = worm_datas[1]
        self.position = worm_datas[3]  # x, y, z
        self.length = worm_datas[3]
        self.speed = worm_datas[4]
        self.direction = worm_datas[5]
        self.body = []

    def __getattr__(self, name):
        """
        Called when an attribute lookup has not found
        the attribute in the usual places
        :param name:
        :return:
        """
        return 'Worm class does not have `{}` attribute.'.format(str(name))

    def __setattr__(self, name, value):
        """
        Called when an attribute assignment is attempted
        :param name:
        :param value:
        :return:
        """
        self.__dict__[name] = value

    # def __setitem__(self, key, value):
    # pass

    def __str__(self):
        """
        ex: print(worms_list[0])
        afficher l'objet Worm
        :return:
        """
        category = ["NIBBLE", "DOC", "GRUMPY", "HAPPY", "SLEEPY", "DOPEY", "BASHFUL", "SNEEZY"]
        direction = ["CENTER", "RIGHT", "LEFT", "UP", "DOWN"]
        state = ["BAD", "GOOD"]
        out = ' {:<7} | {:<4} | {:03d} | {:03d} | {:02d} | {:01d} | {:<5}' \
            .format(category[self.category],
                    state[self.state],
                    self.position[0], self.position[1],
                    self.length,
                    self.speed,
                    direction[self.direction])
        return out

    def __len__(self):
        """
        :return: longueur d'un Worm
        """
        return self.length

    def get_attr(self, name):
        return self.__dict__[name]

class WormsList:

    def __init__(self):
        """
        creation de la liste des Worms
        """
        self.worm_list = []

    def __len__(self):
        """
        ex: print(len(worms_list))
        :return: nombre d'objet Worm dans la liste
        """
        return len(self.worm_list)

    def __getitem__(self, index):
        """
        ex: print(worms_list[0]), fait appel a Worm.__str__
        retourner un type Worm
        :param index: index liste
        :return: Worm type
        """
        return self.worm_list[index]

    def __setitem__(self, index, worm_datas):
        """
        ex: worms_list[0] = [DOC, GOOD, 0, 0, 8, 1, RIGHT]
        :param index: index du Worm a insere dans la liste
        :       si index en dehors -> ajouter a la fin de la liste
        :param worm_datas: donnees d'un Worm dans une liste
        :return:
        """
        self.worm_list.insert(index, Worm(worm_datas))

    def __cmp__(self, index1, index2):
        cat1 = self.__getitem__(index1).category
        cat2 = self.__getitem__(index2).category
        if cat1 == cat2:
            return True
        return False

    def add(self, worm_datas):
        """
        ajouter un Worm a la liste
        :param worm_datas: donnees a ajouter dans la liste
        :return:
        """
        # nombre d'element
        datas_size = len(worm_datas)
        # si = 6 ajouter directement un Worm a la liste
        if datas_size == 6:
            self.worm_list.append(Worm(worm_datas))
        # si = 7 ajouter 'worm_datas[-1]' Worm a la liste
        elif datas_size == 7:
            # nombre de Worm a ajouter
            repeat = worm_datas[-1]
            # supprimer la derniere valeur de 'worm_datas[]'
            del worm_datas[-1]
            # conditions pour ajouter plusieurs Worm a la liste
            if repeat > 1 and worm_datas[CONST.WormsAttribute.direction] > 4:
                """
                 0) CENTER
                 1) RIGHT
                 2) LEFT
                 3) UP
                 4) DOWN
                                                   int((index / 2) + 1)
                 5) (0 RIGHT_UP     -> x,y[0,-1]        1
                 6) (1 RIGHT_DOWN   -> x,y[0,1]         1
                 7) (2 LEFT_UP      -> x,y[0,-1]        2
                 8) (3 LEFT_DOWN    -> x,y[0,1]         2
                 9) (4 UP_LEFT      -> x,y[-1,0]        3
                10) (5 UP_RIGHT     -> x,y[1,0]         3
                11) (6 DOWN_LEFT    -> x,y[-1,0]        4
                12) (7 DOWN_RIGHT   -> x,y[1,0]         4
                """
                # direction de creation des Worms dans la grille [x,y]
                directions = ([0, -1], [0, 1],
                              [0, -1], [0, 1],
                              [-1, 0], [1, 0],
                              [-1, 0], [1, 0])
                # recuperer la direction de creation de plusieurs Worms
                # 5) RIGHT_UP ... 12) DOWN_RIGHT -> 0) RIGHT_UP ...  7) DOWN_RIGHT
                index = worm_datas[CONST.WormsAttribute.direction] - 5
                # fixer la direction
                worm_datas[CONST.WormsAttribute.direction] = int((index / 2) + 1)
                # ajouter plusieurs Worms dans la direction
                for i in range(repeat):
                    self.worm_list.append(Worm(worm_datas))
                    worm_datas[CONST.WormsAttribute.position][0] += directions[index][0]
                    worm_datas[CONST.WormsAttribute.position][1] += directions[index][1]
        else:
            pass

    def show(self):
        """
        affichage de tous les Worms de la liste
        :return:
        """
        for i in range(self.__len__()):
            print('{:03d})'.format(i), self.__getitem__(i))
