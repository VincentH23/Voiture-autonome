import road

import Voiture


class environment:

    def __init__(self,size_road,  number_of_turn, x, y, n, p, init_pos = (0,0),
                 size_matrix = (360,360)):
        self.my_road = road.Road(size_road,  number_of_turn, init_pos = (0,0),
                 size_matrix = (360,360))
        self.car = Voiture.Voiture(x, y, n, p,size_matrix = (360,360))
        self.envi = self.my_road.map + self.car.map

