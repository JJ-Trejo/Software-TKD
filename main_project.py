import pygame
import tkinter as tk
from tkinter import StringVar

# Inicializar Tkinter
ventana = tk.Tk()
ventana.title("Marcador TKD Moopalkwan Ecatepec V1.0")
ventana.geometry("1210x600+30+30")
ventana.minsize(1000, 600) #dimensiones minimas de la ventana

# Inicializar pygame para manejo de joystick
pygame.init()
pygame.joystick.init()

# Configuración inicial para controlar el tiempo
tiempo_total = 0  # Tiempo en segundos
running = False   # Estado del cronómetro

#Variables de color globales
color_equipo_1 = "blue"
color_equipo_2 = "red"

#################################### FUNCION BOTONES PRESIONADOS CONTROL
# Función para actualizar la entrada del control
def detectar_entrada():
    try:
        pygame.event.pump()  # Necesario para procesar eventos de pygame
        for i in range(joystick.get_numbuttons()):
            estado_actual = joystick.get_button(i)
            # Detectar el cambio de estado del botón
            if estado_actual and not botones_presionados[i]:
            # if joystick.get_button(i):
                print(f"Boton {i} presionado")
                if i == 0:   #A
                    incrementar_gamjeon_red()
                elif i == 1: #B
                    decrementar_gamjeon_red()
                elif i == 3: #X
                    incrementar_gamjeon_blue()
                elif i == 4: #Y
                    decrementar_gamjeon_blue()
                elif i == 6: #L1
                    decrementar_puntos_blue()
                elif i == 7: #R1
                    decrementar_puntos_red()
                elif i == 8: #L2
                    incrementar_puntos_blue()
                elif i == 9: #R2
                    incrementar_puntos_red()
                elif i == 10: #SELSECT
                    pass
                elif i == 11: #START
                    alternar_cronometro()
                elif i == 13: #JOY IZQUIERDO
                    decrementar_tiempo()
                elif i == 14: #JOY DERECHO
                    incrementar_tiempo()
                # Marcar el botón como presionado
                botones_presionados[i] = True
            elif not estado_actual:
                # Marcar el botón como no presionado
                botones_presionados[i] = False
        # Llamar continuamente a esta función para detección en tiempo real
        ventana.after(100, detectar_entrada)
        
    except (ValueError, KeyError, TypeError, IndexError, UnboundLocalError, NameError):
        # Mensaje si se pierde conexión
        print("Error detectando el control")

#################################### FUNCION SALIR DEL FOCO DEL ENTRY CON "ESC"
def quitar_foco(event):
    ventana.focus()  # Pone el foco en la ventana principal

#################################### FUNCIONES TIEMPO
# Función para mostrar el tiempo en formato mm:ss
def mostrar_tiempo():
    minutos = tiempo_total // 60
    segundos = tiempo_total % 60
    label_tiempo.config(text=f"{minutos:02}:{segundos:02}")

# Función para incrementar el tiempo en 1 minuto
def incrementar_tiempo(event=None):
    global tiempo_total
    tiempo_total += 60 #Suma 60 segundos 
    mostrar_tiempo()

# Función para decrementar el tiempo en 1 minuto
def decrementar_tiempo(event=None):
    global tiempo_total
    tiempo_total = max(0, tiempo_total - 60)  # Asegurarse de que no sea negativo y resta 60 segundos
    mostrar_tiempo()

# Función para alternar inicio/pausa del cronómetro
def alternar_cronometro(event=None):
    global running
    running = not running  # Alterna entre True y False
    if running:
        actualizar_tiempo()

# Función para actualizar el cronómetro
def actualizar_tiempo(*args):
    global tiempo_total, running
    if running and tiempo_total > 0: #Si running es verdadero y el tiempo total es mayor que cero
        tiempo_total -= 1 #Se le resta uno al tiempo total
        mostrar_tiempo() #LLama a la función que muestra el tiempo en pantalla
        ventana.after(1000, actualizar_tiempo) #cada 1 segundo
    elif tiempo_total <= 0:
        running = False
        label_tiempo.config(text="00:00")

