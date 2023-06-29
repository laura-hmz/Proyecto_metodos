import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import tkinter as tk

def generar_tabla(table):
    # Crear una nueva ventana para mostrar la tabla
    new_window = tk.Tk()
    new_window.title("Tabla Bisección generada")

    # Crear un widget Text en la nueva ventana
    table_text = tk.Text(new_window, width=80)
    table_text.insert(tk.END, table.get_string())
    table_text.configure(state="disabled")
    table_text.pack()


def biseccion(f_expr, a, b, tol):
    x = sp.symbols('x')
    f = sp.sympify(f_expr)
    
    #tablita
    listaTitulo = ('n','an','bn','Pn','error')
    tabla = PrettyTable(listaTitulo)
    k = 0
    
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    
    if fa * fb > 0:
        print('La función no cambia de signo en el intervalo.')
        return
    
    while abs(b - a) > tol:
        c = (a + b) / 2
        tabla.add_row([k, a, b, c, abs(b - a)])
        
        fc = f.subs(x, c)
        
        if fc == 0:
            print(f'La raíz exacta es {c}.')
            return
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        k += 1

    tabla.add_row([k, a, b, c, abs(b - a)])
    print(f'x{k} = {c} es una buena aproximación.')
    print(tabla)
    generar_tabla(tabla)
    
    # Graficar la función, el intervalo y la raíz
    x_vals = np.linspace(a - 1, b + 1, 1000)
    y_vals = [f.subs(x, x_val) for x_val in x_vals]
    root = (a + b) / 2
    
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axvline(a, color='red', linestyle='--', label='Intervalo [a]')
    plt.axvline(b, color='red', linestyle='--', label='Intervalo [b]')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter(root, f.subs(x, root), color='green', label='Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la raíz método de bisección')
    plt.legend()
    plt.grid(True)
    plt.show()


# Ejemplo de uso
f_expr = "x**3 + 4*x**2 - 10"
a = 1
b = 2
tol = 1e-4

#biseccion(f_expr, a, b, tol)