# mostrar palabra secreta con un icono de estrella
# ir mostrando formacion de la palabra
# mostrar letras acertadas y erradas
# mostrar vida restantes 
import os  # importo esta libreria que me sirve para limpiar pantalla
from random import randint # para importar de la libreria randon la funcion randit (que se usa para aleatoridad)
from funcionBaseDatos import baseDatos , listapalabras,obtenerUsuario ,editarPuntaje,agregarUsuario,tablaPosiciones# importo la funcion creada 

baseDatos()#executo dicha funcion para crear la base de datos 

listaPalabras= listapalabras()
indice = randint(0 , len(listaPalabras)-1) # aqui uso el len(listapalabras)- 1 por que el len arranca la cuenta de 1 y los indices de 0 
palabraSecreta = listaPalabras[indice] # creo la variable, casa a ser un string va entre ""
vidas = 6
letrasUsadas=[] # creo una lista vacia

nombre = input("ingrese su nombre aqui : ")


print (F"""
    Bienvenido {nombre} al juego del "AHORCADO"
    La cosa es asi yo pienso una palabra y vos tratas de adivinarla
    Para eso tenes 6 vidas    
    Listo , comencemos !!!   """)
os.system("pause")


while True : # con el while True me aseguro que siempre se entre al bucle 
    letraEncontrada = 0 
    os.system("cls") # uso la libreria os y su funcion system ("cls") para limpiar la pantalla
    print("Esta es la palabra secreta :")
    print("-"*50)
    for letra in palabraSecreta:# el "for" lo usamos para itera string entre otras cosas 
        if letra in letrasUsadas:
            print(letra , end=" ")
            letraEncontrada = letraEncontrada + 1
        else:
            print("★", end=" ")# con el end=" " hacemos que no haya saltos de linea y las estrellas aparescan una al lado de la otra
    print("")
    print("-"* 50)
    if letraEncontrada == len(palabraSecreta):
        print(f"has acertado {nombre}, la palabra secreta era {palabraSecreta}¡¡¡ FELICITACIONES !!!")  
        puntaje = vidas * len(palabraSecreta)
        break     
    print("#"* 5 , "Letras ya Intentadas " , "#"*5)
    print(letrasUsadas)# aqui muestro las letras ya usadas por el usuario ,para no repetirlas 
    print("#"*50)
    print(f"Te quedan {vidas} vidas para jugar")
    print("#"*50)
    letraIngresada = input("Ingrese la letra aqui: ")# con el input interactuo con el usuario
    if letraIngresada in letrasUsadas:
        print(f"La letra {letraIngresada} ya fue ingresada, pruebe otra letra")
        os.system("pause")# aqui con la libreria os y la funcion system("pause") hago que el continue no sea tan rapido y se pueda ver el print
        continue # para que vuelva al inicio del bucle 
    else :
        letrasUsadas.append(letraIngresada)
        if letraIngresada not in palabraSecreta :# el "not in" se usa para decir si letra no esta en palabra hace esto 
             print("Has errado perdiste una vida , Prueba otra letra!!! ")
             vidas = vidas -1
             os.system("pause")
    if vidas == 0 :
        print(f"Has perdido {nombre}, la palabra secreta era {palabraSecreta}")
        puntaje = -1 * len(palabraSecreta)
        break   # lo usamos para romper el bucle 
print(f"{nombre} tu  puntaje fue de : {puntaje}")

nombre = nombre.lower()
usuario = obtenerUsuario(nombre)

if usuario : # poner asi es igual que poner if usuario == True
    usuario["puntaje"] = usuario["puntaje"] + puntaje 
    if usuario["puntaje"] <= 0 :
        usuario["puntaje"]= 0
    editarPuntaje(usuario["id"] ,usuario["puntaje"] )

else :
    if puntaje <= 0 :
        puntaje = 0
    agregarUsuario(nombre, puntaje )
    
print("Posiciones totales")

posiciones = tablaPosiciones()

for posicion in posiciones :
    print (f"{posicion['nombre']} <<>> {posicion['puntaje']}")

    
os.system("pause")
