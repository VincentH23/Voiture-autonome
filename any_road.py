import numpy as np
import random

direction_dic = {'right' : 0, 'left' : 1, 'up' : 2, 'down' : 3}

mvt_with_dir_dic = {0 : (0,1), 1 : (0,-1), 2 : (-1,0), 3 : (1,0)}

turn_dic = {'forward' : 0, 'right' : 1, 'left' : 2}

change_dir_dic = {0 : [0,3,2], 1 : [1,2,3], 2 : [2,0,1], 3 : [3,1,0]} #on utilise les dictionnaires pour les changements de directions dans les virages
class Any_road:

    def __init__(self, size_road, limit_of_turn, turn=0, direction=0, init_pos=(0, 0),
                 size_matrix=(360, 360)):
        self.map = np.zeros(size_matrix)
        self._size_road = size_road
        self.direction = direction
        self._size_matrix = size_matrix

        if self.direction == 0:
            self.pos_y = init_pos[0] + self._size_road + 2
            self.pos_x = init_pos[1] + 1
        else:
            self.pos_y = init_pos[0] + 1
            self.pos_x = init_pos[1] + self._size_road + 2


        self.map[self.pos_y][self.pos_x] = 1
        for k in range(self._size_matrix[0]):
            self.map[k][0] = 2
            self.map[k][-1] = 2

        for k in range(self._size_matrix[1]):
            self.map[0][k] = 2
            self.map[-1][k] = 2

        self.turn = turn

        self.list_of_turns = [(self.pos_y, self.pos_x, self.turn)]
        self.path = [(self.pos_y, self.pos_x,self.turn)]
        self.number_of_turn = 0
        self.limit_of_turn = limit_of_turn

        for j in range(self.pos_x,self.pos_x + 3*self._size_road + 1):
            for i in range(self.pos_y - self._size_road,self.pos_y + self._size_road):
                self.map[i][j] = 1
            self.path.append([[self.pos_y, j, self.turn]])
            self.map[self.pos_y + self._size_road][j] = 2
            self.map[self.pos_y - self._size_road - 1][j] = 2
        self.pos_x += 3*self._size_road


    def get_road(self):
        return self.map

    def show_road(self):
        print(self.map)


    def draw_road_segment(self):
        if self.direction in [0,1]:
            for k in range(self._size_road + 1):
                self.map[self.pos_y + k][self.pos_x] = 1
                self.map[self.pos_y - k][self.pos_x] = 1
            self.map[self.pos_y + self._size_road][self.pos_x] = 2
            self.map[self.pos_y - self._size_road - 1][self.pos_x] = 2
        else:
            self.map[self.pos_y][self.pos_x - self._size_road : self.pos_x + self._size_road + 1] = 1
            self.map[self.pos_y][self.pos_x + self._size_road + 1] = 2
            self.map[self.pos_y][self.pos_x - self._size_road - 1] = 2

    def draw_right_to_down(self):
        for k in range(self.pos_x - self._size_road, self.pos_x + self._size_road + 1):
            self.map[self.pos_y - 2*self._size_road - 2][k] = 2
        for k in range(self.pos_y - 2*self._size_road - 2, self.pos_y):
            self.map[k][self.pos_x + self._size_road + 1] = 2
        for i in range(self.pos_y - 2*self._size_road - 1, self.pos_y + 1):
            for j in range(self.pos_x - self._size_road, self.pos_x + self._size_road + 1):
                self.map[i][j] = 1
        self.map[self.pos_y - 1][self.pos_x - self._size_road - 1] = 2
        self.map[self.pos_y - 2*self._size_road -2][self.pos_x - self._size_road - 1] = 2
        for i in range(self.pos_y - 2 * self._size_road - 1, self.pos_y - 1):
            self.map[i][self.pos_x - self._size_road - 1] = 1

    def draw_right_to_up(self):
        for k in range(self.pos_x - self._size_road - 1, self.pos_x + self._size_road + 2):
            self.map[self.pos_y + 2*self._size_road + 1][k] = 2
        for k in range(self.pos_y, self.pos_y + 2*self._size_road + 2):
            self.map[k][self.pos_x + self._size_road + 1] = 2
        for i in range(self.pos_y, self.pos_y + 2*self._size_road + 1):
            for j in range(self.pos_x - self._size_road - 1, self.pos_x + self._size_road + 1):
                self.map[i][j] = 1
        self.map[self.pos_y - 1][self.pos_x - self._size_road - 1] = 2


    def draw_down_to_left(self):
        self.map[self.pos_y + self._size_road][self.pos_x : self.pos_x + 2*self._size_road + 2] = 2
        for k in range(self.pos_y - self._size_road - 1, self.pos_y + self._size_road + 1):
            self.map[k][self.pos_x + 2*self._size_road + 2] = 2
        for i in range(self.pos_y - self._size_road - 1, self.pos_y + self._size_road):
            for j in range(self.pos_x + 1, self.pos_x + 2*self._size_road + 2):
                self.map[i][j] = 1
        # for j in range(self.pos_x - 2*self._size_road - 1):
        #     self.map[self.pos_y + self._size_road + 1][j] = 1

    def draw_down_to_right(self):
        for i in range(self.pos_y - self._size_road - 1, self.pos_y + self._size_road):
            for j in range(self.pos_x - 2 * self._size_road - 2, self.pos_x):
                self.map[i][j] = 1
        self.map[self.pos_y + self._size_road][self.pos_x - 2 * self._size_road - 2: self.pos_x] = 2
        for k in range(self.pos_y - self._size_road - 1, self.pos_y + self._size_road + 1):
            self.map[k][self.pos_x - 2 * self._size_road - 2] = 2

    def draw_left_to_up(self):
        for i in range(self.pos_y - 1, self.pos_y + 2*self._size_road + 2):
            self.map[i][self.pos_x - self._size_road - 1] = 2
        for j in range(self.pos_x - self._size_road - 1,self.pos_x + self._size_road + 2):
            self.map[self.pos_y + 2*self._size_road + 1][j] = 2
        for i in range(self.pos_y, self.pos_y + 2*self._size_road + 1):
            for j in range(self.pos_x - self._size_road, self.pos_x + self._size_road + 1):
                self.map[i][j] = 1

    def draw_left_to_down(self):
        self.map[self.pos_y - 2 * self._size_road - 2][self.pos_x - self._size_road - 1: self.pos_x + self._size_road + 1] = 2
        for i in range(self.pos_y - 2 * self._size_road - 2, self.pos_y + 1):
            self.map[i][self.pos_x - self._size_road - 1] = 2
        for j in range(self.pos_x - self._size_road - 1, self.pos_x + self._size_road + 1):
            for i in range(self.pos_y - 2 * self._size_road - 1, self.pos_y + 1):
                self.map[i][j] = 1

    def draw_up_to_right(self):
        for j in range(self.pos_x - 2 * self._size_road - 2, self.pos_x + 1):
            self.map[self.pos_y - self._size_road - 1][j] = 2
        for i in range(self.pos_y - self._size_road - 1, self.pos_y + self._size_road + 1):
            self.map[i][self.pos_x - 2 * self._size_road - 2] = 2
        for i in range(self.pos_y - self._size_road, self.pos_y + self._size_road + 1):
            for j in range(self.pos_x - 2 * self._size_road - 1, self.pos_x):
                self.map[i][j] = 1

    def draw_up_to_left(self):
        for j in range(self.pos_x - 2 * self._size_road - 2, self.pos_x + 1):
            self.map[self.pos_y - self._size_road - 1][j] = 2
        for i in range(self.pos_y - self._size_road - 1, self.pos_y + self._size_road + 1):
            self.map[i][self.pos_x - 2 * self._size_road - 2] = 2
        for i in range(self.pos_y - self._size_road, self.pos_y + self._size_road + 1):
            for j in range(self.pos_x  - 2 * self._size_road - 1, self.pos_x + 1):
                self.map[i][j] = 1



    def add_segment(self,new_pos):
        self.pos_y = new_pos[0]
        self.pos_x = new_pos[1]
        self.path.append([self.pos_y, self.pos_x,self.turn])


    def possible_turn_0(self):
        distance = self.pos_x - [item for item in self.path if item[-1] == 1][-1][1]
        distance = abs(distance)
        if self._size_matrix[1] - self.pos_x - 2*self._size_road - 2 < 0:
            self.number_of_turn = self.limit_of_turn
        elif distance <= 1:
            self.turn = 0
        elif self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2 or self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
            if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2:
                if self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2:
                    self.turn = 2
                else:
                    if distance >= 2*self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 2
                        else:
                            self.turn = 0
            elif self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                if self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2:
                    self.turn = 1
                else:
                    if distance >= 2 * self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 1
                        else:
                            self.turn = 0
            if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2 and self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                self.turn = 0
        else:
            if self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2:
                x = random.random()
                if x > 0.5:
                    self.turn = 1
                else:
                    self.turn = 2
            elif distance >= 2*self._size_road + 2:
                x = random.random()
                if 0 <= x < 0.33:
                    self.turn = 0
                elif 0.33 <= x < 0.66:
                    self.turn = 1
                else:
                    self.turn = 2


    def possible_turn_1(self):
        distance = self.pos_x - [item for item in self.path if item[-1] == 1][-1][1]
        distance = abs(distance)
        if self.pos_x - 2*self._size_road - 2 < 0:
            self.number_of_turn = self.limit_of_turn
        elif distance <= 1:
            self.turn = 0
        elif self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2 or self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
            if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2:
                if self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
                    self.turn = 1
                else:
                    if distance >= 2*self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 1
                        else:
                            self.turn = 0
            elif self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                if self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
                    self.turn = 2
                else:
                    if distance >= 2 * self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 1
                        else:
                            self.turn = 0
            if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2 and self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                self.turn = 0
        else:
            if self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
                x = random.random()
                if x > 0.5:
                    self.turn = 1
                else:
                    self.turn = 2
            elif distance >= 2*self._size_road + 2:
                x = random.random()
                if 0 <= x < 0.33:
                    self.turn = 0
                elif 0.33 <= x < 0.66:
                    self.turn = 1
                else:
                    self.turn = 2

    def possible_turn_2(self):
        distance = self.pos_y - [item for item in self.path if item[-1] == 1][-1][0]
        distance = abs(distance)
        if self.pos_y - 2*self._size_road - 2 < 0:
            self.number_of_turn = self.limit_of_turn
        elif distance <= 1:
            self.turn = 0
        elif self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2 or self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
            if self.map[self.pos_y][self.pos_x + self._size_road + 2]:
                if self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                    self.turn = 2
                else:
                    if distance >= 2*self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 2
                        else:
                            self.turn = 0
            elif self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
                if self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                    self.turn = 1
                else:
                    if distance >= 2 * self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 1
                        else:
                            self.turn = 0
            if self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2 and self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
                self.turn = 0
        else:
            if self.map[self.pos_y - self._size_road - 2][self.pos_x] == 2:
                x = random.random()
                if x > 0.5:
                    self.turn = 1
                else:
                    self.turn = 2
            elif distance >= 2*self._size_road + 2:
                x = random.random()
                if 0 <= x < 0.33:
                    self.turn = 0
                elif 0.33 <= x < 0.66:
                    self.turn = 1
                else:
                    self.turn = 2

    def possible_turn_3(self):
        distance = self.pos_y - [item for item in self.path if item[-1] == 1][-1][0]
        distance = abs(distance)
        if self._size_matrix[0] - self.pos_y - 2*self._size_road - 2 < 0:
            self.number_of_turn = self.limit_of_turn
        elif distance <= 1:
            self.turn = 0
        elif self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2 or self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
            if self.map[self.pos_y][self.pos_x + self._size_road + 2]:
                if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2:
                    self.turn = 2
                else:
                    if distance >= 2*self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 2
                        else:
                            self.turn = 0
            elif self.map[self.pos_y][self.pos_x - self._size_road - 2]:
                if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2:
                    self.turn = 1
                else:
                    if distance >= 2 * self._size_road + 2:
                        x = random.random()
                        if x > 0.5:
                            self.turn = 1
                        else:
                            self.turn = 0
            if self.map[self.pos_y][self.pos_x + self._size_road + 2] == 2 and self.map[self.pos_y][self.pos_x - self._size_road - 2] == 2:
                self.turn = 0
        else:
            if self.map[self.pos_y + self._size_road + 2][self.pos_x] == 2:
                x = random.random()
                if x > 0.5:
                    self.turn = 1
                else:
                    self.turn = 2
            elif distance >= 2*self._size_road + 2:
                x = random.random()
                if 0 <= x < 0.33:
                    self.turn = 0
                elif 0.33 <= x < 0.66:
                    self.turn = 1
                else:
                    self.turn = 2

    def way_to_go(self):
        if self.map[self.pos_y][self.pos_x] == 2:
            self.number_of_turn = self.limit_of_turn


        else:
            if self.number_of_turn == 0:  ##obligé de faire ça car il y a une erreure d'indexage de liste sinon
                if self.pos_x + 2 * self._size_road + 4 - self._size_matrix[1] == 0:
                    self.turn = 1
                else:
                    x = random.random()
                    self.turn = 1
                    if x < 0.8:
                        self.turn = 0
                    else:
                        self.turn = 1
            elif self.direction == 0: ## si la voiture se dirige vers la droite
                self.possible_turn_0()

            elif self.direction == 1: ##si la voiture se dirige vers la gauche
                self.possible_turn_1()

            elif self.direction == 2: ##si la voiture se dirige vers le haut
                self.possible_turn_2()

            else:
                self.possible_turn_3()

    def next_slot(self):
        self.way_to_go()
        if self.turn != 0:
            self.number_of_turn += 1
            if self.direction == 0:
                if self.turn == 1:
                    new_pos = (self.pos_y + self._size_road + 1,self.pos_x + self._size_road + 1)
                    self.add_segment(new_pos)
                    self.draw_right_to_down()
                else:
                    new_pos = (self.pos_y - self._size_road - 1, self.pos_x + self._size_road + 1)
                    self.add_segment(new_pos)
                    self.draw_right_to_up()
            elif self.direction == 1:
                if self.turn == 2:
                    new_pos = (self.pos_y - self._size_road - 1, self.pos_x + self._size_road + 1)
                    self.add_segment(new_pos)
                    self.draw_left_to_up()
                else:
                    new_pos = (self.pos_y - self._size_road - 1, self.pos_x - self._size_road - 1)
                    self.add_segment(new_pos)
                    self.draw_left_to_down()
            elif self.direction == 2:
                if self.turn == 1:
                    new_pos = (self.pos_y - self._size_road - 1, self.pos_x + self._size_road + 1)
                    self.add_segment(new_pos)
                    self.draw_up_to_right()
                else:
                    new_pos = (self.pos_y - self._size_road - 1, self.pos_x - self._size_road - 1)
                    self.add_segment(new_pos)
                    self.draw_up_to_left()
            else:
                if self.turn == 2:
                    new_pos = (self.pos_y + self._size_road + 1, self.pos_x + self._size_road + 1)
                    self.add_segment(new_pos)
                    self.draw_down_to_right()
                else:
                    new_pos = (self.pos_y + self._size_road + 1, self.pos_x - self._size_road - 1)
                    self.add_segment(new_pos)
                    self.draw_down_to_left()
        else:
            new_pos = (self.pos_y + mvt_with_dir_dic[self.direction][0], self.pos_x + mvt_with_dir_dic[self.direction][1])
            self.draw_road_segment()
            self.add_segment(new_pos)

    def continuous_road(self):
        while self.number_of_turn != self.limit_of_turn:
            print(self.direction, self.turn,self.number_of_turn,self.pos_y,self.pos_x)
            self.next_slot()
            self.direction = change_dir_dic[self.direction][self.turn]
            self.turn = 0

