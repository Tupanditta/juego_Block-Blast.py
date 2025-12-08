####################################################

# Autor: Ander Lifeng Sola
# Alias: Tupanditta :)
# Color Favorito: Azul Stich

# Fecha: Jv 04/12/2025
# Archivo: JUEGO_BlockBlast_1.0.py
# Descripción: Block Blast el juego de bloques.

####################################################


################################            LIBRERÍAS

from random import randint


################################            FUNCIONES

#####       1. Crear y mostrar tabla

def crear_tablero(N): #Creo un tablero vacío de NxN
    #Constantes
    #Listas
    tablero = []

    #Variables
    #Cuerpo General
    for fila in range(N):
        fila_ = []
        for columna in range(N):
            fila_.append(' ')
        tablero.append(fila_)
    
    return tablero #Tablero de NxN (8x8)
    
def mostrar_tablero(tablero): #Mostrar el tablero (NOTA: No devuelvo nada)
    print() #Visual

    #Cuerpo General
    print('     ', end='')
    for columna in range(len(tablero)):
        print(columna, end='   ')
    print()

    print('   +', end=' ')
    print('- + '*8)

    for fila in range(len(tablero)):
        print(fila, ' |', end='') #Primer símbolo de cada fila
        for columna in range(len(tablero)):
            if tablero[fila][columna] != ' ':
                print('', tablero[fila][columna], '|', end='')
            else:
                print('   |', end='')

        print() #Terminar fila

        #Cambio de fila
        print('   +', end=' ')
        print('- + '*8)

    print() #Visual

#####       2. Datos del turno

def bloques_nuevos(lista_bloques): #Elije 3 bloques nuevos aleatorios de entre todas las posibilidades (lista_bloques[str])
    #Listas
    lista_bloques_nuevos = []

    #Variables
    bloque1 = 0 #Entra en el bucle ya que inicializo los tres bloques a 0
    bloque2 = 0 #Entra en el bucle ya que inicializo los tres bloques a 0
    bloque3 = 0 #Entra en el bucle ya que inicializo los tres bloques a 0

    #Cuerpo General
        #Entra en el bucle ya que inicializo los tres bloques a 0
    while bloque1 == bloque2 or bloque1 == bloque3 or bloque3 == bloque2:
        bloque1 = randint(0, len(lista_bloques) - 1) #Así puedo ir añadiendo bloques nuevos a la 'lista_bloques'
        bloque2 = randint(0, len(lista_bloques) - 1) #Así puedo ir añadiendo bloques nuevos a la 'lista_bloques'
        bloque3 = randint(0, len(lista_bloques) - 1) #Así puedo ir añadiendo bloques nuevos a la 'lista_bloques'

    lista_bloques_nuevos.append(lista_bloques[bloque1]) #Añado el bloque a la lista que mostraré con los 3 nuevos bloques
    lista_bloques_nuevos.append(lista_bloques[bloque2]) #Añado el bloque a la lista que mostraré con los 3 nuevos bloques
    lista_bloques_nuevos.append(lista_bloques[bloque3]) #Añado el bloque a la lista que mostraré con los 3 nuevos bloques

        #NOTA: SIEMPRE, en la posición 0 (bloque1), posición 1 (bloque2) y posición 2 (bloque3)
    return lista_bloques_nuevos #Devuelvo la lista con los 3 nuevos bloques (Sus respectivos nombres)
    
def matriz_bloque(bloque): #Le paso el nombre (str) de un bloque nuevo, y me devuelve su respectiva matriz
    #Matrices
        #NOTA: Una 'X' y lo demás 'O' o '_'
        #NOTA: La 'X' es el punto de anclaje (coordenada que introduce el usuario)
        #NOTA: He creado matrices, NO LISTAS
    Cuadrado_mini = [['X', 'O'], ['O', 'O']] 
    L_mini = [['X', ' '], ['O', ' '], ['O', 'O']]
    Linea_4 = [['X', 'O', 'O', 'O']]
    Linea_3 = [['X', 'O', 'O']]
    Uno = [['X']]

    #Variables
    matriz_bloque = []
    
    #Bucle condicional para asignar a 'matriz_bloque' su valor según 'bloque'
    if bloque == 'Cuadrado_mini':
        matriz_bloque = Cuadrado_mini
    elif bloque == 'L_mini':
        matriz_bloque = L_mini
    elif bloque == 'Uno':
        matriz_bloque = Uno
    elif bloque == 'Linea_3':
        matriz_bloque = Linea_3
    elif bloque == 'Linea_4':
        matriz_bloque = Linea_4

    return matriz_bloque #Devuelvo la matriz asignada al 'bloque' (str)

