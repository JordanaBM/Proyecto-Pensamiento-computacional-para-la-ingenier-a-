from colorama import Fore, Back, Style
"""Biblioteca colorama, permite imprimir textos en colores en la consola,
incluyendo el fondo o estilo del texto"""
import json
with open("datos guanajuato.json", "r") as f:
    cadena_gto = json.load(f)
"""
Json es un formato de texto sencillo para el intercambio de datos,
permite almacenarlos en forma de diccionario para su fácil
manipulación
"""
"""
Proyecto Pensamiento Computacional para la ingeniría
Jordana Betancourt Menchaca_A01707434
"Conociendo Guanajuato"
El programa es un menú que te aporta información acerca
de los lugares turísticos de Guanajuato e información general
de la cuidad
"""
"""
=====================Funciones principales====================================
Menú y sus respectivas funciones
"""


def menu_p():  # Función que genera el menú
    # Menú color verde
    print(Fore.WHITE + Back.GREEN + "   Menú Conociendo Guanajuato \n")
    print(Style.RESET_ALL)
    # Declaro opciones de menú
    print(Fore.GREEN + cadena_gto["menu_principal"])
    print(Style.RESET_ALL)  # Aquí el texto vuele a predeterminado (negro)


def opcion_submenu(titulo, opciones): #Genera las opciones de los submenús
    print(Back.GREEN + Style.BRIGHT + titulo)
    print(Style.RESET_ALL)
    i = 0
    for linea in opciones:
        print(opciones[i])
        i = i + 1


def opcion_1():  # Función que crea un submenú de opción 1
    opcion2 = 1
    while opcion2 != 0:  # Uso de While
        opcion_submenu("1.Guanajuato “Patrimonio cultural de la humanidad”",
                       cadena_gto["submenu_1"])
        # El usuario digita la opción que quiere con un número
        opcion2 = float(input("""Digite la opción que desee con el punto
decimal, 0 para salir al menú principal: """))
        if opcion2 == 1.1:   # Anidación
            print (Style.BRIGHT + """\n1.1 ¿Por qué se dice que Guanajuato es
            patrimonio cultural de la humanidad? \n""")
            print(Style.RESET_ALL)
            print(cadena_gto["patrimonio"])
        elif opcion2 == 1.2:
            print (Style.BRIGHT + "\n1.2 Breve reseña histórica \n")
            print (Style.RESET_ALL)
            print(cadena_gto["reseña"])
        elif opcion2 == 0:
            print("Regresando a menú principal")
        else:
            print ("Número de submenú incorrecto")
    # Se repetirá el submenú y menú hasta que digite la opcion de salir


def opcion_2():  # Función que crea un submenú de opción 2
    opcion2 = 1
    while opcion2 != 0:
        opcion_submenu("2.Lugares emblemáticos \n", cadena_gto["submenu_2"])
        # El usuario digita la opción que quiere con un número decimal
        opcion2 = float(input("""Digite la opción que desee con el punto
decimal,0 para salir al menú principal: """))
        if opcion2 == 2.1:  # Anidación
            print (Style.BRIGHT+"\n2.1 Alhóndiga de Granaditas \n")
            print(Style.RESET_ALL)
            print(cadena_gto["alhondiga"])
        elif opcion2 == 2.2:
            print(Style.BRIGHT + "\n2.2 Teatro Juárez \n")
            print(Style.RESET_ALL)
            print(cadena_gto["teatro"])
        elif opcion2 == 0:
            print("Regresando al menú principal")
        else:
            print("Número de submenú incorrecto")


def opcion_3():  # Función que crea un submenú de opción 3
    opcion2 = 1
    while opcion2 != 0:
        opcion_submenu("\n3.Festividades \n", cadena_gto["submenu_3"])
        opcion2 = float(input("""Digite la opción que desee con el punto
decimal, 0 para salir al menú principal: """))
        if opcion2 == 3.1:  # Anidación
            print (Style.BRIGHT + "\n3.1 Día de la cueva")
            print(Style.RESET_ALL)
            print(cadena_gto["cueva"])
        elif opcion2 == 3.2:
            print(Style.BRIGHT + "\n3.2 Día de las flores")
            print(Style.RESET_ALL)
            print(cadena_gto["flores"])
        elif opcion2 == 0:
            print("Regresando a menú principal")
        else:
            print("Número de submenú incorrecto")


def opcion_4():  # Función que crea un submenú de opción 4
    opcion2 = 1
    while opcion2 != 0:
        opcion_submenu("4.Restaurantes y comida típica \n",
                       cadena_gto["submenu_4"])
        opcion2 = float(input("""Digite la opción que desee con el punto
decimal, 0 para salir al menú principal: """))
        if opcion2 == 4.1:  # Anidación
            print (Style.BRIGHT + "\n4.1 Enchiladas mineras")
            print(Style.RESET_ALL)
            print(cadena_gto["enchiladas"])
        elif opcion2 == 4.2:
            print (Style.BRIGHT + "\n4.2 “Charamuscas” ")
            print(Style.RESET_ALL)
            print(cadena_gto["charamuscas"])
        elif opcion2 == 4.3:
            print (Style.BRIGHT + "\n4.3 Restaurante “Los calandrios” ")
            print(Style.RESET_ALL)
            print(cadena_gto["calandrios"])
        elif opcion2 == 4.4:
            print (Style.BRIGHT + "\n4.4 Restaurante “Casa Valadez” ")
            print(Style.RESET_ALL)
            print(cadena_gto["valadez"])
        elif opcion2 == 4.5:
            print (Style.BRIGHT + "\n4.5 Restaurante “Trattoria” ")
            print(Style.RESET_ALL)
            print(cadena_gto["trattoria"])
        elif opcion2 == 4.6:
            print(Style.BRIGHT + "\n4.6 “Restaurant de la Sierra”")
            print(Style.RESET_ALL)
            print(cadena_gto["sierra"])
        elif opcion2 == 0:
            print("Regresando a menú principal")
        else:
            print("Número de submenú incorrecto")


