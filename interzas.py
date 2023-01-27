import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from random import randint
from funcionBaseDatos import baseDatos , listapalabras,obtenerUsuario ,editarPuntaje,agregarUsuario,tablaPosiciones

baseDatos()#executo dicha funcion para crear la base de datos 
listaPalabras= listapalabras()

# --------- creacion de la ventana ------------

root = tk.Tk() #creo la ventana
root.title("Juego del Ahorcado")#cambio el titulo de la ventana
#root.iconbitmap("./ahorcado.png")#cambio el icono de la ventana
root.geometry("720x400") # establesco las medida de la ventana
root.config(bg="lightblue") # establezco el color de fondo de la ventana

#----------- creacion de las funciones para la presentacion --------------------

def bienvenida(event=None):
  
  global nombre , saludo
  nombre = etiqueta_1.get()
  nombre= nombre.capitalize()
  frame.place_forget()
  frame_2.place_forget()
  etiqueta_1.place_forget()
  saludo = ttk.Label(root,text= f"""
           ¡¡¡Bienvenido {nombre} !!! al juego del "AHORCADO"
            ¡La cosa es asi yo pienso una palabra y vos 
            tratas de adivinarla "Para eso tenes 6 vidas" !  
                      """, font="helvetica 18 ", background="lightblue" )
  saludo.place(x= 30 ,y = 30 )
  boton_comenzar.place(x= 280, y=180 , width=140 , height= 60)
    
def comenzar (event=None):
  #global nombre
  boton_comenzar.place_forget ()
  saludo.place_forget () 
  etiqueta_3.place_forget()
  botonSi.place_forget()
  botonNo.place_forget()
  tabla_1.place_forget()
  
  presentacioPalabraSecreta.place(x=20,y=20)
  palabraSecreta.place(x= 20 , y=60)
  elijaLetra.place(x=20 , y = 120)
  ingresoLetra.place(x=20,y=180)
  botonProbar.place(x=20, y=240)
  etiquetaImagen.place(x=400,y=80)
  presentacioIntentos.place(x=20,y=275)
  etiquetaIntentos.place(x=20,y=300)
  etiquetaVidas.place(x=20,y=360)
  etiquetaResultado.place(x=350,y=300)
  etiquetaResultado.config(text="")
  
 #creo las variables del funcionamiento del programa
  
  global palabrasSecretas, letrasIntentadas,vidasRestantes,puntaje
  indice = randint(0,len(listaPalabras)-1)
  palabrasSecretas = listaPalabras[indice]
  letrasIntentadas=[] #creo una lista vacia para ingresar aqui las letras intentadas
  vidasRestantes = 6
  puntaje = 0
  
  #invoco funciones de inicio:
  mostrarPalabra()
  
#---------------- creacion funciones del funcionamiento programa ---------------
def eleccionLetra():
  global  puntaje,vidasRestantes
  letraIngresada = ingresoLetra.get() #le doy a la varieble el valor que ingreso en el input
  # Chequear si esta letra esta en letras intentadas
  if letraIngresada in letrasIntentadas: # ['a']
    etiquetaResultado.config(text=f'''La letra >>> {letraIngresada} <<< ya la
    elegiste anteriormente''', foreground='blue')
  else:
    letrasIntentadas.append(letraIngresada)#ingreso la letra a la lista 
    if letraIngresada not in palabrasSecretas:
      etiquetaResultado.config(text="""Letra no esta en la palabra,
      restaste una vida""", foreground='red')
      vidasRestantes = vidasRestantes - 1
    else:
      etiquetaResultado.config(text="Letra en la palabra !!!!", foreground='green')
  if vidasRestantes == 0:
    #etiquetaResultado.config(text=f"""{nombre} Perdiste, la palabra 
    #era '{palabrasSecretas}'""")
     puntaje = -10
     finalizar()
  
  mostrarPalabra()
  ingresoLetra.delete(0)
  ingresoLetra.focus()




def mostrarPalabra():
  global puntaje
  encontradas = 0
  progresoPalabra=""
  
  for letra in palabrasSecretas:
    if letra in letrasIntentadas: 
      progresoPalabra = f'{progresoPalabra} {letra}'
      encontradas = encontradas + 1
    else:
      progresoPalabra = f'{progresoPalabra} *'
  palabraSecreta.config(text=f"{progresoPalabra}", font='bold 14')
  
  if encontradas == len(palabrasSecretas):
    puntaje = vidasRestantes * len(palabrasSecretas)
    #etiquetaResultado.config(text=f'¡¡GANASTE, puntos: {puntaje}!!',foreground='green')
    finalizar()
    
  # Mostrar letras ya intentadas (Erroneas y las correctas)
  intentadas=''
  for l in letrasIntentadas:
    intentadas = f'{intentadas}  {l}'
  etiquetaIntentos.config(text=f'{intentadas.upper()}', font='bold 16')
  
  # Mostrar Vidas restantes
  etiquetaVidas.config(text=f"{nombre} te restan {vidasRestantes} intentos", font='bold 12')
  
