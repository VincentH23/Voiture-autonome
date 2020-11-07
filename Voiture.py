import numpy as np
import matplotlib.pyplot as plt
class Voiture:
    def __init__(self,x,y,n,p,tailleMaps):
        self.pos=np.array([[x],[y]]).astype('float')
        self.direction=np.array([[-1],[0]]).astype('float')
        self.size=n,p
        self.map=np.zeros((tailleMaps,tailleMaps))

        self.map[y-p//2:y+p//2+1,x-n//2:x+n//2+1]=1

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
        indice=self.index.astype('int32')

        self.map[indice[1],indice[0]]=1





map=np.zeros((15,15))
angle=np.linspace(0,np.pi/2,11)
voiture=Voiture(80,150,35,25,360)
print(voiture.index)
plt.figure()
plt.imshow(voiture.map)
k=0
while 1:
    print(voiture.direction)
    print(voiture.pos,k)
    if k%3==0:
        voiture.deplacement(5,0.1)
        plt.show()
        plt.figure()
        plt.imshow(voiture.map)
    else:
        voiture.deplacement(5, 0)
        plt.show()
        plt.figure()
        plt.imshow(voiture.map)

    plt.show()
    k+=1