def opcion_5():  # Función que crea un submenú de opción 5
    opcion2 = 1
    while opcion2 != 0:
        opcion_submenu("5.Hoteles \n", cadena_gto["submenu_5"])
        opcion2 = float(input("""Digite la opción que desee con el punto
decimal, 0 para salir al menú principal: """))
        if opcion2 == 5.1:  # Anidación
            print (Style.BRIGHT + "\n5.1 Castillo Santa Cecilia")
            print(Style.RESET_ALL)
            print(cadena_gto["castillo"])
        elif opcion2 == 5.2:
            print (Style.BRIGHT + "\n5.2 Hotel Misión Guanajuato")
            print(Style.RESET_ALL)
            print(cadena_gto["mision"])
        elif opcion2 == 5.3:
            print (Style.BRIGHT + "\n5.3 Hotel La Abadia")
            print(Style.RESET_ALL)
            print(cadena_gto["abadia"])
        elif opcion2 == 5.4:
            print(Style.BRIGHT + "\n5.4 Hotel Boutique 1850 ")
            print(Style.RESET_ALL)
            print(cadena_gto["1850"])
        elif opcion2 == 0:
            break
        else:
            print("Número de submenú incorrecto")


def opcion_6():  # Función que crea un submenú de opción 6
    directorio_opcion = "q"
    while directorio_opcion != "s":
        print (Style.BRIGHT)
        opcion_submenu("6.Directorio de números telefónicos\n",
                       cadena_gto["submenu_6"])
        print(Style.RESET_ALL)
# Realizo mi directorio telefónico en forma de lista (dentro de archivo)
        directorio_opcion = input("Digite la opción que desee: ")
        if directorio_opcion == "a":
            print(cadena_gto["directorio"][0])
        elif directorio_opcion == "b":
            print(cadena_gto["directorio"][1])
        elif directorio_opcion == "c":
            print(cadena_gto["directorio"][2])
        elif directorio_opcion == "d":
            print(cadena_gto["directorio"][3])
        elif directorio_opcion == "e":
            print(cadena_gto["directorio"][4])
        elif directorio_opcion == "f":
            print(cadena_gto["directorio"][5])
        elif directorio_opcion == "g":
            print(cadena_gto["directorio"][6])
        elif directorio_opcion == "h":
            print(cadena_gto["directorio"][7])
        elif directorio_opcion == "i":
            print(cadena_gto["directorio"][8])
        elif directorio_opcion == "j":
            print(cadena_gto["directorio"][9])
        elif directorio_opcion == "s":
            print("Regresando a menú principal")
        else:
            print("Letra o equivocada")

"""
=====================Funciones secundarias=================================
Contiene una función que se incluye en la opcion 7 del menú
"""


def precio_vacaciones():  # Operadores de igualdad,suma y multiplicación
    suma = hotel + desayuno + turismo + comida + cena
    print("\n El precio por día es: ", suma, "\n")
    dias = int(input("Digite los días que se quiere quedar: "))
    costo = dias*suma
    print("El costo de sus vacaciones es de aproximadamente: $", costo, "\n")
"""
========  Parte principal del programa ====================================
"""
# Uso del ciclo while, repetirá el menú hasta que la opción sea 8 (break)
opcion = 0
while opcion != 8:
    menu_p()  # Llamo a la función de menú principal
    # El usuario digita la opción que quiere con un número
    opcion = int(input("Digite la opción que desee: "))
    print("")
    """Los submenús se seguirán repitiendo hasta que el usuario
digite 0 y se regresará al menú principal"""
    if opcion == 1:   # IF/ ELIF/ELSE en todas las opciones del menú
        opcion_1()
    elif opcion == 2:
        opcion_2()
    elif opcion == 3:
        opcion_3()
    elif opcion == 4:
        opcion_4()
    elif opcion == 5:
        opcion_5()
    elif opcion == 6:
        opcion_6()
    elif opcion == 7:  # Calcular el costo de vacaciones
        # Defino mi opción 7, la única que colocaré en el main
        print(Back.GREEN + Style.BRIGHT + """Plan de vacaciones en
        Guanajuato \n""")
        print(Style.RESET_ALL)
        print(cadena_gto["submenu_7"][0])
        hotel = float(input(Fore.RED + """Digite el costo por noche que desea pagar:
        $"""))
        print(Style.RESET_ALL)
        print(cadena_gto["submenu_7"][1])
        desayuno = float(input(Fore.RED + "Digite el costo del desayuno: $"))
        print(Style.RESET_ALL)
        print(cadena_gto["submenu_7"][2])
        turismo = float(input(Fore.RED + """Digite el costo de su guía de
        turismo: $"""))
        print(Style.RESET_ALL)
        print(cadena_gto["submenu_7"][3])
        comida = float(input(Fore.RED + "Digite el costo de la comida: $"))
        print(Style.RESET_ALL)
        print(cadena_gto["submenu_7"][4])
        cena = float(input(Fore.RED + "Digite el costo de la cena: $"))
        print(Style.RESET_ALL)
        precio_vacaciones()  # Llamo a la función precio_vacaciones
    elif opcion == 8:
        print("¡Gracias, hasta pronto!")
    else:
        print ("Número de menú incorrecto")