def mostrar_matriz_bloque(matriz_bloque): #Recoge el bloque (matriz) y lo imprime
    #Cuerpo General 
    for fila in range(len(matriz_bloque)):
        if fila != 0: 
            print(' '*13, end='') #Para que concuerde con 'Bloque X --> '
        for columna in range(len(matriz_bloque[fila])):
                print(matriz_bloque[fila][columna], end=' ')
    
        print()

def elegir_bloque_y_pos(lista_bloques_no_puestos): #devuelve una lista con el bloque y su pos
    #Listas
    lista_bloque_pos = []

    #Variables
    pos_col = -1 #Inicializamos pos_col < 0, para que entre en el bucle, me evito un if
    pos_fil = -1 #Inicializamos pos_col < 0, para que entre en el bucle, me evito un if
    num_bloque = 10 #Incializo num_bloque con 9, que no esta en lista_bloques_no_puestos, entro en el bucle si o sí

    #Cuerpo General
    num_bloque = int(input('Elije un bloque {} : '.format(lista_bloques_no_puestos))) - 1 #Las posiciones de una lista son 0, 1, 2 y NO 1, 2, 3
    while num_bloque + 1 not in lista_bloques_no_puestos:
        print('Introduzca un bloque válido')
        num_bloque = int(input('Elije un bloque {} : '.format(lista_bloques_no_puestos))) - 1 #Las posiciones de una lista son 0, 1, 2 y NO 1, 2, 3
    
    pos_fil = int(input('Introduzca la fila: '))
    pos_col = int(input('Introduzca la columna: '))
    while 0 > pos_fil or pos_fil > 7 or 0 > pos_col or pos_col > 7: #Sino error (out of range)
        print('El rango de la tabla es de índices 0-7')
        pos_fil = int(input('Introduzca la fila: '))
        pos_col = int(input('Introduzca la columna: '))
        
    
    
    lista_bloque_pos = [num_bloque, pos_fil, pos_col] 

    return lista_bloque_pos #devuelve una lista con el bloque y su pos

#####       3. Actualizar tabla

def lugar_correcto(lista_bloque_pos, matriz_bloque, tablero, avisar=True):
    #Variables
    bloque_pos_valido = True #Comienzo en True y busco un fallo

    #Coordenadas internas de X
    for fila in range(len(matriz_bloque)):
        for columna in range(len(matriz_bloque[fila])):
            if matriz_bloque[fila][columna] == 'X':
                X_fila = fila
                X_columna = columna
                break

    #Cuerpo General
    for fila in range(len(matriz_bloque)): #Voy a conseguir cuales serían las coordenadas del bloque en el tablero
        for columna in range(len(matriz_bloque[fila])):
            if matriz_bloque[fila][columna] != ' ': #Es 'O' o 'X'
                fila_destino_tablero = lista_bloque_pos[1] + (fila - X_fila) #Posición de 'X' o 'O' en el tablero
                columna_destino_tablero = lista_bloque_pos[2] + (columna - X_columna) #Posición de 'X' o 'O' en el tablero

                if 0 <= fila_destino_tablero <= 7 and 0 <= columna_destino_tablero <= 7: #Está dentro del rango del tablero
                    if tablero[fila_destino_tablero][columna_destino_tablero] != ' ': #El hueco ya está ocupado
                        if avisar: #Para evitar prints al usar la función 'bloque_cabe'
                            print('Ese hueco está ocupado')

                        bloque_pos_valido = False
                        return False #Me salgo del 'for columna', 'for fila' y de la función

                else: #Estas fuera del tablero
                    if avisar: #Para evitar prints al usar la función 'bloque_cabe'
                        print('Introduce el bloque DENTRO del tablero')
                    bloque_pos_valido = False
                    return False #Me salgo del 'for columna', 'for fila' y de la función

    return bloque_pos_valido #Booleano para saber si puedo introducir el bloque en esa posición
    print()

def colocar_bloque(lista_bloque_pos, matriz_bloque, tablero):
    #Coordenadas internas de X
    for fila in range(len(matriz_bloque)):
        for columna in range(len(matriz_bloque[fila])):
            if matriz_bloque[fila][columna] == 'X':
                X_fila = fila
                X_columna = columna
                break

    #Cuerpo General
    for fila in range(len(matriz_bloque)): #Voy a conseguir cuales serían las coordenadas del bloque en el tablero
        for columna in range(len(matriz_bloque[fila])):
            if matriz_bloque[fila][columna] != ' ': #Es 'O' o 'X'
                fila_destino_tablero = lista_bloque_pos[1] + (fila - X_fila) #Posición de 'X' o 'O' en el tablero
                columna_destino_tablero = lista_bloque_pos[2] + (columna - X_columna) #Posición de 'X' o 'O' en el tablero

                tablero[fila_destino_tablero][columna_destino_tablero] = 'O' #Cambio el 'vacío' por 'O'
                #NOTA: Solo hago este cambio porque anteriormente he verificado que puedo hacerlo (lugar_correcto)
                
    return tablero #Devuelvo el nuevo tablero

