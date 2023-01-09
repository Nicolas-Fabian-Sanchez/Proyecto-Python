import sqlite3

def baseDatos():
    listaPalabras=["casa","perro","gato","argentina","brasil","sillas","elefante","auto","pileta","verano","doctor"]
    conexion = sqlite3.connect("ahorcado.db")#creo la conexion con la base de datos
    cursor = conexion.cursor()#creo el cursor para porder utilizar dicha base de datos
    
    #para ejecutar algo en la base de datos uso cursor.execute
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS palabras( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT
    )
                   """)# aqui lo que hago es usar los comando sqlite desde python, Create table if not exists lo que hace 
    # me crea una tabla si no existe con una columna "id" que se incrementa solo y otra llamada "palabra" que es de formato texto
    
    cursor.execute("SELECT * FROM palabras") # con selec lo uso para consultar , aca le digo traeme todo de la tabla palabras 
    if len(cursor.fetchall()) == 0 :         # fetchall me trae un lista 
        for p in listaPalabras:
            cursor.execute (f"INSERT INTO palabras (palabra) VALUES('{p}') ") # inserto todas las palabras de la lista en la base de datos
        conexion.commit() #para guardar los cambios realizados
    
    conexion.close()#siempre al final tengo que cerrrar la base de datos
    
def listapalabras():
    conexion = sqlite3.connect("ahorcado.db")
    cursor = conexion.cursor()
    
    cursor.execute("SELECT palabra FROM palabras")#el cursor seleciona todas las palabras de la tabla palabras
    resultado =[]
    for fila in cursor : #recordar que el cursor tiene memoria y se puede iterar
        resultado.append(fila[0])#con append agrego cada palabra a la lista resultados 
    
    
    conexion.close()
    return resultado # tengo que retorar la lista por eso uso return
