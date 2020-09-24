from colorama import Fore, Back, Style #Biblioteca colorama, permite imprimir textos en colores en la consola, incluyendo el fondo o estilo del texto
"""
Proyecto Pensamiento Computacional para la ingeniría
Jordana Betancourt Menchaca_A01707434
"Conociendo Guanajuato"
El programa es un menú que te aporta información acerca
de los lugares turísticos de Guanajuato e información general
de la cuidad
"""
def menu_p():
    print(Fore.WHITE+ Back.GREEN +"         Menú Conociendo Guanajuato \n") #Menú color verde
    print(Style.RESET_ALL)
    print(Fore.GREEN+"1.Guanajuato “Patrimonio cultural de la humanidad”")#Declaro opciones de menú
    print("2.Lugares emblemáticos")
    print("3.Festividades")
    print("4.Restaurantes y comida típica")
    print("5.Hoteles")
    print("6.Directorio de números telefónicos")
    print("7.Plan de vacaciones en Guanajuato")
    print("8.Salir \n")
    print(Style.RESET_ALL) #Aquí el texto de consola vuele a predeterminado (negro) 
    
def precio_vacaciones():
    suma=hotel+desayuno+turismo+comida+cena
    print("El precio por día es:",suma,"\n")
    dias=int(input("Digite los días que se quiere quedar: "))
    costo=dias*suma
    print("El costo de sus vacaciones es de aproximadamente: $",costo)

def opcion_1():
    while True: #Uso de While
        print(Back.GREEN+Style.BRIGHT+"1.Guanajuato “Patrimonio cultural de la humanidad” \n")
        print(Style.RESET_ALL)
        print("1.1 ¿Por qué se dice que Guanajuato es patrimonio cultural de la humanidad?")
        print("1.2 Breve reseña histórica")
        print("0 Volver a menú principal")
        opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
        print("")
        if opcion2==1.1: #Anidación 
            print (Style.BRIGHT+"1.1 ¿Por qué se dice que Guanajuato es patrimonio cultural de la humanidad? \n")
            print(Style.RESET_ALL)
            patrimonio_gto()
        elif opcion2==1.2:
            print(Style.BRIGHT+ "1.2 Breve reseña histórica \n")
            print(Style.RESET_ALL)
            reseña_historica()
        elif opcion2==0:
            break #Saldrá al menú principal 
        else:
            print("Número de submenú incorrecto") #Se repetirá el submenú y menú hasta que digite la opcion de salir

def opcion_2():
    while True:
        print(Back.GREEN+Style.BRIGHT+"2.Lugares emblemáticos \n")
        print(Style.RESET_ALL)
        print("2.1 Alhóndiga de Granaditas")
        print("2.2 Teatro Juárez")
        print("0 Volver a menú principal")
        opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
        print("")
        if opcion2==2.1: #Anidación 
            print (Style.BRIGHT+"2.1 Alhóndiga de Granaditas \n")
            print(Style.RESET_ALL)
            alhondiga()
        elif opcion2==2.2:
            print(Style.BRIGHT+"2.2 Teatro Juárez \n")
            print(Style.RESET_ALL)
            teatro_juarez()
        elif opcion2==0:
            break
        else:
            print("Número de submenú incorrecto")
        
def opcion_3():
    while True:
        print(Back.GREEN+Style.BRIGHT+"3.Festividades \n")
        print(Style.RESET_ALL)
        print("3.1 Día de la cueva")
        print("3.2 Día de las flores")
        print("0 Volver a menú principal")
        opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
        print("")
        if opcion2==3.1: #Anidación 
            print (Style.BRIGHT+"3.1 Día de la cueva")
            print(Style.RESET_ALL)
            dia_cueva()
        elif opcion2==3.2:
            print(Style.BRIGHT+"3.2 Día de las flores")
            print(Style.RESET_ALL)
            dia_flores()
        elif opcion2==0:
            break
        else:
            print("Número de submenú incorrecto")

