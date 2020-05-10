#voy a hacer un plot temporal:
#quiero graficar un punto que se une con otro punto calculado al azar en un tablero de 10x10
import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np
import random as rnd
from time import sleep

semilla = 72
escala=10
iRand72 = rnd.Random(72)
iRand10 = rnd.Random(10)
plt.ion()
puntos = [[],[]]
for x in range(5):
    for y in range(5):
        puntos[0].append(round(iRand72.random()*escala))
        puntos[1].append(round(iRand10.random()*escala))
        plt.plot(puntos[0], puntos[1], 'b*-', label='trayecto')
        plt.xlim(-0.5,10.5)
        plt.ylim(-0.5,10.5)
        sleep(1)
        plt.pause(0.01)

#dejar el plot en pantalla hasta que se aprete un boton


#print("{}".format(puntos))

#iteracion de la cantidad de puntos a graficar
    #generacion de un random de 2 dimensiones con distribución uniforme