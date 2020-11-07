import numpy as np
class Voiture:
    def __init__(self,x,y,n,p):
        self.pos=np.array([[x],[y]]).astype('float')
        self.direction=np.array([[-1],[0]]).astype('float')
        self.size=n,p


    def deplacement(self,vitesse,angle):
        #rotation
        rotation=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
        self.direction=rotation@self.direction
        self.pos=self.pos+vitesse*self.direction






map=np.zeros((10,10))
angle=np.linspace(0,np.pi/2,11)
voiture=Voiture(5,5,2,3)
map[int(voiture.pos[1]),int(voiture.pos[0])]=1
for k in range (len(angle)):
    voiture.deplacement(1,angle[k])
    map[int(voiture.pos[1]), int(voiture.pos[0])] = k+2
    print(map)
