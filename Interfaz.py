import tkinter as tk
from PIL import Image, ImageTk
import Biseccion, TaylorLau,Newton_RaphsonV2

def generar_newton_raphson():
    f_expr1 = newton_raphson_entry.get()
    x0 = float(x0_entry.get())
    error = float(error_entry_newton.get())
    iteraciones = int(iteraciones_entry.get())
    
    Newton_RaphsonV2.newthon_raphson(f_expr1, x0, error, iteraciones)
    #newthon_raphson("x**2-8", 2.0)

    
def generar_biseccion():
    f_expr2 = biseccion_entry.get()
    a  = float(intervalo_entry_a.get())
    b = float(intervalo_entry_b.get())
    error2 = float(error_entry.get())

    Biseccion.biseccion(f_expr2,a,b,error2)
    #Biseccion.biseccion("x**3 + 4*x**2 - 10",1,2,1e-4)

    
def generar_polinomio_taylor():
    f_expr3 = taylor_f_entry.get()
    grado = int(taylor_grado_entry.get())
    c = float(taylor_x0_entry.get())

    TaylorLau.taylor_polynomial(f_expr3,c,grado)
    #taylor_polynomial("exp(x)", 3, 3)
   

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("850x700")
ventana.title("Calculadora de métodos numéricos")
ventana.configure(bg="snow")


"----------------------------------------------------------------------------------------"
# Primera sección - Newton-Raphson
newton_raphson_frame = tk.Frame(ventana,bg="lightblue",relief="solid",borderwidth=2)
newton_raphson_frame.pack(fill=tk.X,pady=20)

newton_raphson_label = tk.Label(newton_raphson_frame, text="Newton-Raphson", font=("Arial", 16, "bold"),bg="lightblue")
newton_raphson_label.pack(pady=10)
#####
newton_raphson_entry_frame = tk.Frame(newton_raphson_frame,bg="lightblue")
newton_raphson_entry_frame.pack(pady=30)
###
newton_raphson_label2 = tk.Label(newton_raphson_entry_frame, text="f(x)",bg="lightblue")
newton_raphson_label2.pack(side=tk.LEFT)

newton_raphson_entry = tk.Entry(newton_raphson_entry_frame, width=40)
newton_raphson_entry.pack(side=tk.LEFT, padx=5)

x0_label = tk.Label(newton_raphson_entry_frame, text="x0",bg="lightblue")
x0_label.pack(side=tk.LEFT)

x0_entry = tk.Entry(newton_raphson_entry_frame, width=20)
x0_entry.pack(side=tk.LEFT, padx=5)

error_label = tk.Label(newton_raphson_entry_frame, text="error",bg="lightblue")
error_label.pack(side=tk.LEFT)

error_entry_newton = tk.Entry(newton_raphson_entry_frame, width=20)
error_entry_newton.pack(side=tk.LEFT, padx=5)

iteraciones_label = tk.Label(newton_raphson_entry_frame, text="iteraciones",bg="lightblue")
iteraciones_label.pack(side=tk.LEFT)

iteraciones_entry = tk.Entry(newton_raphson_entry_frame, width=20)
iteraciones_entry.pack(side=tk.LEFT, padx=5)

generar_button1=tk.Button(newton_raphson_frame, height = 1,
                 width = 15,
                 text ="Generar",
                 command = generar_newton_raphson,font=("times new roman", 12), bg="green",fg="cornsilk2",bd=0,cursor="hand2"
                 )
generar_button1.pack(pady=10)
"----------------------------------------------------------------------------------------"
# Segunda sección - Bisección
biseccion_frame = tk.Frame(ventana,bg="lightyellow",relief="solid",borderwidth=2)
biseccion_frame.pack(fill=tk.X, pady=20)

biseccion_label = tk.Label(biseccion_frame, text="Bisección", font=("Arial", 16, "bold"),bg="lightyellow")
biseccion_label.pack(pady=10)
##
biseccion_entry_frame = tk.Frame(biseccion_frame,bg="lightyellow")
biseccion_entry_frame.pack(pady=30)
####
biseccion_label2 = tk.Label(biseccion_entry_frame, text="f(x)",bg="lightyellow")
biseccion_label2.pack(side=tk.LEFT)

biseccion_entry = tk.Entry(biseccion_entry_frame, width=40)
biseccion_entry.pack(side=tk.LEFT, padx=5)

intervalo_label_a = tk.Label(biseccion_entry_frame, text="a",bg="lightyellow")
intervalo_label_a.pack(side=tk.LEFT)

intervalo_entry_a = tk.Entry(biseccion_entry_frame, width=20)
intervalo_entry_a.pack(side=tk.LEFT, padx=5)

intervalo_label_b = tk.Label(biseccion_entry_frame, text="b",bg="lightyellow")
intervalo_label_b.pack(side=tk.LEFT)

intervalo_entry_b = tk.Entry(biseccion_entry_frame, width=20)
intervalo_entry_b.pack(side=tk.LEFT, padx=5)

error_label = tk.Label(biseccion_entry_frame, text="error",bg="lightyellow")
error_label.pack(side=tk.LEFT)

error_entry = tk.Entry(biseccion_entry_frame, width=20)
error_entry.pack(side=tk.LEFT, padx=5)

generar_button2=tk.Button(biseccion_frame, height = 1,
                 width = 15,
                 text ="Generar",
                 command = generar_biseccion,font=("times new roman", 12), bg="green",fg="cornsilk2",bd=0,cursor="hand2"
                 )
generar_button2.pack(pady=10)

"----------------------------------------------------------------------------------------"
# Tercera sección - Polinomio de Taylor
taylor_frame = tk.Frame(ventana,bg="lavender",relief="solid",borderwidth=2)
taylor_frame.pack(fill=tk.X, pady=20)

taylor_label = tk.Label(taylor_frame, text="Polinomio de Taylor", font=("Arial", 16, "bold"),bg="lavender")
taylor_label.pack(pady=10)
##

taylor_entry_frame = tk.Frame(taylor_frame,bg="lavender")
taylor_entry_frame.pack(pady=30)
####

taylor_f_entry_label = tk.Label(taylor_entry_frame, text="f(x)",bg="lavender")
taylor_f_entry_label.pack(side=tk.LEFT)

taylor_f_entry = tk.Entry(taylor_entry_frame,width=40)
taylor_f_entry.pack(side=tk.LEFT, padx=5)

taylor_grado_entry_label = tk.Label(taylor_entry_frame, text="Grado",bg="lavender")
taylor_grado_entry_label.pack(side=tk.LEFT)

taylor_grado_entry = tk.Entry(taylor_entry_frame)
taylor_grado_entry.pack(side=tk.LEFT, padx=5)

taylor_x0_entry_label = tk.Label(taylor_entry_frame, text="x0",bg="lavender")
taylor_x0_entry_label.pack(side=tk.LEFT)

taylor_x0_entry = tk.Entry(taylor_entry_frame)
taylor_x0_entry.pack(side=tk.LEFT, padx=5)

generar_button3=tk.Button(taylor_frame, height = 1,
                 width = 15,
                 text ="Generar",
                 command =generar_polinomio_taylor,font=("times new roman", 12), bg="green",fg="cornsilk2",bd=0,cursor="hand2"
                 )
generar_button3.pack(pady=10)

ventana.mainloop()