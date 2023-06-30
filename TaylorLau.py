import sympy as sp
from sympy.plotting import plot
import tkinter as tk


def mostrar_expresion(ex):
    # Crear una nueva ventana para mostrar la tabla
    new_window = tk.Tk()
    new_window.title("Polinomio de Taylor Generado")
    table_text = tk.Text(new_window, width=120,height=5)
    table_text.insert(tk.END, ex)
    table_text.configure(state="disabled")
    table_text.pack(fill=tk.X)



def taylor_polynomial(f_expr, a, n):
    x = sp.symbols('x')
    f = sp.sympify(f_expr)
    taylor_approximation = 0
    
    for k in range(n+1):
        dfk = f.diff(x, k)
        taylor_approximation += (dfk.subs(x, a) / sp.factorial(k)) * (x - a)**k
    
    mostrar_expresion(taylor_approximation)
    print(taylor_approximation)
    
    p1 = plot(f, show=False, line_color='blue', label='Función original')
    p2 = plot(taylor_approximation, show=False, line_color='red', label='Polinomio de Taylor')

    # Agregar una leyenda y mostrar la gráfica
    p1.extend(p2)
    p1.legend = True
    p1.title("Gráfica de aproximación polinomio de Taylor")
    p1.show()


#taylor_polynomial("exp(x)", 3, 3)
