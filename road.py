import numpy as np
import random

direction_dic = {'horizontal' : 0, 'vertical' : 1}
turn_dic = {'forward' : 0, 'left' : 1, 'right' : 2}

class Road:

    def __init__(self, size_road, direction = 0, init_pos = (0,0), size_matrix = (360,360), turn =0):
        self.enivronment = np.zeros(size_matrix)
        self._size_road = size_road
        self.direction = direction
        if self.direction == 0:
            self.pos_x = init_pos[0] + size_road // 2 + 1
            self.pos_y = init_pos[1] + 1
        else :
            self.pos_x = init_pos[0] + 1
            self.pos_y = init_pos[1] + size_road // 2 + 1
        self.turn = turn
        self.list_of_turns = []
        self.enivronment[self.pos_x][self.pos_y] = 1

    def get_road(self):
        return self.enivronment

    def show_road(self):
        print(self.enivronment)

    def add_segment(self,pos_new):
        self.pos_x = pos_new[0]
        self.pos_y = pos_new[1]
        self.enivronment[self.pos_x][self.pos_y] = 1

    def draw_road(self):
        if self._size_road%2 == 1:
            if self.direction == 0:
                for k in range(-(self._size_road //2), self._size_road //2):
                    self.enivronment[self.pos_x + k][self.pos_y] = 1
                self.enivronment[self.pos_x + (self._size_road//2) - 1][self.pos_y] = 2
                self.enivronment[self.pos_x - (self._size_road//2) - 1][self.pos_y] = 2
            else:
                for k in range(-(self._size_road //2), self._size_road //2):
                    self.enivronment[self.pos_x][self.pos_y + k] = 1
                self.enivronment[self.pos_x][self.pos_y + (self._size_road//2) - 1] = 2
                self.enivronment[self.pos_x][self.pos_y - (self._size_road//2) - 1] = 2
        else:
            if self.direction == 0:
                for k in range (-((self._size_road //2) + 1), (self._size_road //2) - 1):
                    self.enivronment[self.pos_x + k][self.pos_y] = 1
                self.enivronment[self.pos_x + (self._size_road //2) - 2][self.pos_y] = 2
                self.enivronment[self.pos_x -((self._size_road //2) + 1)][self.pos_y] = 2
            else :
                for k in range (-((self._size_road //2) + 1), (self._size_road //2) -1):
                    self.enivronment[self.pos_x][self.pos_y + k] = 1
                self.enivronment[self.pos_x][self.pos_y + (self._size_road //2) - 2] = 2
                self.enivronment[self.pos_x][self.pos_y -((self._size_road //2) + 1)] = 2


    def allow_turn(self):
        if self.pos_x - (self._size_road // 2 + 1) < 0 \
                or self.pos_x + (self._size_road // 2 + 1) > self.enivronment.shape[0] \
                or self.pos_y - (self._size_road // 2 + 1) < 0 \
                or self.pos_y + (self._size_road // 2 + 1) > self.enivronment.shape[1]: ## on tourne que si on est assez loin des bords
            return False
        elif len(self.list_of_turns) > 0:
            if ((self.pos_x - self.list_of_turns[-1][0])**2 + (self.pos_y - self.list_of_turns[-1][1])**2)**(1/2) \
                < (self._size_road // 2 + 1) : ## evite que la route se boucle dessus
                return False
        else:
            return True

    def way_to_turn(self):
        if self.allow_turn() == False:
            self.turn = 0
        else :
            x = random.random()
            if x < 0.33:
                self.turn = 0
            elif 0.33 <= x < 0.66:
                self.turn = 1
            else:
                self.turn = 2