def opcion_4():
    while True:
        print(Back.GREEN+Style.BRIGHT+"4.Restaurantes y comida típica \n")
        print(Style.RESET_ALL)
        print("4.1 Enchiladas mineras")
        print("4.2 “Charamuscas” ")
        print("4.3 Restaurante “Los calandrios” ")
        print("4.4 Restaurante “Casa Valadez” ")
        print("4.5 Restaurante “Trattoria”")
        print("4.6 “Restaurant de la Sierra”")
        print("0 Volver a menú principal")
        opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número
        print("")
        if opcion2==4.1: #Anidación 
            print (Style.BRIGHT+"4.1 Enchiladas mineras")
            print(Style.RESET_ALL)
            enchiladas()
        elif opcion2==4.2:
            print (Style.BRIGHT+"4.2 “Charamuscas” ")
            print(Style.RESET_ALL)
            charamuscas()
        elif opcion2==4.3:
            print (Style.BRIGHT+"4.3 Restaurante “Los calandrios” ")
            print(Style.RESET_ALL)
            calandrios()
        elif opcion2==4.4:
            print (Style.BRIGHT+"4.4 Restaurante “Casa Valadez” ")
            print(Style.RESET_ALL)
            casa_valadez()
        elif opcion2==4.5:
            print (Style.BRIGHT+"4.5 Restaurante “Trattoria” ")
            print(Style.RESET_ALL)
            casa_valadez()
        elif opcion2==4.6:
            print(Style.BRIGHT+"4.6 “Restaurant de la Sierra”")
            print(Style.RESET_ALL)
            restaurant_sierra()
        elif opcion2==0:
            break
        else:
            print("Número de submenú incorrecto")

def opcion_5():
    while True:
        print(Back.GREEN+Style.BRIGHT+"5.Hoteles \n")
        print(Style.RESET_ALL)
        print("5.1 Castillo Santa Cecilia")
        print("5.2 Hotel Misión Guanajuato")
        print("5.3 Hotel La Abadia")
        print("5.4 Hotel Boutique 1850 ")
        print("0 Volver a menú principal")
        opcion2=float(input("Digite la opción que desee con el punto decimal, 0 para salir al menú principal: ")) #El usuario digita la opción que quiere con un número decimal
        print("")
        if opcion2==5.1: #Anidación 
            print (Style.BRIGHT+"5.1 Castillo Santa Cecilia")
            print(Style.RESET_ALL)
            castillo_santa_cecilia()
        elif opcion2==5.2:
            print (Style.BRIGHT+"5.2 Hotel Misión Guanajuato")
            print(Style.RESET_ALL)
            hotel_mision_guanajuato()
        elif opcion2==5.3:
            print (Style.BRIGHT+"5.3 Hotel La Abadia")
            print(Style.RESET_ALL)
            hotel_la_abadia()
        elif opcion2==5.4:
            print(Style.BRIGHT+"5.4 Hotel Boutique 1850 ")
            print(Style.RESET_ALL)
            hotel_1850()
        elif opcion2==0:
            break
        else:
            print("Número de submenú incorrecto")

def patrimonio_gto():
    print("La Lista del Patrimonio Mundial de la UNESCO es un legado de monumentos y sitios de una gran riqueza natural y cultural, que cumplen la función de crear conciencia en los pueblos sobre su valor")
    print("Guanajuato Capital fue declarada por la UNESCO como Ciudad Histórica de Guanajuato y Minas Adyacentes en diciembre de 1988; fue una de las ciudades más importantes durante el Virreinato, ya que jugó un papel de gran trascendencia en la Guerra de Independencia de México.")
    print("Ciudad colonial de bellos edificios que contienen los elementos de las dos culturas principales que la crearon: la indígena y la hispana, que marcan el origen de la nacionalidad mexicana. \n")

