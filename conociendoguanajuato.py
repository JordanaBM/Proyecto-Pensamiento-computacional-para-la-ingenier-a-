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
    días=int(input("Digite los días que se quiere quedar: "))
    costo=días*suma
    print("El costo de sus vacaciones es de aproximadamente: $",costo)
   

    

menu_p()#Llamo a la función de menúprincipal


opcion=int(input("Digite la opción que desee: ")) #El usuario digita la opción que quiere con un número, sólo está desarrolada la 7
print("")



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



    