#################################### FUNCIONES ROUNDS
def incrementar_rounds(*args):
    var_round_value.set(value=var_round_value.get()+1)

def reset_rounds(*args):
    var_round_value.set(value=1)

#################################### FUNCIONES PUNTOS BLUE
def incrementar_puntos_blue(*args):
    var_blue_point.set(value=var_blue_point.get()+1)

def decrementar_puntos_blue(*args):
    var_blue_point.set(value=var_blue_point.get()-1)

#################################### FUNCIONES PUNTOS RED
def incrementar_puntos_red(*args):
    var_red_point.set(value=var_red_point.get()+1)

def decrementar_puntos_red(*args):
    var_red_point.set(value=var_red_point.get()-1)

#################################### FUNCIONES GAMJEON BLUE
def incrementar_gamjeon_blue(*args):
    var_gamjeon_blue_point.set(value=var_gamjeon_blue_point.get()+1)

def decrementar_gamjeon_blue(*args):
    var_gamjeon_blue_point.set(value=var_gamjeon_blue_point.get()-1)

#################################### FUNCIONES GAMJEON RED
def incrementar_gamjeon_red(*args):
    var_gamjeon_red_point.set(value=var_gamjeon_red_point.get()+1)

def decrementar_gamjeon_red(*args):
    var_gamjeon_red_point.set(value=var_gamjeon_red_point.get()-1)

# >>>>> Contenedor categoria
cont_categoria = tk.Frame(ventana, background="Black")
cont_categoria.grid(row=0, column=0, sticky="nsew")

# >>>>> contenedor elementos
cont_elementos = tk.Frame(ventana)
cont_elementos.grid(row=1, column=0, sticky="nsew")

# >>>>> Pie de pagina
footer = tk.Label(text="Developed by Ing. J.J. Trejo - Nov 2024", background="light gray")
footer.grid(row=2, column=0, sticky="nsew")

# >>>>> contenedor para ingresar la bandera de mexico
cont_bandera = tk.Frame(cont_elementos)
cont_bandera.grid(row=0, column=0, sticky="nsew")

# >>>>> contenedor para ingresar la bandera de Moopalkwan
cont_tkd = tk.Frame(cont_elementos)
cont_tkd.grid(row=0, column=3, sticky="nsew")

# >>>>> Contenedor nombre equipo azul
cont_name_blue = tk.Frame(cont_elementos, background=color_equipo_1)
cont_name_blue.grid(row=0, column=1, sticky="nsew")

# >>>>> Contenedor nombre equipo rojo
cont_name_red = tk.Frame(cont_elementos, background=color_equipo_2)
cont_name_red.grid(row=0, column=2, sticky="nsew")

# >>>>> Configuración para que las filas y columnas se expandan
ventana.grid_columnconfigure(0, weight=1)       #ventana principal
ventana.grid_rowconfigure(1, weight=1)          #ventana principal
cont_elementos.grid_rowconfigure(0, weight=1)   #fila 0
cont_elementos.grid_rowconfigure(1, weight=10)  #fila 1
cont_elementos.grid_rowconfigure(2, weight=1)   #fila 2
cont_elementos.grid_columnconfigure(0, weight=1)  #columna 0
cont_elementos.grid_columnconfigure(1, weight=10) #columna 1
cont_elementos.grid_columnconfigure(2, weight=10) #columna 2
cont_elementos.grid_columnconfigure(3, weight=1)  #columna 3