def reseña_historica():
    print("Los primeros pobladores del asentamiento fueron los otomíes, quienes más tarde fueron desplazados por grupos chichimecas dedicados a la caza y a la recolección y al parecen denominaron al lugar Mo-o-ti, que significa “Lugar de Metales”. Durante la dominación azteca fue llamado Paxtitlan, que en castellano es “Lugar de Paja”. El vocablo Guanajuato proviene del purepecha Quanaxhuato, y según los investigadores tiene como significado: “Lugar montuoso de ranas” \n")
    print("En el año de 1541 el virrey Don Antonio de Mendoza otorgó estas tierras a Don Rodrigo Vázquez, en recompensa por los servicios prestados durante la conquista. En 1570 se fundó legalmente el pueblo de Santa Fe de Guanajuato.")
    print("El período porfirista fue época del esplendor para la ciudad, se instala el observatorio astronómico del estado, se inaugura la estación de ferrocarril, empiezan a funcionar los tranvías, se instala el servicio telefónico y de alumbrado público con electricidad; se construye la presa “La Esperanza”, llega el cinematógrafo a la ciudad y se construyen los jardines “El cantador” y “Florencio Antillón” \n")
    print("A principios del siglo XX,  la ciudad tiene la mayor parte de sus calles empedradas.La plaza de San Roque fue el lugar en la que se originaron Los Entremeses Cervantinos en 1952 con los estudiantes de la Universidad. Estos a su vez fueron los cimientos para que en 1972 se iniciara el Festival Internacional Cervantino. \n")

def alhondiga():
    print("El Museo Regional de Guanajuato también es conocido como Alhóndiga de Granaditas, “Alhóndiga” significa en árabe “almacén o mercado de granos”, mientras que el nombre de “Granaditas” significa “granos” lo cual lo recibió popularmente porque en su interior se almacenaban granos.")
    print("La Alhóndiga de Granaditas es un emblema de nuestra identidad y nacionalidad. En ella se gestó la primera batalla insurgente y con ello el origen de la Independencia y de la Nación Mexicana. \n")
    print("Al principio este inmueble iba a funcionar como un almacenaje y venta de granos, pero esto duró poco porque ocho meses después comenzó el movimiento de Independencia y esto cambió su destino porque ante el inminente ataque de los insurgentes dirigidos por don Miguel Hidalgo y Costilla, la Alhóndiga de Granaditas sirvió de refugio a los defensores del régimen virreinal comandados por el intendente Riaño.")
    print("El 28 de septiembre de 1810 ocurrió una de las primeras y más importantes batallas de la Guerra de Independencia con la toma de la Alhóndiga de Granaditas, en la que se cubrieron de gloria las armas insurgentes lideradas por don Miguel Hidalgo y Costilla, acompañado por Ignacio Allende y Unzaga, Juan Aldama, Mariano Abasolo y Mariano Jiménez.")
    print("Esta batalla es recordada por la valentía de los mineros guanajuatenses, entre los que sin duda destacó el barretero de la mina de Mellado, Juan José de los Reyes Martínez, “El Pípila”, quien cubierto con una pesada losa para esquivar a los contendientes que se encontraban parapetados, logró quemar la puerta del baluarte y propiciar el triunfo de Hidalgo y su ejército. \n")

def teatro_juarez():
    print("Este recinto es uno de los más emblemáticos en la capital y recibe su nombre en homenaje al ex presidente Benito Juárez García. \n")
    print("Se mando a construir en 1872 por el entonces gobernador de Guanajuato, el General Florencio Antillón quien quería un teatro a la altura de los mejores del país.")
    print("Fue el arquitecto José Noriega quien estuvo inicialmente a cargo de la obra, 20 años después el arquitecto Antonio Rivas Mercado y el ingeniero Alberto Malo la reanudaron pero modificando el proyecto original de un estilo arquitectónico clásico a uno ecléctico.")
    print("Sus puertas fueron abiertas por vez primera el 27 de octubre de 1903, siendo inaugurado por el entonces presidente Porfirio Díaz en la etapa final de su mandato.")
    print("Para su inauguración el 27 de octubre de 1903 fue invitada la más alta burguesía y personalidades de México.")
    print("Los primeros en presentarse fueron la compañía Italiana de Ettore Drog, con la ópera de Giuseppe Verdi “Aída”.")
    print("Resaltan en su fachada de estilo romano dórico las esculturas vaciadas en bronce de ocho de las nueve musas, las cuales miden 3.5 metros. Inicialmente se tenían previstas las nueve, pero al retrasarse la llegada de la última, se opto por no esperarla más. \n")

