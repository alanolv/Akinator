database=[
    {"name":"thanos", "extraterrestre":True,"hombre":True, },
    
    {"name":"iron man", "humano": True, "hombre" : True},
    
    {"name":"capitan america", "humano": True,  "hombre" : True},
    
    {"name":"spiderman","humano": True,  "hombre" : True, "poderes": True },
    
    {"name":"pantera negra", "humano": True,  "hombre" : True},

    {"name":"thor", "humano": True,  "hombre" : True, "poderes": True},
    
    {"name":"hulk", "humano": True,  "hombre" : True, "poderes": True},

    {"name":"doctor strange", "humano": True,  "hombre" : True, "poderes": True},

    {"name":"gamora", "humano": True,  "mujer" : True},

    {"name":"bruja escarlata", "humano": True,  "mujer" : True, "poderes": True},

    {"name":"la hija de antman", "humano": True,  "mujer" : True},
    
    {"name":"bucky barnes", "humano": True, "hombre" : True},

    {"name":"scott lang", "humano": True, "hombre" : True},
    
    {"name":"craneo rojo", "humano": True, "hombre" : True},

    {"name":"groot", "extraterrestre": True, "hombre" : True, "poderes": True},

    {"name":"vision", "androide": True, "hombre" : True, "poderes": True},

    {"name":"loki", "humano": True, "hombre" : True, "poderes": True},

    {"name":"peper pots", "humano": True,  "mujer" : True},

    {"name":"jane foster", "humano": True,  "mujer" : True},

    {"name":"morgan stark", "humano": True,  "mujer" : True},

    {"name":"shuri", "humano": True,  "mujer" : True},

    {"name":"henry pym", "humano": True, "hombre" : True},

    {"name":"howard stark", "humano": True, "hombre" : True},

    {"name":"star lord", "humano": True, "hombre" : True},

    {"name":"rocket racoon", "extraterrestre": True, "animal": True, "hombre" : True},

    {"name":"el anciano", "humano": True,  "mujer" : True, "poderes": True},

    {"name":"maquina de guerra", "humano": True, "hombre" : True},

    {"name":"ebony maw", "extraterrestre": True, "hombre" : True, "poderes": True},

    {"name":"falcon", "humano": True, "hombre" : True},

    {"name":"harley", "humano": True, "hombre" : True},

    {"name":"avispa", "humano": True,  "mujer" : True},

    {"name":"korg","extraterrestre": True, "hombre" : True,}, 

    {"name":"mbaku", "humano": True, "hombre" : True},

    {"name":"kraglin", "extraterrestre": True, "hombre" : True},

    {"name":"frigga", "humano": True,  "mujer" : True},

    {"name":"drax el destructor", "extraterrestre": True, "hombre" : True},

    {"name":"calavera", "humano": True, "hombre" : True},

    {"name":"corvus glalve", "extraterrestre": True, "hombre" : True},

    {"name":"may parker", "humano": True,  "mujer" : True},

    {"name":"alexander pierce", "humano": True, "hombre" : True},
    
    {"name":"valquiria", "humano": True,  "mujer" : True},
    
    {"name":"okoye", "humano": True,  "mujer" : True},

    {"name":"mantis", "humano": True,  "mujer" : True},

    {"name":"happy holgan", "humano": True, "hombre" : True},

    {"name":"proxima midnight", "humano": True,  "mujer" : True},

    {"name":"nick fury", "humano": True, "hombre" : True},

    {"name":"wong", "humano": True, "hombre" : True},

    {"name":"hope van dyne", "humano": True,  "mujer" : True},

    {"name":"maria hill", "humano": True,  "mujer" : True},

    {"name":"cooper barton", "humano": True, "hombre" : True},

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
        
print("Akinator Marvel-Endgame edition")
lista_pregunta=[]
for personaje in database:
    for caracteristica in personaje:
        if caracteristica=="name":
            n=1
        else:
            lista_pregunta.append(caracteristica)
            Respuesta = input("Tu personaje es "+caracteristica+" (y,n)")
            comprobar_respuesta(Respuesta, caracteristica)
            print(lista_pregunta)
       
print(database)
#Respuesta = input("Tu personaje es humano (y,n)")
#comprobar_respuesta(Respuesta, "humano")

#Respuesta = input("Tu personaje es hombre (y,n)")
#comprobar_respuesta(Respuesta, "hombre")
#Respuesta = input("Tu personaje es mujer (y,n)")
#comprobar_respuesta(Respuesta, "mujer")
#Respuesta = input("Tu personaje es inventado(y,n)")
#comprobar_respuesta(Respuesta, "inventado")