############################################ Contenedor match | puntos ############################################
# >>>>> contenedor vacio 1
cont_vacio1 = tk.Frame(cont_elementos, background=color_equipo_1)
cont_vacio1.grid(row=1, column=0, sticky="nsew")
# >>>>> contenedor puntos | match | tiempo
cont_puntos_match = tk.Frame(cont_elementos)
cont_puntos_match.grid(row=1, column=1, columnspan=2, sticky="nsew")
# >>>>> Contenedor vacio 2
cont_vacio2 = tk.Frame(cont_elementos, background=color_equipo_2)
cont_vacio2.grid(row=1, column=3, sticky="nsew")

############################################ Contenedor round ############################################
# >>>>> contenedor gamjeon equipo azul
cont_gamjeon_blue = tk.Frame(cont_elementos, background=color_equipo_1)
cont_gamjeon_blue.grid(row=2, column=0, sticky="nsew")
# >>>>> contenedor round
cont_round = tk.Frame(cont_elementos, background="black")
cont_round.grid(row=2, column=1, columnspan=2, sticky="nsew")
# >>>>> Contenedor gamjeon equipo rojo
cont_gamjeon_red = tk.Frame(cont_elementos, background=color_equipo_2)
cont_gamjeon_red.grid(row=2, column=3, sticky="nsew")

############################################ NOMBRE 1 EQUIPO AZUL ############################################
# >>>>> Variable de control | equipo azul
var_name_blue = StringVar(value="NAME 1")
# >>>>> Entry nombre equipo azul
en_name_blue = tk.Entry(cont_name_blue, bd=0, textvariable=var_name_blue, background=color_equipo_1, foreground="white", font=("Arial", 15, "bold"), justify="center", width=20)
en_name_blue.pack( expand=True, fill="both")
# en_name_blue.grid(row=0, column=0, sticky="nsew", pady=30)

############################################ NOMBRE 2 EQUIPO ROJO ############################################
# >>>>> Variable de control | equipo rojo
var_name_red = StringVar(value="NAME 2")
# >>>>> Entry nombre equipo rojo
en_name_red = tk.Entry(cont_name_red, bd=0, textvariable=var_name_red, background=color_equipo_2, foreground="white", font=("Arial", 15, "bold"), justify="center", width=20)
en_name_red.pack( expand=True, fill="x")

############################################ FRAME PUNTOS EQUIPO AZUL ############################################
cont_points_blue = tk.Frame(cont_puntos_match, background="red")
cont_points_blue.pack(side="left", expand=True, fill="both")
# >>>>> Frame | Match
cont_match = tk.Frame(cont_puntos_match, background="black")
cont_match.pack(side="left", expand=True, fill="both")

############################################ FRAME PUNTOS EQUIPO ROJO ############################################
cont_points_red = tk.Frame(cont_puntos_match, background="red")
cont_points_red.pack(side="left", expand=True, fill="both")
# >>>>> Variable de control | categoria / peso
var_categoria_texto = StringVar(value="CATEGORIA / PESO")
# >>>>> Entry categoria / peso
en_categoria_texto = tk.Entry(cont_categoria, bd=0, textvariable=var_categoria_texto, background="black", foreground="white", font=("Arial", 20, "bold"), justify="center", width=50)
en_categoria_texto.pack(pady=30, expand=True, fill="both")

############################################ LABEL GAMJEON EQUIPO AZUL ############################################
lb_gamjeon_blue_texto = tk.Label(cont_gamjeon_blue, text="GAM-JEON", font=("Arial", 15, "bold"), justify="center", background=color_equipo_1, foreground="white")
lb_gamjeon_blue_texto.pack()
# >>>>> Variable de control | GAMJEON
var_gamjeon_blue_point = tk.IntVar(value=0)
# >>>>> label gamjeon puntos
lb_gamjeon_blue_point = tk.Label(cont_gamjeon_blue, textvariable=var_gamjeon_blue_point, font=("Arial", 30), justify="center", background=color_equipo_1, foreground="white")
lb_gamjeon_blue_point.pack(expand=True, fill="x") #Lo alinea al centro