def dia_cueva():
    print("En honor del santo patrono San Ignacio de Loyola, se celebra una misa en punto de la una de la tarde cada 31 de julio, en la cueva enclavada en el cerro de la Bufa, donde se encuentra una imagen del santo.")
    print("Los asistentes suben por la difícil pendiente de tierra y piedras con la finalidad de mostrar su fe y agradecer en algunos casos los milagros recibidos. Se puede ver a familias completas, niños pequeños, personas de la tercera edad e incluso gente en silla de ruedas, todo por estar presente y ser parte de dicha tradición.")
    print("Como en todo festejo, se pueden encontrar los característicos puestos de aretes hechos a mano, juguetes, antojitos e incluso alguna que otra novedad, como almohadas de personajes de caricaturas, sin faltar las cervezas.")
    print("También se hace presente la música que se escucha en cada uno de los sitios donde las familias acampan para comer y después de las 3 de la tarde pueden disfrutar de la música en vivo en el escenario ubicado en el Hormiguero, donde se observa una fuerte presencia de elementos de diferentes corporaciones de seguridad. \n")

def dia_flores():
    print("El Día de las Flores en Guanajuato capital se celebra el jueves antes del Viernes de Dolores, (día en el que se realizan altares en honor a la Virgen de los Dolores), con esta tradición se inicia la celebración de la Semana Santa y es una de las más esperadas por turistas y locales.")
    print("Anteriormente había una romántica tradición en la que hombres y mujeres caminaban alrededor del Jardín de la Unión, en distintas direcciones, los caballeros portaban una flor que en el camino otorgaban a su pareja o bien alguna doncella que les haya gustado en forma de cortejo.")
    print("Con el tiempo la manera de celebrar este día ha cambiado, en la noche del jueves se organizan fiestas en diferentes salones de la ciudad llamados “Baile de las flores”, al terminar los bailes, las personas acuden al Jardín de la Unión a observar los puestos de flores, que se colocan para que los creyentes comiencen a realizar el altar a la Virgen, y ahí las personas pueden aprovechar para regalarle una bella flor a su acompañante. \n")

def enchiladas():
    print("Guanajuato es famoso por la actividad minera y este platillo representa la versión local de las tortillas fritas bañadas en un mole elaborado con chiles, en este caso guajillos,éstas se sirven acompañadas de papas y zanahorias en cubos fritos.")
    print("Pueden ir rellenas de queso fresco y cebolla o carne. Se adornan con lechuga y a veces se acompañan con una pieza de pollo frito. Son simplemente deliciosas. \n")

def charamuscas():
    print("Son los dulces guanajuatenses por excelencia; elaborados a base de piloncillo con leche, coco y nuez,su mayoría son distinguidas por hacer alusión con sus formas a las tradicionales momias de Guanajuato. \n ")

def calandrios():
    print("Restaurante de Antojitos mexicanos, aquí podrás encontrar desde las típicas enchiladas mineras hasta un buen pozole, con un sazón casero y con precios accesibles para todos.")
    print("Ubicado en Calle Real de Marfil 6, C.P. 36251, Guanajuato,Gto,México")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")
    
def casa_valadez():
     print("Restaurante Guanajuatense ubicado en el corazón de la ciudad, fundado en marzo de 1950. Menú Gourmet Internacional y nominado como uno de los 50 mejores restaurantes de Mexico ")
     print("Dirección: Jardín de la Unión 3, Zona Centro , C.P. 6000, Guanajuato, Gto. ​México")
     print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")

