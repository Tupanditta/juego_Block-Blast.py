# Block Blast - Lógica y Estructura

Este proyecto es una recreación en Python del juego de puzle **Block Blast**. El objetivo es encajar piezas de diferentes formas en un tablero de 8x8, eliminando filas y columnas completas para ganar espacio.

## Arquitectura del Código

El programa está dividido en diferentes funciones, las cuales se aplican en la función general del juego (`BlockBlast`).
Dichas funciones tienen como fin general...

      --> Crear (inicializar) la partida, creando la tabla 8x8 y mostrandola
      --> Pedir al usuario datos para colocar los bloques en el tablero
      --> Modificar el tablero de juego, colocando los bloques y limpiando las filas/columnas llenas
      --> Determinar cuando la partida se ha terminado

### Flujo del Código

1. Inicio: El programa comienza creando un tablero vacío de 8x8.

2. Bucle de Partida (Rondas): Se inicia el ciclo principal que se repite hasta el fin de la partida.

      //// Se generan 3 bloques aleatorios nuevos para el jugador.

      //// Bucle de Turno: Se ejecuta 3 veces (una por cada bloque disponible).

            --> Verificación de Derrota : Antes de nada, el juego comprueba si alguno de los bloques restantes cabe en el tablero.

                  % % Si no caben: El juego termina inmediatamente ("Fin del Juego").

                  % % Si caben: El turno continúa.

            --> Entrada de Datos: Se solicita al usuario qué bloque quiere usar y en qué coordenadas (fila y columna).

            --> Validación: Se comprueba si el movimiento es válido (no se sale del rango y no choca).

                  % % Si no es válido: Se pide al usuario que repita la entrada.

                  % % Si es válido: Se inserta el bloque en el tablero.

            --> Actualización: Se buscan filas o columnas completas y se eliminan del tablero.

            --> Visualización: Se muestra el estado actual del tablero al jugador.

      //// Siguiente Ronda: Una vez colocados los 3 bloques, el flujo vuelve al inicio del "Bucle de Partida" para generar nuevos bloques.

##### Optimización del Código

Actualmente el archivo "JUEGO_BlockBlast_Base" contiene el código del juego base. Es por ello que existen diferentes mejoras que se pueden implementar en el código para hacerlo más visual y entretenido (las dejo como puntos de mejora para versiones posteriores).

      --> De momento los 3 bloques aleatorios son distintos entre sí; esto se puede cambiar a que la elección de estos se base en probabilidad.
      --> Sería posible e interesante agregar un contador de puntos.
      --> Siempre habrá la posibilidad de agregar más tipos de bloques (actualmente el juego cuenta con 5 bloques diferentes).
      --> Respecto a lo visual, el programa es mejorable.
            //// Esta vez me he enfocado en la lógica interna, dejando la estética y el diseño un poco de lado.
      
