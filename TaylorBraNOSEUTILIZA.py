from math import *
import sympy as sp
from sympy.plotting import plot

def PolTaylor(f_expr,a,n,grapinter):
    x=sp.symbols('x') #define la variable x para usarse como simbolo
    f=sp.sympify(f_expr) # Convertir la expresión de la función a un objeto simbólico
    F=f
    T=f.subs(x,a)
    for k in range(1,n+1):
        dfk=sp.diff(f,x)
        T = T + dfk.subs(x,a)*((x-a)**k)/factorial(k)
        f=dfk

    T= sp.expand(T) # Expandir el polinomio de Taylor
    print(T)

    g=plot(F,T,(x,a-3,a+3), title='Polinomio de Taylor', show=False)
    g[0].line_color='b'
    g[1].line_color='r'
    g.show()



f_expr = input('Digite la función f(x): ')
a= float(input('Digite alrededor de cual punto desea el polinomio de taylor:'))
n = int(input('Digite el orden del polinomio:'))
intervalor = int(input('Digite el intervalo para el grafico:'))

PolTaylor(f_expr, a, n, intervalor)