def trattoria():
    print("Restaurante de cocina Italiana tradicional con un toque especial mexicano. Uso de ingredientes de alta calidad, recetas deliciosas y espacios modernos.")
    print("Ubicación: Jardin Unión , Zona Centro, C.P. 36000, centro histórico Guanajuato,Gto.México")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")

def restaurant_sierra():
    print("El Restaurante con mas tradición de la región en comida Mexicana, con una vista panorámica de la Sierra de Guanajuato, ubicado a media hora del centro de la ciudad.")
    print("Dirección: Km 14, Carretera Guanajuato-Dolores Hidalgo, C.P. 36220, Guanajuato,Gto.México")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")
    
def castillo_santa_cecilia():
    print("La historia del Castillo de Santa Cecilia se remonta algunos siglos atrás, cuando originalmente los terrenos donde se ubicaba pertenecían a la hacienda de beneficio de San Francisco Javier hacia el año de 1686.")
    print("El 27 de octubre de 1881 es visitada por el General Porfirio Díaz y el gobernador Manuel Muñoz Ledo, quienes elogian la forma como se trabajaba.") 
    print("Lamentablemente comenzó a decaer en todo Guanajuato la producción minera y muchas de las haciendas de beneficiar metales desaparecieron o disminuyeron sus actividades. Así para 1916 se convierte en albergue y hospital, permaneciendo un año en estas condiciones, hasta que por incosteabilidad fue completamente cerrada.")
    print("La propiedad fue adquirida por Don Manuel Quezada Brandy. Esta incluía además una gran extensión de terreno, donde incluso estaba un tiro de mina ya abandonado, conocido como “Santa Cecilia” y así fue como el 17 de mayo de 1951 comenzó a construir un hotel con las características de un castillo medieval.")
    print("Inaugurado en 1952 la fama del hotel creció, Manuel Quezada Brandy inicio el hotel en su primera etapa con la construcción de 20 habitaciones, en una segunda etapa Don Ricardo Orozco creció el hotel a 80 habitaciones y en la actualidad Alfonso García García y su familia lo han reacondicionado en todas sus instalaciones y aumentado el total de habitaciones a 110 unidades. \n")
    print("Dirección: Camino a la Valenciana S/N, Km. 1,San Javier Guanajuato, México. C.P. 3602 ")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")
    
def hotel_mision_guanajuato():
    print("Don Roberto Zapata Gil, donde en los años setenta, se la pasaba ideando cómo hacer nacer su propia cadena hotelera.")
    print("Funda la Promotora Hotelera La Palapa y tres años después, en 1977, le cambia el nombre a Promotora Hotelera Misión comenzando la primera cadena hotelera 100% mexicana ")
    print("Cuentan con 60 hoteles en 40 destinos equivalentes a 4,500 habitaciones distribuidas en todo el país, en Guanajuato hay un total de 138 habitaciones")
    print("Dirección:Camino Antiguo a Marfil km 2.5, col. Noria Alta, 36050, Guanajuato, Gto ")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")
    
def hotel_la_abadia():
    print(" Hoteles con decorados rústicos y elementos tradicionales únicos, Hoteles La Abadía ofrecen a sus huéspedes una verdadera experiencia de hospedaje colonial.")
    print("Admire la variedad de edificios y arquitectura barroca del Centro Histórico eligiendo a Hotel Abadía Plaza, un Hotel en Guanajuato decorado con arcos de cantera, techos de ladrillos y exquisitos elementos como jarrones de talavera y pintorescos cuadros multicolores, o recorra las principales atracciones de la ciudad eligiendo a Hotel Abadía Tradicional.")
    print("Dirección: Hotel Abadia Plaza y Abadia Tradicional ---> Carretera de Guanajuato a Dolores Hidalgo Km. 1 36020 Guanajuato México (Se encuentran ubicados uno enfrente del otro)")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")
    
