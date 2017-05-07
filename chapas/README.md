Chapas
======



### Introdución

Las Chapas es un juego de azar que básicamente consiste en jugarse una cantidad de dinero a la posibilidad de que, lanzando dos monedas al aire, caigan ambas cara-cara o cruz-cruz (llamadas en este caso lis-lis).

Sólo se juga en semana santa y en determinadas zonas de España, en concreto  en Castilla y León (provincia de León y Zamora, núcleos de la provincia de Burgos como Miranda; provincia de Palencia como (Prádanos de Ojeda, Aguilar de Campoo, Alar del Rey, Herrera de Pisuerga, Saldaña, Espinosa de Villagonzalo ); La Rioja (Haro); provincia de Alicante (Confrides).

Aunque cada zona tiene su variante del juego, en este programa se ha reflejado el que se realiza en la zona Norte de la provincia de Palencia.

Más información:
https://es.wikipedia.org/wiki/Chapas_(juego_de_apuestas)



### Juego Real

El juego se lleva a cabo en lugares públicos, habitualmente un bar. Se habilita una zona libre y se crea un corro de personas que van a ser los jugadores que apuestan.

En el centro se encuentra el baratero (a veces el baratero y un tirador) que es la persona encargada de lanzar las monedas y hacer la apuesta. Para el lance sólo se utilizan dos monedas de 10 céntimos, de la épica de Alfonso XIII.

Los jugadores depositan en el suelo, delante suyo, la apuesta de dinero. El baratero elige en voz alta si va a caras o lises, coloca las monedas lis contra lis y las lanza al aire. Ahora pueden darse tres casos:

1.- Las monedas no caen iguales, lis-cara o viceversa. Tirada nula, se vuelve a apostar y tirar.

2.- Las monedas caen iguales, como había apostado el baratero. Los jugadores pierden y el baratero recoge todo el dinero del suelo.

3.- Las monedas caen iguales, pero el baratero falla la apuesta. Los jugadores ganan y el baratero tiene que poner, a cada jugador, la misma cantidad de dinero que éstos han apostado.

Así se repite todo el tiempo mientras dura el juego. El baratero puede  abandonar (siempre pagando en caso de pérdida), se puede cambiar la persona de baratero por otra persona que siga en esa función, los jugadores pueden entrar y salir en cualquier momento.



### Juego Virtual



#### Comienzo

Aunque en un principio este proyecto tenía un enfoque más estadístico, al final ha acabado reflejando el comportamiento real de una manera baste fiel.

Al ejecutar el programa lo primero que nos pide es que se indique el "Número de jugadores virtuales", es decir, el número de jugadores que va a simular el ordenador.

Seguidamente se deberá indicar el número de personas reales que van a jugar "Número de jugadores reales", se puede indicar "0" para que funcione automáticamente.

Con el "Número de tiradas" elegimos la duración de esta simulación de juego. 

En el caso de haber indicado algún número en "Número de jugadores reales", ahora se pedirá el nombre para cada uno "Nombre jugador real [nombre]"

Siguiendo con los jugadores reales, habrá que indicar la cantidad de dinero con la que comienza el juego "Cartera inicial para [nombre]"

Finalmente llega el momento de realizar la primera apuesta "Apuesta [nombre]"

Quedaría algo así:
```
------------------------------------------------------------------------------

Número de jugadores virtuales: 5

Número de jugadores reales: 1

Número de tiradas: 7

------------------------------------------------------------------------------

Nombre jugador real 1: Ricardo

------------------------------------------------------------------------------

Cartera inicial para Ricardo: 55

------------------------------------------------------------------------------

¡Hagan sus apuestas!

Apuesta Ricardo: 5
```



#### Desarrollo

Automaticamente comienza la tirada, a la derecha de la primera línea se ve la apuesta que ha realizado el baratero.

Seguidamente se indica cómo han caído las monedas.

A continuación el resultado de la tirada, pueden ganar los jugadores, el baratero o toca volver a tirar.

Se imprime la tabla con la cartera que tienen en ese momento, la apuesta realizada y el total de cómo han quedado tras la tirada.

Al final, en el caso de jugar con algún jugador real, se solicita la apuesta para la siguiente tirada.

```
Tirada 1 de 7 <-------------------------------- Lis
***********************************************

Moneda 1: Cara
Moneda 2: Cara

= = = = = = = =  ¡Ganan Jugadores!  = = = = = = = =

Nombre      Cartera   Apuesta    Total   
                                         
Jugador 1      50.0       7.0     57.0   
Jugador 2      30.0       3.0     33.0   
Jugador 3      30.0       2.5     32.5   
Jugador 4      10.0       1.0     11.0   
Jugador 5      20.0       5.0     25.0   
Ricardo        55.0       5.0     60.0   
                                         
Baratero     2500.0      23.5   2476.5   

---------------------------------------------------

Apuesta Ricardo: 10
```



#### Final

Al terminar el número de tiradas se muestra la tabla resumen. Contiene la información de cómo le ha ido el juego a cada jugador, las tiradas que ha jugado, las ganadas, perdidas y repetidas, la cartera inicial con la que comenzó, con la que acabó y lo ganado o perdido.

Si se quiere, se puede continuar jugando las mismas tiradas que ya se habían indicado. Tendremos la opción de seguir con la cartera actual o volver a asignar unas nuevas, de igual manera que si se comenzara de nuevo.

Se puede dar el caso que el baratero o los jugadores se arruinen. En ese caso el juego se dará por finalizado.
```
---------------------------------------------------

Nombre     Tiradas  Gan  Perd  Rep  Catera inicial  Catera final  Total juego
                                                                             
Jugador 1        7    2     2    3            50.0          20.0        -30.0
Jugador 2        7    2     2    3            30.0          12.5        -17.5
Jugador 3        7    2     2    3            50.0          76.5        +26.5
Jugador 4        7    2     2    3             5.0           4.5         -0.5
Jugador 5        7    2     2    3           200.0         231.5        +31.5
Ricardo          7    2     2    3            55.0          50.0         -5.0
                                                                             
Baratero         7    2     2    3           900.0         895.0         -5.0

---------------------------------------------------

Fin de tiradas.
¿Seguir jugando otras 7? (s/n):
```




### Notas

Las apuestas de los jugadores se realizan de manera aleatoria teníendo en cuenta el valor de las monedas y sus combinaciones habituales. El rango se encuentra entre 0 (sin apuesta) hasta 300. Aunque puede salir cualquier valor, se da más prioridad al rango entre 0.50 y 40.

La asignación de carteras al inicio es similar, para los jugadores el rango se encuentra entre 5 y 1000. Para el baratero las cantidades son mayores, se encuentran entre 300 y 11000. Aunque puede salir cualquier valor entre esos rangos, se da más prioridad para los jugadores a valores entre 70 y 150 y para el baratero entre 800 y 3000.  

Se pueden pasar los parámetros del juego desde la línea de comandos, las opciones son las siguientes:

Options:
  -h, --help    show this help message and exit
  -j JUGADORES  Numero de jugadores virtuales
  -t TIRADAS    Numero de tiradas
  -r REALES     Numero de jugadores reales
  -x            Juego modo rápido
  -v            Verbose

Por ejemplo, para simular 15 jugadores, 20 tiradas, ninguno real y velocidad rápida:
```
# chapas -j 15 -t 20 -r 0 -x
```


### Requisitos


- Linux, OSX o Windows
- Python 3 o posterior

Sólo se necesita tener instalado el intérprete de Python. El programa como tal no necesita instalación, funciona sólo con bajar el archivo "chapas.py" y ejecutarlo. 

En sistemas Linux, es muy probable que Python ya se encuentre instalado, sino es recomendable realizar la instalación desde el gestor de paquetes de la distribución.

Para sistemas Windows, Python se puede descargar aquí:
https://www.python.org/downloads/windows/
