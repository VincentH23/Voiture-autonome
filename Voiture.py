import numpy as np

import matplotlib.pyplot as plt
import tensorflow as tf
class Brain:
    def __init__(self,input_shape):
        self.input_shape=input_shape
        self.layer1=tf.keras.layers.Conv2D(16,kernel_size=(5,5),activation='relu',input_shape=input_shape)
        self.layer2=tf.keras.layers.Conv2D(32,kernel_size=(3,3),strides=(2,2),activation='tanh')
        self.layer3=tf.keras.layers.Dense(32,activation='tanh')
        self.layer4=tf.keras.layers.Dense(3,activation='sigmoid')

    def forward(self,x,batch_size=1):
        new_shape=(batch_size,)+self.input_shape     #add the batch size and the channel
        out=x.reshape(new_shape)
        out=self.layer1(out)
        out=self.layer2(out)
        out=tf.keras.layers.Flatten()(out)
        out=self.layer3(out)
        out=self.layer4(out)
        return out

    def decision(self,x):
        pred=self.forward(x)
        return pred[0]>np.array([0.5,0.5,0.5])

class Voiture:

    def __init__(self,x,y,n,p,size_matrix = (360,360)):
        self.pos=np.array([[x],[y]]).astype('float64')
        self.direction=np.array([[-1],[0]]).astype('float64')
        self.size=n,p
        self.brain=Brain(size_matrix+(1,))                      # add the channel
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