def hotel_1850():
    print("Ubicado en el corazón de la ciudad, es un extraordinario inmueble de estilo clásico, pero a su vez abre sus puertas con lujo, brindando comodidad y servicios de categoría superior a sus clientes preferenciales.")
    print("Cuenta 20 exclusivas y variadas suites,que varían de lo sofisticado, a lo contemporáneo ejecutivo de lujo, tradicional, con toques originales, detalles minimalistas que logran integrar en un solo edificio versiones de decoración para diferentes gustos.")
    print("Dirección: Jardín de La Unión 7, Centro Histórico,Guanajuato, Gto. México C.P., 36250 ")
    print("Puedes consultar su teléfono en la opción 6 de Directorio Telefónico \n")
    
while True: #Uso del ciclo while, repetirá el menú hasta que la opción sea 8 (break)
    print("")
    menu_p()#Llamo a la función de menú principal
    
    opcion=int(input("Digite la opción que desee: ")) #El usuario digita la opción que quiere con un número
    print("")
    
    if opcion==1: #IF/ ELIF/ELSE en todas las opciones del menú
        opcion_1()
        
    elif opcion==2: #Los submenús se seguirán repitiendo hasta que el usuario digite 0 y se regrresará al menú principal
        opcion_2()
    
    elif opcion==3:
        opcion_3()
    
    elif opcion==4:
        opcion_4()

    elif opcion==5:
        opcion_5()
   
    elif opcion==6:
        print(Back.GREEN+Style.BRIGHT+"6.Directorio de números telefónicos \n")
        print(Style.RESET_ALL)
        print(" Hospital General ----> 4737331576")
        print("Servicios turísticos  ----> 4736529696")

    elif opcion==7: #Calcular el costo de vacaciones #Operadores de igualdad,suma y multiplicación
        print(Back.GREEN+Style.BRIGHT+"Plan de vacaciones en Guanajuato \n")
        print(Style.RESET_ALL)
        print("Calcularemos el costo aproximado por día en guanajuato ($ MX), después podrá poner el número de días que quiere estar en la cuidad. \n")
        print("Si su paquete incluye desayuno, comida y cena, ponga 0 en el costo de los antes mencionados")
        print("Todos los precios son aproximados, pueden cambiar \n")
        print("         Hoteles \n")
        print("Posada $500")
        print("Hotel sin alberca $800, con 3 comidas incluidas $1200")
        print("Hotel con alberca $1000, con 3 comidas incluidas $1400")
        print("Hotel sin alberca en el centro $1000, con 3 comidas incluidas $1400")
        print("Hotel con alberca en el centro $1200, con 3 comidas incluidas $1600 \n")
        hotel=float(input(Fore.RED+"Digite el costo por noche que desea pagar: $"))
        print(Style.RESET_ALL)
        print("")
        print("         Desayuno \n")
        print( "Desayuno americano: Huevos y Hot Cakes + Jugo $75")
        print( "Desayuno mexicano: Chilaquiles con pollo + Jugo $75")
        print( "Desayuno buffet: $125 \n")
        desayuno=float(input(Fore.RED+"Digite el costo del desayuno: $"))
        print(Style.RESET_ALL)
        print("")
        print("       Turismo \n")
        print("Un destino $200")
        print("Dos destinos $350")
        print("Tour completo (tres destinos) $450 \n")
        turismo=float(input(Fore.RED+"Digite el costo de su guía de turismo: $"))
        print(Style.RESET_ALL)
        print("")
        print("       Comida \n")
        print("Fonda $100")
        print("Platillo restaurante $130")
        print("Buffet $180 \n")
        comida=float(input(Fore.RED+"Digite el costo de la comida: $"))
        print(Style.RESET_ALL)
        print("")
        print("       Cena \n")
        print("Fonda $80")
        print("Platillo restaurante $100")
        print("Buffet $110 \n")
        cena=float(input(Fore.RED+"Digite el costo de la cena: $"))
        print(Style.RESET_ALL)
        print("")
        precio_vacaciones()#Llamo a la función precio_vacaciones

    elif opcion==8:
        print("¡Gracias, hasta pronto!")
        break
    
    else:
        print ("Número de menú incorrecto")
