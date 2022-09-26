import random
import matplotlib.pyplot as plt
import math
import numpy as np

Q = 0.05
R = 1.2
Hsubz = 0.35
Nr = 1.5

# random
def funcionPT():
    Pt = 1 - (Q+ 0.1)*random.uniform(0,1)
    return(Pt)

#saca hprima = Q/A
def funcionHP():
    A = (2*3.1415926*R)*(R+Hsubz)
    print("Value A {}".format(A))   # con el format pasas parametro y con las {} lo llamas
    Hpri = Q/A
    return(Hpri)

# calcula D, y cambia Q dependiendo a sus condiciones
def funcionDs(t):
    print(t)
    t = 0.5 if t == 0 else t
    Calcul = Nr - t
    D = Calcul
    if D < 0:
        Q = 0
    else:
        Q = 0.05
    return Q

#calcula desde un tiempo, puede ser 0 en adelante. mientras sea entero y grafrica
#iteracion para t y para h(t)-> ht
def funcionHt():
    fname = input("ingrese el tiempo: ") 
    fv = float(fname)
    t = []
    ht = []
    for x in range(0,int(fv)):
        funcionDs(x)
        print(funcionHP())
        rara = x * funcionPT() + funcionHP()
        t.insert(int(x), x)
        ht.insert(int(x), rara)

    print(t)
    print(ht)
    plt.plot(t,ht)
    plt.show()

funcionHt()
