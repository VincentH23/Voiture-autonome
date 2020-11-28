import road

import Voiture


class Environment:

    def __init__(self,size_road,  number_of_turn, x, y, n, p, init_pos = (0,0),
                 size_matrix = (360,360)):
        self.my_road = road.Road(size_road,  number_of_turn, init_pos = (0,0),
                 size_matrix = (360,360))
        self.car = Voiture.Voiture(x, y, n, p,size_matrix = (360,360))
        self.envi = self.my_road.map + self.car.map
        self.score = 0
        self.game_over = False
        self.data = [self.score, self.envi, self.game_over]

    def change_envi(self,y,x,new_value):
        self.envi[y][x] = new_value


    def change_game_over(self,y,x):
        if self.envi[y][x] == 5:
            self.game_over = True


    def rules(self):
        path_ = self.my_road.path
        for road_segment in path_:
            if road_segment[2] in [0,1]:
                self.change_game_over(road_segment[0] + (self.my_road._size_road//2) - 1,road_segment[1])
                self.change_game_over(road_segment[0] - (self.my_road._size_road // 2) + 1, road_segment[1])
            else :
                self.change_game_over(road_segment[0], road_segment[1] + (self.my_road._size_road//2) - 1)
                self.change_game_over(road_segment[0], road_segment[1] - (self.my_road._size_road // 2) + 1)
            if self.game_over == True:
                break