def actualizar_tablero(tablero): #Borrar lineas/columnas llenas
    #Variables
    fila_borrar = []
    columna_borrar = []
    
    #Localizar filas llenas
    for fila in range(len(tablero)): 
        if ' ' not in tablero[fila]: #No hay huecos vacíos en la fila
            fila_borrar.append(fila) #Agrego que filas estan llenas, es decir, cuales no tienen huecos vacíos

    #Localizar columnas llenas
    for columna in range(len(tablero)):
        columna_llena = True #COmienza en True y compruebo que lo sea
        for fila in range(len(tablero)):
            if tablero[fila][columna] == ' ':
                columna_llena = False #Si encuentro un hueco vacío, la columna no está llena
                break

        if columna_llena: #Será true y se ejecutará solo si no he encontrado ningún hueco vacío
            columna_borrar.append(columna)

    
    #Borrar todas las filas llenas
    for fila in range(len(fila_borrar)):
        for elemento in range(len(tablero)):
            tablero[fila_borrar[fila]][elemento] = ' '

    #Borrar todas las columnas llenas
    for columna in range(len(columna_borrar)):
        for fila in range(len(tablero)):
            tablero[fila][columna_borrar[columna]] = ' '

    return tablero

#####       4. Terminar
def bloque_cabe(tablero, matriz_bloque): #Quiero saber si hay hueco disponible para el bloque en el tablero
    #Variables
    cabe = False #Asumo que no cabe en ningún lado, y miro si es cierto

    #Cuerpo General
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            lista_bloque_pos = ['bloque', fila, columna] #Recorro todas las posiciones posibles del bloque en el tablero
            if lugar_correcto(lista_bloque_pos, matriz_bloque, tablero, avisar=False): #Compruebo si hay algún lugar_correcto (espacio donde cabe el bloque)
                cabe = True
                return True
            
    return cabe #Devuelve si hay alguna casilla donde el bloque puede insertarse (booleano)

def terminado_(tablero, matriz_bloque1, matriz_bloque2, matriz_bloque3, lista_bloques_no_puestos): #No hay huecos para introducir los nuevos bloques
    #Variables
    terminado = False #Comienzo asumiendo que todos los bloques caben
    cont_no_cabe = 0 #Inicializar contador a 0

    #Cuerpo General
    for bloque in lista_bloques_no_puestos:
        if bloque == 1:
            cabe = bloque_cabe(tablero, matriz_bloque1) #Devuelvo True si cabe, y False si no cabe
            if not cabe:
                cont_no_cabe += 1 #Cuento cuantos bloques no caben
        elif bloque == 2:
            cabe = bloque_cabe(tablero, matriz_bloque2) #Devuelvo True si cabe, y False si no cabe
            if not cabe:
                cont_no_cabe += 1 #Cuento cuantos bloques no caben
        else: #Bloque == 3
            cabe = bloque_cabe(tablero, matriz_bloque3) #Devuelvo True si cabe, y False si no cabe
            if not cabe:
                cont_no_cabe += 1 #Cuento cuantos bloques no caben
    
    if cont_no_cabe == len(lista_bloques_no_puestos): #Número de bloques que no caben y bloques que faltan por poner es igual
        terminado = True

    return terminado #Será True si al menos un bloque no cabe


################################            FUNCIÓN GENERAL

