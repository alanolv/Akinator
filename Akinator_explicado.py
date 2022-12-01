#base de datos
database=[
    {"name":"iron man","humano":True,"hombre":True},
    
    {"name":"mantis","mujer":True},
    
    {"name":"rocket","hombre":True},
    
    {"name":"inventado","mujer":True,"inventado":True}
]
#funcion para comprobar la respuesta dada por el usuario
def comprobar_respuesta(answer, property):
#Establecemos la respuesta como verdadero o false, segun la respuesta del usuario
    if answer == "y":
        Respuesta = True
    else:
        Respuesta = False
#se crea la lista de los eliminados
    lista_eliminados=[]
#se recorren los personajes en la base de datos
    for d in database:
#se comprueba si la caracteristica existe en el personaje
        if property in d:
#si existe la caracteristica se compara la respuesta del usuario, 
            if Respuesta==True:
#si el personaje tiene la caracteristica y la respuesta es si, se ignora el personaje
                n=1
            else:
#si el personaje tiene la caracteristica y la respuesta es no, se agrega a la lista de los personajes por eliminar
                lista_eliminados.append(d)
#si el personaje no tiene la caracteristica pero la respuesta es no, se ignora el personaje
        elif property not in d and Respuesta==False:
            n=2
        else:
#si el personaje no tiene la caracteristica pero la respuesta es si, se agrega a la lista de personajes por eliminar
            lista_eliminados.append(d)
#se recorre la lista para eliminar
    for i in lista_eliminados:
#se borran los personajes que no coincidieron
        database.remove(i)
#se comprueba si solo hay un personaje
    if len(database) == 1:
#si solo queda un personaje se imprime, si quedan mas de uno, se sigue a la siguiente caracteristica
        print("your character is "+database[0]["name"])
        quit()


Respuesta = input("Tu personaje es humano (y,n)")
comprobar_respuesta(Respuesta, "humano")

Respuesta = input("Tu personaje es hombre (y,n)")
comprobar_respuesta(Respuesta, "hombre")
Respuesta = input("Tu personaje es mujer (y,n)")
comprobar_respuesta(Respuesta, "mujer")
Respuesta = input("Tu personaje es inventado(y,n)")
comprobar_respuesta(Respuesta, "inventado")