def posiciones():
  global tabla_2,tabla_3,usuarios
  usuarios = tablaPosiciones()
  fila = 70
  tabla_1.place(x=280, y=fila)
  fila=fila+30 # esto lo hago para que cuando itere me coloque uno debajo del otro a la misma linea
  for usu in usuarios:
    tabla_2=ttk.Label(
       text=f"{usu['nombre']}",
      # width=60,
      justify='right',background="lightblue"
    ).place(x=300,y=fila)
    tabla_3=tk.Label(
     text=f"{usu['puntaje']}",
     width=3,background="lightblue"
    ).place(x=370,y=fila)
    fila = fila + 20 
 
  
def finalizar():
  global nombre, puntaje,botonNo,botonSi,etiqueta_3
  presentacioPalabraSecreta.place_forget()
  palabraSecreta.place_forget()
  elijaLetra.place_forget()
  ingresoLetra.place_forget()
  botonProbar.place_forget()
  etiquetaImagen.place_forget()
  presentacioIntentos.place_forget()
  etiquetaIntentos.place_forget()
  etiquetaVidas.place_forget()
  
  
  # Gestion del usuario
  #nombre = nombre.lower()
  usuario = obtenerUsuario(nombre)

  if usuario:
    # Existe, modificar puntaje

    usuario["puntaje"] = usuario["puntaje"] + puntaje
    if usuario["puntaje"] <= 0:
      usuario["puntaje"] = 0
    editarPuntaje(usuario["id"],usuario["puntaje"])
  else:
    # No existe, agregarlo con el puntaje
    if puntaje <= 0:
      puntaje = 0
    agregarUsuario(nombre, puntaje)
  if vidasRestantes == 0:
    etiquetaResultado.config(text=f"{nombre} Perdiste, la palabra era '{palabrasSecretas}'")
    etiquetaResultado.place(x=100,y=30)
  else:
     etiquetaResultado.config(text=f'¡¡¡ {nombre} GANASTE,tu puntuaje fue: {puntaje}!!!',foreground='green')
     etiquetaResultado.place(x=100,y=30)
  posiciones()
  etiqueta_3.place(x=210,y=250)
  botonSi.place(x=260,y=310)
  botonNo.place(x=360,y=310)

def cerrarPrograma():
  root.destroy()

def reiniciar():
  tabla_2.remove() #--- aca esta el error , pienso que no lo puedo anular lista " no se  ver"
  tabla_3.remove() #--- si no lo anulo queda mal
  comenzar()
  


  

#------------- creacion de las etiquetas presentacion (widgets en ingles) ---------- 
frame = ttk.Label(root,text="Ingrese su nombre aqui : ", width="25") # de esta forma ingreso un texto a la ventana
#frame.config(padx = 5 ,pady =5 ) # de esta manera configuro el padding
frame.place(x=260 ,y=10) # place va si o si para que el elemento se muestre en la ventana y dentro de el configuro la po
etiqueta_1 = ttk.Entry(root, font="helvetica 20")# de esta forma creo un input para ingresar datos del usuario
etiqueta_1.place(x=185 , y= 35)

#nombre =  "" #etiqueta_1.get() con get tomo el valor de lo que pose adentro la etiqueta
#nombre= nombre.lower()
frame_2 = ttk.Button(root,text="Entrar!!!",command= bienvenida )#creo un boton de entrada para que se realce la funcion 
frame_2.place(x=295, y=95)
boton_comenzar =ttk.Button(root,text="Comencemos !!!",command=comenzar)
#saludo = ttk.Label(root,text= f"""
           #¡¡¡Bienvenido {nombre} !!! al juego del "AHORCADO"
           #¡La cosa es asi yo pienso una palabra y vos 
            #tratas de adivinarla "Para eso tenes 6 vidas" !  
                      #""", font="helvetica 18 ", background="lightblue" )


#---------------- creacion de etiquetas juego ---------------

presentacioPalabraSecreta= ttk.Label(root,text="Palabra Secreta :",font="helvatica 20 ",background="lightblue")
palabraSecreta=ttk.Label(root,text="",font="helvetica",background="white",width="25")
elijaLetra=ttk.Label(root,text="Elija una letra :",font="helvetica 20",background="lightblue")
ingresoLetra=ttk.Entry(root,font="helvetica 20")
botonProbar=ttk.Button(root,text="Probar",cursor="hand2",command=eleccionLetra)
presentacioIntentos=ttk.Label(root,text="Letras ya intentadas :")
etiquetaIntentos=ttk.Label(root,text="",background="lightblue")
etiquetaVidas=ttk.Label(root,text="",background="lightblue")
imagen= tk.PhotoImage(file="ahorcado.png")
etiquetaImagen=ttk.Label(root,image=imagen)
etiquetaResultado = ttk.Label(root,text="",background="lightblue",font="helvetica 20")
etiqueta_3=ttk.Label(root,text="Desea seguir jugando ?",background="lightblue",font="helvetica 20")
botonSi = ttk.Button(root,text="SI",command=reiniciar)
botonNo=ttk.Button(root,text="NO",command= cerrarPrograma)
tabla_1=ttk.Label(text='Posiciones', font='Bold 20',background="lightblue")
tabla_2=[]
tabla_3=[]

#tababla_posiciones=ttk.Treeview(root,columns=("Nombre","Puntos"))


    





root.mainloop()