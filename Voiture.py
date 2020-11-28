import numpy as np

import matplotlib.pyplot as plt

class Voiture:

    def __init__(self,x,y,n,p,size_matrix = (360,360)):
        self.pos=np.array([[x],[y]]).astype('float64')
        self.direction=np.array([[-1],[0]]).astype('float64')
        self.size=n,p
        self.map=np.zeros(size_matrix)

        self.map[y-p//2:y+p//2+1,x-n//2:x+n//2+1]=1
        self.step = 0

        self.index=np.zeros((2,n*p))
        counter=0
        for i in range(y-p//2,y+p//2+1):
            for j in range(x - n // 2, x+ n // 2 + 1):
                self.index[0,counter]=j
                self.index[1, counter] = i
                counter+=1


    def deplacement(self,vitesse,angle):
        #rotation
        rotation=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
        self.direction=rotation@self.direction
        self.pos=self.pos+vitesse*self.direction
        self.index= rotation@(self.index-self.pos)+self.pos+vitesse * self.direction

        self.map=0*self.map
        indice=self.index.astype('int64')

        self.map[indice[1],indice[0]]=1
        self.step += 1

        print(np.sum(self.map== 1))