def BlockBlast():
    #####   Constantes
    N = 8

    #####   Listas
    lista_bloques = ['L_mini', 'Cuadrado_mini', 'Linea_4', 'Uno', 'Linea_3']
    lista_bloque_pos = [] #lista con el bloque que se va a introducir y su posición
    lista_bloques_no_puestos = [] #Lista con los bloques que puedo posicionar
    lista_bloques_puestos = [] #Lista con los bloques que ya no puedo posicionar
    matriz_bloque1 = [] #Matriz del bloque nuevo 1
    matriz_bloque2 = [] #Matriz del bloque nuevo 2
    matriz_bloque3 = [] #Matriz del bloque nuevo 3
    
    #####   Variables
    terminado = False #Para que el juego termine
    bloque1 = '' #Nombre del bloque 1
    bloque2 = '' #Nombre del bloque 2
    bloque3 = '' #Nombre del bloque 3
    
    #####   Cuerpo General
        ## Inicio
    tablero = crear_tablero(N) #Creo un tablero vacío de NxN
    print("¡BIENVENIDO A BLOCK BLAST - EDICIÓN TUPANDITTA!")
    mostrar_tablero(tablero)

        ## Medio Juego
    while not terminado: #Mientras pueda colocar más bloques, el juego sigue (no ha terminado)
            #Inicializar listas y variables
        lista_bloques_no_puestos = [1, 2, 3] #Siempre comienzo con 3 nuevos bloques
        lista_bloques_puestos = [] #Lista con los bloques que ya no puedo posicionar
        cont_bloques_no_puestos = 3 #Cuenta cuantos bloques quedan por poner

            # Crear 3 bloques aleatorios nuevos
        lista_bloques_nuevos = bloques_nuevos(lista_bloques) #Crear 3 bloques nuevos aleatorios de entre todas las posibilidades (lista_bloques[str])
            
            # Cambio de bloqueX (str) a matriz_bloqueX (list)
        bloque1 = lista_bloques_nuevos[0] #Asignar valor (nombre del bloque)
        bloque2 = lista_bloques_nuevos[1] #Asignar valor (nombre del bloque)
        bloque3 = lista_bloques_nuevos[2] #Asignar valor (nombre del bloque)

        matriz_bloque1 = matriz_bloque(bloque1) #Obtengo la matriz_bloque
        matriz_bloque2 = matriz_bloque(bloque2) #Obtengo la matriz_bloque
        matriz_bloque3 = matriz_bloque(bloque3) #Obtengo la matriz_bloque

        print(f'\n--- NUEVA RONDA ---')
        
        print('Bloque 1 --> ', end='')
        mostrar_matriz_bloque(matriz_bloque1) #Final: Muestro el bloque
        print() #Visual
        print('Bloque 2 --> ', end='')
        mostrar_matriz_bloque(matriz_bloque2) #Final: Muestro el bloque
        print() #Visual
        print('Bloque 3 --> ', end='')
        mostrar_matriz_bloque(matriz_bloque3) #Final: Muestro el bloque
        print() #Visual

            #El usuario escoje, posiciona y el tablero cambia
        while cont_bloques_no_puestos > 0: #Bucle termina cuando he introducido los 3 bloques, o cuando pierdes el juego
            #Variables
            bloque_pos_valido = False #Así se mete en el bucle siempre
            
            #Cuerpo General
            terminado = terminado_(tablero, matriz_bloque1, matriz_bloque2, matriz_bloque3, lista_bloques_no_puestos)
            if terminado: #No hay espacio para ningún bloque de los que faltan por introducir
                print() #Visual
                print('\n################################')
                print('#        HAS PERDIDO           #')
                print('#   No caben más bloques :(    #')
                print('################################\n')
                
                break

            while not bloque_pos_valido: #Para saber si puedo poner este bloque en esa posición
                lista_bloque_pos = elegir_bloque_y_pos(lista_bloques_no_puestos)

                if lista_bloque_pos[0] not in lista_bloques_puestos: #'lista_bloque_pos[0]' siempre es el número del bloque
                    #Verifico si puedo insertar el bloque en la posición
                    if lista_bloque_pos[0] == 0:
                        bloque_pos_valido = lugar_correcto(lista_bloque_pos, matriz_bloque1, tablero) #Si me devuelve True, borro el bloque de lista_bloques_no_puestos y paso a pedir el siguiente bloque
                    elif lista_bloque_pos[0] == 1: 
                        bloque_pos_valido = lugar_correcto(lista_bloque_pos, matriz_bloque2, tablero)
                    else:
                        bloque_pos_valido = lugar_correcto(lista_bloque_pos, matriz_bloque3, tablero)

                    #Ya lo he verificado
                    if bloque_pos_valido: #Solo si la posición es válida
                        lista_bloques_no_puestos.remove(lista_bloque_pos[0] + 1) #Elimino de la 'lista_bloques_no_puestos' los bloques que voy poniendo
                
                else:
                    print('Ya has introducido este bloque antes')
                
            lista_bloques_puestos.append(lista_bloque_pos[0]) #Añado el bloque que he puesto. En este punto el bloque está bien puesto; su posición es válida

            #Añado el bloque al tablero
            if lista_bloque_pos[0] == 0:
                tablero = colocar_bloque(lista_bloque_pos, matriz_bloque1, tablero)
            elif lista_bloque_pos[0] == 1: 
                tablero = colocar_bloque(lista_bloque_pos, matriz_bloque2, tablero)
            else:
                tablero = colocar_bloque(lista_bloque_pos, matriz_bloque3, tablero)

            #Actualizar Tablero
            tablero = actualizar_tablero(tablero)
            print() #Visual
            mostrar_tablero(tablero) #Muestro el tablero ya actualizado
            print() #Visual

            cont_bloques_no_puestos -= 1 #Sentencia de continuar


################################            JUGAR
BlockBlast()

