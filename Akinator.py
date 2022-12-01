database=[
    {"name":"iron man","humano":True,"hombre":True},
    
    {"name":"mantis","mujer":True},
    
    {"name":"rocket","hombre":True},
    
    {"name":"inventado","mujer":True,"inventado":True}
]
def comprobar_respuesta(answer, property):
    if answer == "y":
        Respuesta = True
    else:
        Respuesta = False
    lista_eliminados=[]
    for d in database:
        if property in d:
            if Respuesta==True:
                n="easter egg1"
            else:
                lista_eliminados.append(d)
        elif property not in d and Respuesta==False:
            n="easter egg2"
        else:
            lista_eliminados.append(d)

    for i in lista_eliminados:

        database.remove(i)

    if len(database) == 1:

        print("your character is "+database[0]["name"])
        quit()
print("Akinator Marvel")

Respuesta = input("Tu personaje es humano (y,n)")
comprobar_respuesta(Respuesta, "humano")

Respuesta = input("Tu personaje es hombre (y,n)")
comprobar_respuesta(Respuesta, "hombre")
Respuesta = input("Tu personaje es mujer (y,n)")
comprobar_respuesta(Respuesta, "mujer")
Respuesta = input("Tu personaje es inventado(y,n)")
comprobar_respuesta(Respuesta, "inventado")
