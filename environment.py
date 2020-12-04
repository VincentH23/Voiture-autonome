import road

import Voiture


class Environment:

    def __init__(self,size_road,  number_of_turn, x, y, n, p, init_pos = (0,0),
                 size_matrix = (360,360)):
        self.my_road = road.Road(size_road,  number_of_turn, init_pos = (0,0),
                 size_matrix = (360,360))
        self.car = Voiture.Voiture(x, y, n, p,size_matrix = (360,360))
        self.window = self.my_road.map + self.car.map
        self.score = 0
        self.game_over = False
        self.data = [self.score, self.window, self.game_over]
        self.DeltaAngle=0.05
        self.vitesse=5
        self.acc=1
        self.decelaration=-1
        self.vitesseMin=5


    def get_data(self):
        return self.data

    def nextStep(self):

        if self.data['gameover'] == False:

            decision =self.car.decision(self.get_data())
            self.vitesse+=decision[0]*self.acc+(1-decision[0])*self.decelaration
            self.vitesse=max(self.vitesse,self.vitesseMin)

            angle=(decision[1]-decision[2])*self.DeltaAngle
            self.car.deplacement(self.vitesse,angle)
            self.score += self.vitesse
            self.window=self.my_road.map+self.car.map
            A=self.window[self.window>5]
            if A.shape[0]==0:
                self.game_over=True











