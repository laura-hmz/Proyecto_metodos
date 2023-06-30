import sympy as sp
import tkinter as tk
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np


def generar_tabla_newton(table):
    # Crear una nueva ventana para mostrar la tabla
    new_window2 = tk.Tk()
    new_window2.title("Tabla de Newton-Raphson generada")

    # Crear un widget Text en la nueva ventana
    table_text = tk.Text(new_window2, width=80)
    table_text.insert(tk.END, table.get_string())
    table_text.configure(state="disabled")
    table_text.pack()



def newthon_raphson(expresion, punto_inicial, tolerancia=0.00001, numero_iteraciones=20):
    """
    datos obligatorios funcion y punto_inicial, en caso de no introducir el numero de iteraciones se detendra en la
    iteracion 20 y toleracia de 0.00001
    :param expresion: introducir la expresion de funcion en formato compatible con la libreria sympy
    :param punto_inicial: introducir el valor del punto inicial
    :param tolerancia: introducir el valor en formato decimal
    :param numero_iteraciones: introducir el valor en formato decimal
    """

    x = sp.symbols('x')  # Creamos la variable x
    derivada_expresion = sp.diff(expresion)
    funcion = sp.lambdify(x, expresion)
    derivada_funcion = sp.lambdify(x, derivada_expresion)
    roots = [punto_inicial]
    punto_actual = punto_inicial
    # tablita
    lista_titulo = ('n', 'Xn', 'Error')
    tabla = PrettyTable(lista_titulo)
    for i in range(numero_iteraciones):
        punto_futuro = punto_actual - funcion(punto_actual) / derivada_funcion(punto_actual)
        roots.append(punto_futuro)
        tabla.add_row([i, punto_actual, abs(punto_actual - punto_futuro)])
        if abs(punto_actual - punto_futuro) < tolerancia:
            # print(f'x {i + 1} = {punto_futuro} es una buena aproximacion de la raiz')
            
            break
        punto_actual = punto_futuro
        # print(f'x {i + 1} = {punto_futuro}')
    print(tabla)
    generar_tabla_newton(tabla)

    # Codigo para graficar la funcion
    x_vals = np.linspace(-100, 100, 100)
    f_vals = funcion(x_vals)

    plt.plot(x_vals, f_vals, label='f(x)')
    plt.scatter(roots, [funcion(val) for val in roots], color='red', label='Raíz encontrada') #Este es para grafica todas las raices
    plt.scatter(roots[-1], funcion(roots[-1]), color='black', label='Ultima raiz encontrada') #Este es para graficar unicamente la ulima raiz

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.title('Gráfica de la función y raíz encontrada')

    plt.show()

#newthon_raphson("x**2-8", 2.0)

