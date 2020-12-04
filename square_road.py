import numpy as np
import random


direction_dic = {'vertical' : 0, 'horizontal' : 1}
turn_dic = {'forward' : 0, 'turn' : 1}
turn_to_dir_dic = {0 : 0, 1 : 1, 2 : 0, 3 : 1}
mvt_with_dir_dic = {0 : (0,1), 1 : (1,0), 2 : (0,-1), 3 : (-1,0)}

class Square_road:  ## pas de test pour init, set et get, qui sont reprises de road et qui fonctionnent
    def __init__(self, size_road, turn=0, direction=0, init_pos=(0, 0),
                 size_matrix=(360, 360)):
        self._size_matrix = size_matrix
        self.map = np.zeros(self._size_matrix)
        self._size_road = size_road
        self.turn = turn
        self.direction = direction

        if self.direction == 0:
            self.pos_y = init_pos[0] + self._size_road + 2
            self.pos_x = init_pos[1] + 1
        else :
            self.pos_y = init_pos[0] + 1
            self.pos_x = init_pos[1] + self._size_road + 2

        ## on met des 2 sur les bords pour que la voiture s'arrête
        for k in range(self._size_matrix[0]):
            self.map[k][0] = 2
            self.map[k][-1] = 2

        for k in range(self._size_matrix[1]):
            self.map[0][k] = 2
            self.map[-1][k] = 2


        self.path = [[self.pos_y, self.pos_x,self.turn]]
        self.number_of_turn = 0

        #init pour demarer way_to_go
        for j in range(self.pos_x,self.pos_x + 4*self._size_road):
            for i in range(self.pos_y - self._size_road,self.pos_y + self._size_road):
                self.map[i][j] = 1
                self.path.append([[i, j, self.turn]])
            self.map[self.pos_y + self._size_road][j] = 2
            self.map[self.pos_y - self._size_road - 1][j] = 2
        self.pos_x += 4*self._size_road


    def get_road(self):
        return self.map

    def show_road(self):
        print(self.map)

    def draw_road_segment(self):
        if self.direction == 0:
            for k in range(self._size_road):
                self.map[self.pos_y + k][self.pos_x] = 1
                self.map[self.pos_y - k][self.pos_x] = 1
            print(self.pos_y + self._size_road + 1,self.pos_x,self.map.shape)
            self.map[self.pos_y + self._size_road + 1][self.pos_x] = 2
            self.map[self.pos_y - self._size_road - 1][self.pos_x] = 2
        else:
            print(self.pos_y + self._size_road + 1, self.pos_x, self.map.shape)
            self.map[self.pos_y][self.pos_x - self._size_road : self.pos_x + self._size_road] = 1
            self.map[self.pos_y][self.pos_x + self._size_road + 1] = 2
            self.map[self.pos_y][self.pos_x - self._size_road - 1] = 2

    def draw_turn(self):
        if self.number_of_turn == 1:
            print(self.map.shape)
            self.map[self.pos_y - 2*self._size_road - 2][self.pos_x - self._size_road : self.pos_x + self._size_road + 1] = 2
            self.map[self.pos_y - 2*self._size_road - 2 : self.pos_y][self.pos_x + self._size_road + 1] = 2
            self.map[self.pos_y - 2*self._size_road - 1 : self.pos_y][self.pos_x - self._size_road : self.pos_x + self._size_road] = 1

        elif self.number_of_turn == 2:
            self.map[self.pos_y + self._size_road + 1][self.pos_x : self.pos_x + 2*self._size_road + 2] = 2
            self.map[self.pos_y - self._size_road : self.pos_y + self._size_road + 1][self.pos_x + 2*self._size_road + 2] = 2
            self.map[self.pos_y - self._size_road : self.pos_y + self._size_road][self.pos_x : self.pos_x + 2*self._size_road + 1] = 1

        elif self.number_of_turn == 3:
            self.map[self.pos_y + 2 * self._size_road + 2][self.pos_x - self._size_road - 1: self.pos_x + self._size_road] = 2
            self.map[self.pos_y: self.pos_y + 2 * self._size_road + 2][self.pos_x - self._size_road - 1] = 2
            self.map[self.pos_y: self.pos_y + 2 * self._size_road + 1][self.pos_x - self._size_road: self.pos_x + self._size_road] = 1

        else:
            self.map[self.pos_y - self._size_road - 1][self.pos_x - 2 * self._size_road - 2 : self.pos_x] = 2
            self.map[self.pos_y - self._size_road - 1: self.pos_y + self._size_road][self.pos_x - 2 * self._size_road - 2] = 2
            self.map[self.pos_y - self._size_road: self.pos_y + self._size_road][self.pos_x - 2 * self._size_road - 1 : self.pos_x] = 1

    def add_segment(self,new_pos):
        self.draw_road_segment()
        self.pos_y = new_pos[0]
        self.pos_x = new_pos[1]
        """if self.turn == 0:"""
        self.path.append([self.pos_y, self.pos_x,self.turn])

        """else :
            if self.number_of_turn == 1:
                for k in range(1,self._size_road + 1):
                    self.path.append([self.pos_y, self.pos_x - k,self.turn])
                    self.path.append([self.pos_y - k, self.pos_x,self.turn])
                self.path.append([self.pos_y - self._size_road, self.pos_x,self.turn])
            elif self.number_of_turn == 2:
                for k in range(1,self._size_road + 1):
                    self.path.append([self.pos_y, self.pos_x - k,self.turn])
                    self.path.append([self.pos_y + k, self.pos_x,self.turn])
                self.path.append([self.pos_y, self.pos_x + self._size_road,self.turn])
            elif self.number_of_turn == 3:
                for k in range(1,self._size_road + 1):
                    self.path.append([self.pos_y, self.pos_x + k,self.turn])
                    self.path.append([self.pos_y + k, self.pos_x,self.turn])
                self.path.append([self.pos_y + self._size_road, self.pos_x,self.turn])
            else:
                for k in range(1,self._size_road + 1):
                    self.path.append([self.pos_y, self.pos_x + k,self.turn])
                    self.path.append([self.pos_y + k, self.pos_x,self.turn])
                self.path.append([self.pos_y, self.pos_x - self._size_road,self.turn])
            self.draw_turn()"""

    def way_to_go(self):
        if self.direction == 0:
            if self.number_of_turn == 0:
                if self.pos_x + 2*self._size_road + 3 - self._size_matrix[1] == 0:
                    self.turn == 1
                else:
                    x = random.random()
                    if x > 0.9:
                        self.turn = 1
            elif self.number_of_turn in [1,2]:
                distance = self.pos_x - [item for item in self.path if item[-1] == 1][-1][1]
                if abs(distance) > 4*self._size_road:
                    x = random.random()
                    if x > 0.9:
                        self.turn = 1
                elif self.pos_x + 2*self._size_road + 3 - self._size_matrix[1] == 0 or self.pos_x - 2*self._size_road - 3 == 0:
                    self.turn = 1
            elif self.number_of_turn == 3:
                if self.pos_y == self.path[0][0]:
                    self.turn = 1
                else:
                    self.turn = 0
            else:
                self.turn = 1
        else:
            distance = self.pos_y - [item for item in self.path if item[-1] == 1][-1][0]
            if abs(distance) > 4 * self._size_road:
                x = random.random()
                if x > 0.9:
                    self.turn = 1
            elif self.pos_y + 2*self._size_road + 3 - self._size_matrix[0] == 0 or self.pos_y - self._size_road - 1 == 0:
                self.turn = 1

    def next_slot(self):
        self.way_to_go()
        if self.turn == 1:
            self.number_of_turn +=1
            if self.number_of_turn == 1:
                new_pos = (self.pos_y + self._size_road + 1,self.pos_x + self._size_road + 1)
            elif self.number_of_turn == 2:
                new_pos = (self.pos_y + self._size_road + 1,self.pos_x - self._size_road - 1)
            elif self.number_of_turn == 3:
                new_pos = (self.pos_y - self._size_road - 1,self.pos_x - self._size_road - 1)
            elif self.number_of_turn == 4:
                new_pos = (self.pos_y - self._size_road - 1,self.pos_x + self._size_road + 1)
        else:
            new_pos = (self.pos_y + mvt_with_dir_dic[self.number_of_turn][0],self.pos_x + mvt_with_dir_dic[self.number_of_turn][1])
        self.add_segment(new_pos)

    def continuous_road(self):
        while self.number_of_turn != 4:
            self.next_slot()
            print(self.number_of_turn)
            if self.number_of_turn < 4:
                self.direction = turn_to_dir_dic[self.number_of_turn]
            self.turn = 0