############################################ LABEL GAMJEON EQUIPO ROJO ############################################
lb_gamjeon_red_texto = tk.Label(cont_gamjeon_red, text="GAM-JEON", font=("Arial", 15, "bold"), justify="center", background=color_equipo_2, foreground="white")
lb_gamjeon_red_texto.pack()
# >>>>> Variable de control | GAMJEON
var_gamjeon_red_point = tk.IntVar(value=0)
# >>>>> label gamjeon puntos
lb_gamjeon_red_point = tk.Label(cont_gamjeon_red, textvariable=var_gamjeon_red_point, font=("Arial", 30), justify="center", background=color_equipo_2, foreground="white")
lb_gamjeon_red_point.pack(expand=True, fill="both") #Lo alinea al centro

############################################ LABEL PUNTOS EQUIPO AZUL ############################################
# >>>>> Variable de control
var_blue_point = tk.IntVar(value=0)
# >>>>> Label puntos equipo azul
lb_blue_point = tk.Label(cont_points_blue, textvariable=var_blue_point, font=("Arial", 150), width=2) ####################
lb_blue_point.pack(expand=True, fill="both")

############################################ LABEL PUNTOS EQUIPO ROJO ############################################
# >>>>> Variable de control
var_red_point = tk.IntVar(value=0)
# >>>>> Label puntos equipo azul
lb_red_point = tk.Label(cont_points_red, textvariable=var_red_point, font=("Arial", 150), width=2)
lb_red_point.pack(expand=True, fill="both")

############################################ LABEL MATCH ############################################
# >>>>> Label match
lb_match = tk.Label(cont_match, text="MATCH", font=("Arial", 30, "bold"), background="black", foreground="White" )
lb_match.pack()
# >>>>> Variable de control
var_match_value = tk.IntVar(value=1)
# >>>>> Label numero de match
lb_match_value = tk.Entry(cont_match, bd=0, textvariable=var_match_value, font=("Arial", 30, "bold"), justify="center", background="black", foreground="White", width=5 )
lb_match_value.pack()
# Etiqueta para mostrar el tiempo
label_tiempo = tk.Label(cont_match, text="00:00", font=("Arial", 70, "bold"), background="black", foreground="White")
label_tiempo.pack(pady=20)

############################################ LABEL ROUND ############################################
#Label ROUND
lb_round = tk.Label(cont_round, text="ROUND", font=("Arial", 30, "bold"), justify="center", foreground="white", background="black")
lb_round.pack()
#Variable de control
var_round_value = tk.IntVar(value=1)
#Label ROUND

lb_round_value = tk.Entry(cont_round, width=3, bd=0, textvariable=var_round_value, font=("Arial", 30, "bold"), justify="center", foreground="white", background="black")
# lb_round_value = tk.Label(cont_round, textvariable=var_round_value, font=("Arial", 30, "bold"), justify="center", foreground="white", background="black")
lb_round_value.pack()

# >>>>> Imagenes
imagen1 = tk.PhotoImage(file="Mexico.png")
imagen2 = tk.PhotoImage(file="tkd.png")
etiqueta1 = tk.Label(cont_bandera, image=imagen1, background=color_equipo_1)
etiqueta2 = tk.Label(cont_tkd, image=imagen2, background=color_equipo_2)
etiqueta1.pack(expand=True, fill="both")
etiqueta2.pack(expand=True, fill="both")
# <<<<< Imagenes

ventana.bind("<Escape>", quitar_foco) # Capturar clics en la ventana para quitar el foco del Entry

# Función para intentar la conexión del control
if pygame.joystick.get_count() > 0:
    global joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()  # Inicializar joystick para detección de eventos
    print(f"Joystick conectado: {joystick.get_name()}")
    # Variable para llevar el estado de los botones
    botones_presionados = [False] * pygame.joystick.Joystick(0).get_numbuttons()
    detectar_entrada()  # Iniciar detección de botones
else:
    print("No se detectó ningún joystick conectado")

# Ejecutar la interfaz gráfica
ventana.mainloop()
pygame.quit()