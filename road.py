import numpy as np
import random

direction_dic = {'right' : 0, 'left' : 1, 'up' : 2, 'down' : 3}

mvt_with_dir_dic = {0 : (0,1), 1 : (0,-1), 2 : (-1,0), 3 : (1,0)}

turn_dic = {'forward' : 0, 'right' : 1, 'left' : 2}

change_dir_dic = {0 : [0,3,2], 1 : [1,2,3], 2 : [2,0,1], 3 : [3,1,0]} #on utilise les dictionnaires pour les changements de directions dans les virages

class Road:

    def __init__(self, size_road,  number_of_turn, turn = 0, direction = 0, init_pos = (0,0),
                 size_matrix = (360,360)):
        self.environment = np.zeros(size_matrix)
        self._size_road = size_road
        self.direction = direction

        if self.direction == 0:
            self.pos_y = init_pos[0] + self._size_road // 2 + 1
            self.pos_x = init_pos[1] + 1
        else :
            self.pos_y = init_pos[0] + 1
            self.pos_x = init_pos[1] + self._size_road // 2 + 1

        self.environment[self.pos_y][self.pos_x] = 1
        for k in range (size_matrix[0]):  ##on met des 2 sur les bords de la matrice
            self.environment[k][0] = 2
            self.environment[k][size_matrix[1] - 1] = 2
        for k in range (size_matrix[1]):
            self.environment[0][k] = 2
            self.environment[size_matrix[0] - 1][k] = 2

        self.turn = turn

        self.list_of_turns = [(self.pos_y, self.pos_x, self.turn)]
        self.path = [(self.pos_y, self.pos_x)]
        self.number_of_turn = number_of_turn



    def get_road(self):
        return self.environment

    def show_road(self):
        print(self.environment)

    def draw_road(self):
        if self._size_road%2 == 1:
            if self.direction == 0 or self.direction == 1:
                for k in range(-(self._size_road //2), self._size_road //2):
                    self.environment[self.pos_y + k][self.pos_x] = 1
                self.environment[self.pos_y + (self._size_road//2) - 1][self.pos_x] = 2
                self.environment[self.pos_y - (self._size_road//2) - 1][self.pos_x] = 2
            else:
                for k in range(self._size_road //2 + 1):
                    self.environment[self.pos_y][self.pos_x + k] = 1
                    self.environment[self.pos_y][self.pos_x - k] = 1
                self.environment[self.pos_y][self.pos_x + (self._size_road//2) - 1] = 2
                self.environment[self.pos_y][self.pos_x - (self._size_road//2) + 1] = 2
        else:
            if self.direction == 0:
                for k in range (-((self._size_road //2) + 1), (self._size_road //2) - 1):
                    self.environment[self.pos_y + k][self.pos_x] = 1
                self.environment[self.pos_y + (self._size_road //2) - 2][self.pos_x] = 2
                self.environment[self.pos_y -((self._size_road //2) + 1)][self.pos_x] = 2
            else :
                for k in range (-((self._size_road //2) + 1), (self._size_road //2) -1):
                    self.environment[self.pos_y][self.pos_x + k] = 1
                self.environment[self.pos_y][self.pos_x + (self._size_road //2) - 2] = 2
                self.environment[self.pos_y][self.pos_x -((self._size_road //2) + 1)] = 2

    def draw_end_of_road(self):
        if self._size_road%2 == 1:
            if self.direction == 0:
                for k in range(-(self._size_road //2), self._size_road //2):
                    self.environment[self.pos_y + k][self.pos_x] = 2
            else:
                for k in range(-(self._size_road //2), self._size_road //2):
                    self.environment[self.pos_y][self.pos_x + k] = 2
        else:
            if self.direction == 0:
                for k in range (-((self._size_road //2) + 1), (self._size_road //2) - 1):
                    self.environment[self.pos_y + k][self.pos_x] = 2
            else :
                for k in range (-((self._size_road //2) + 1), (self._size_road //2) -1):
                    self.environment[self.pos_y][self.pos_x + k] = 2

    def add_segment(self,pos_new):
        self.pos_y = pos_new[0]
        self.pos_x = pos_new[1]
        self.path.append((self.pos_y,self.pos_x))
        self.draw_road()

    def way_to_go(self):

        if self.pos_y - (self._size_road // 2 + 1) == 0:  ## on tourne quand on atteint les bords
            if self.direction == 0:
                self.turn = random.choice([0, 1])
            if self.direction == 1:
                self.turn = random.choice([0, 2])
            if self.direction == 2:
                self.turn = random.choice([1, 2])

        if self.pos_y + (self._size_road // 2 + 1) == self.environment.shape[0]:
            if self.direction == 0:
                self.turn = random.choice([0, 2])
            if self.direction == 1:
                self.turn = random.choice([0, 1])
            if self.direction == 3:
                self.turn = random.choice([1, 2])

        if self.pos_x - (self._size_road // 2 + 1) == 0:  ##ok dir
            if self.direction == 3:
                self.turn = random.choice([0, 2])
            if self.direction == 2:
                self.turn = random.choice([0, 1])
            if self.direction == 0:
                self.turn = random.choice([1, 2])

        if self.pos_x + (self._size_road // 2 + 1) == self.environment.shape[1]:
            if self.direction == 1:
                self.turn = random.choice([1, 2])
            if self.direction == 2:
                self.turn = random.choice([0, 2])
            if self.direction == 3:
                self.turn = random.choice([0, 1])

        elif len(self.list_of_turns) > 0:
            if ((self.pos_y - self.list_of_turns[-1][0]) ** 2 + (self.pos_x - self.list_of_turns[-1][1]) ** 2) ** (
                    1 / 2) \
                    < (self._size_road // 2 + 2):  ## evite que la route se boucle dessus
                self.turn = 0
        else:
            self.turn = random.choice([0, 1, 2])
        if self.turn in [1,2]:
            self.list_of_turns.append((self.pos_y, self.pos_x, self.turn))
        self.change_direction()

    def change_direction(self):
        self.direction = change_dir_dic[self.direction][self.turn]

    def next_slot(self):
        self.way_to_go()
        next_pos = (self.pos_y + mvt_with_dir_dic[self.direction][0],
                    self.pos_x + mvt_with_dir_dic[self.direction][1])
        self.add_segment(next_pos)
        print(self.direction)



    def continuous_road(self):
        while self.number_of_turn != 0:
            self.next_slot()
            if self.turn in [1,2]:
                self.number_of_turn -= 1
                print(1)
            elif self.environment[self.path[-1][0]][self.path[-1][1]] == 2:
                self.number_of_turn = 0
                self.draw_end_of_road()
