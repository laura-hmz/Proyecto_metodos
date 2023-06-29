import sympy as sp
from math import *
import numpy as np
import matplotlib.pyplot as plt

#Logica de la funcion

def NewtonRaphson(x0,tao,n,func):
    x = sp.symbols('x') #Creamos la variable x
    f = func
    df=sp.diff(f) #calcula la derivada de la funcion f
    f=sp.lambdify(x,f)
    df=sp.lambdify(x,df)
    roots = []
    for i in range(n):
        x1=x0-f(x0)/df(x0)
        roots.append(x1)
        if(abs(x1-x0)<tao):
            print(f'x {i+1} = {x1} es una buena aproximacion de la raiz')
            return roots
        x0=x1
        print(f'x {i+1} = {x1}')
    return roots


x_0 = float(input("Digite el valor inicial:"))
tolerancia = float(input("Digite tao:"))
iteraciones = int(input("Digite las iteraciones:"))
f_expr = input("Escriba la funcion:")

roots = NewtonRaphson(x_0,tolerancia,iteraciones,f_expr)
#(NewtonRaphson(2,0.0000001,20))

x = sp.Symbol('x')
f = sp.lambdify(x, f_expr)

# Codigo para graficar la funcion
x_vals = np.linspace(-100, 100, 100)
f_vals = f(x_vals)

plt.plot(x_vals, f_vals, label='f(x)')
plt.scatter(roots, [f(val) for val in roots], color='red', label='Raíz encontrada') #Este es para grafica todas las raices
plt.scatter(roots[-1], f(roots[-1]), color='black', label='Ultima raiz encontrada') #Este es para graficar unicamente la ulima raiz

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.title('Gráfica de la función y raíz encontrada')

plt.show()

