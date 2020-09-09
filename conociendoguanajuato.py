"""
Proyecto Pensamiento Computacional para la ingeniría
Jordana Betancourt Menchaca_A01707434
"Conociendo Guanajuato"
El programa es un menú que te aporta información acerca
de los lugares turísticos de Guanajuato e información general
de la cuidad
"""
def menu_p():
    print("         Menú Conociendo Guanajuato")
    print("\n")
    print("1.Guanajuato “Patrimonio cultural de la humanidad”")#Declaro opciones de menú
    print("2.Lugares emblemáticos")
    print("3.Festividades")
    print("4.Restaurantes y comida típica")
    print("5.Hoteles")
    print ("6.Directorio de números telefónicos")
    print("7.Plan de vacaciones en Guanajuato")
    print("8.Salir")
    print("\n")
    
def precio_vacaciones():
    suma=hotel+desayuno+turismo+comida+cena
    print("El precio por día es:",suma)
    print("")
    dias=int(input("Digite los días que se quiere quedar: "))
    costo=dias*suma
    print("El costo de sus vacaciones es de aproximadamente: $",costo)

def opcion_1():
    print("1.Guanajuato “Patrimonio cultural de la humanidad”")
    print("")
    print("1.1 ¿Por qué se dice que Guanajuato es patrimonio cultural de la humanidad?")
    print("1.2 Breve reseña histórica")
    print("0 Volver a menú principal")
    opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
    print("")
    if opcion2==1.1: #Anidación 
        print ("1.1 ¿Por qué se dice que Guanajuato es patrimonio cultural de la humanidad?")
    elif opcion2==1.2:
        print("1.2 Breve reseña histórica")
    elif opcion2==0:
            print("Volver al menú") #Saldrá al menú principal (no sé como hacerlo todavía jeje)
    else:
        print("Número de submenú incorrecto") #Se repetirá el submenú y menú hasta que digite la opcion de salir

def opcion_2():
    print("2.Lugares emblemáticos")
    print("")
    print("2.1 Alhóndiga de Granaditas")
    print("2.2 Teatro Juárez")
    print("0 Volver a menú principal")
    opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
    print("")
    if opcion2==2.1: #Anidación 
        print ("2.1 Alhóndiga de Granaditas")
    elif opcion2==2.2:
        print("2.2 Teatro Juárez")
    elif opcion2==0:
        print("Volver al menú")
    else:
        print("Número de submenú incorrecto")
        
def opcion_3():
    print("3.Festividades")
    print("")
    print("3.1 Día de la cueva")
    print("3.2 Día de las flores")
    print("0 Volver a menú principal")
    opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
    print("")
    if opcion2==3.1: #Anidación 
        print ("3.1 Día de la cueva")
    elif opcion2==3.2:
        print("3.2 Día de las flores")
    elif opcion2==0:
        print("Volver al menú")
    else:
        print("Número de submenú incorrecto")

def opcion_4():
    print("4.Restaurantes y comida típica")
    print("")
    print("4.1 Enchiladas mineras")
    print("4.2 Restaurante “Los calandrios” ")
    print("0 Volver a menú principal")
    opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
    print("")
    if opcion2==4.1: #Anidación 
        print ("4.1 Enchiladas mineras")
    elif opcion2==4.2:
        print ("4.2 Restaurante “Los calandrios” ")
    elif opcion2==0:
        print("Volver al menú")
    else:
        print("Número de submenú incorrecto")

def opcion_5():
    print("5.Hoteles")
    print("")
    print("5.1 Castillo Santa Cecilia")
    print("5.2 Hotel misión Guanajuato")
    print("0 Volver a menú principal")
    opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
    print("")
    if opcion2==5.1: #Anidación 
        print ("5.1 Castillo Santa Cecilia")
    elif opcion2==5.2:
        print ("5.2 Hotel misión Guanajuato")
    elif opcion2==0:
        print("Volver al menú")
    else:
        print("Número de submenú incorrecto")

menu_p()#Llamo a la función de menú principal

opcion=int(input("Digite la opción que desee: ")) #El usuario digita la opción que quiere con un número
print("")

if opcion==1: #IF/ ELIF/ELSE en todas las opciones del menú
    opcion_1()
        
elif opcion==2:
    opcion_2()
    
elif opcion==3:
    opcion_3()
    
elif opcion==4:
    opcion_4()

elif opcion==5:
    opcion:5()
   
elif opcion==6:
    print("6.Directorio de números telefónicos")
    print("")
    print(" Hospital General ----> 4737331576")
    print("Servicios turísticos  ----> 4736529696")

if opcion==7: #Calcular el costo de vacaciones #Operadores de igualdad,suma y multiplicación
    print("Plan de vacaciones en Guanajuato")
    print("")
    print("Calcularemos el costo aproximado por día en guanajuato ($ MX), después podrá poner el número de días que quiere estar en la cuidad.")
    print("")
    print("Si su paquete incluye desayuno, comida y cena, ponga 0 en el costo de los antes mencionados")
    print("Todos los precios son aproximados, pueden cambiar")
    print("")
    print("         Hoteles")
    print("")
    print("Posada $500")
    print("Hotel sin alberca $800, con 3 comidas incluidas $1200")
    print("Hotel con alberca $1000, con 3 comidas incluidas $1400")
    print("Hotel sin alberca en el centro $1000, con 3 comidas incluidas $1400")
    print("Hotel con alberca en el centro $1200, con 3 comidas incluidas $1600")
    print("")
    hotel=float(input("Digite el costo por noche que desea pagar: $"))
    print("")
    print("         Desayuno")
    print("")
    print( "Desayuno americano: Huevos y Hot Cakes + Jugo $75")
    print( "Desayuno mexicano: Chilaquiles con pollo + Jugo $75")
    print( "Desayuno buffet: $125")
    print("")
    desayuno=float(input("Digite el costo del desayuno: $"))
    print("")
    print("       Turismo")
    print("")
    print("Un destino $200")
    print("Dos destinos $350")
    print("Tour completo (tres destinos) $450")
    print("")
    turismo=float(input("Digite el costo de su guía de turismo: $"))
    print("")
    print("       Comida")
    print("")
    print("Fonda $100")
    print("Platillo restaurante $130")
    print("Buffet $180")
    print("")
    comida=float(input("Digite el costo de la comida: $"))
    print("")
    print("       Cena")
    print("Fonda $80")
    print("Platillo restaurante $100")
    print("Buffet $110")
    print("")
    cena=float(input("Digite el costo de la cena: $"))
    print("")
    precio_vacaciones()#Llamo a la función precio_vacaciones
