import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime

#datos de la maquina 
#datos como la temperatura tendran que programarse directamente en la maquina 


#para representar el numero de usuarios mejor representarlo mediante un grafico de barras
#relacion de usuarios con respecto al tiempo 

def num_users():
    f = open('users.txt', 'r')
    a = 0
    for i in range(len(f.read())):
        a = a+1
        
    x = np.array([0,a])
    plt.bar(x)
    plt.show()
    
num_users()