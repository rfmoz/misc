telop
=======

Telop (TELégrafoÓPtico) - Utilidad para codificar y descodificar mensajes de texto empleando una interpretación del código telegráfico ideado por José María Mathé. Permite recrear el sistema utilizado por el servicio de transmisión en la red de telegrafía óptica de España a finales del s.XIX.


### Ejemplos

Codificar mensaje:

	$ telop --mensaje 'Telegrama de prueba'
	--------------------------------------------------------------------------------
	Tipo:		 0 Telegrama ordinario
	Prioridad:	 0
	T. Origen:	 001
	T. Destino:	 052
	Día y Hora:	 08 23:10
	Referencia:	 00
	Novenales:	 05.2
	--------------------------------------------------------------------------------
	
	Mensaje:	 0/0x1052/2310x80x/052/5x1421x41/627102x10/971314972/52730141x/10/0
	
	--------------------------------------------------------------------------------


Descodificar mensaje:

	$ telop --mensaje '0/0x1052/2310x80x/052/5x1421x41/627102x10/971314972/52730141x/10/0'
	--------------------------------------------------------------------------------
	Tipo:		 0 Telegrama ordinario
	Prioridad:	 0
	T. Origen:	 001
	T. Destino:	 052
	Día y Hora:	 08 23:10
	Referencia:	 00
	Novenales:	 05.2
	--------------------------------------------------------------------------------
	
	Mensaje:	 Telegrama de prueba
	
	--------------------------------------------------------------------------------


Opciones:

        usage: telop [-h] [-p {0,4,8}] [-t {0,2,3,6}] [--incd {0,1,2,3,4}] [-o origen]
                     [-d destino] [-b] [--diccionario] [--password PASSWORD]
                     [-r referencia] [-m MENSAJE] [--batch] [-v] [--version]
                     [-z {0,1}]
        
        optional arguments:
          -h, --help            show this help message and exit
          -p {0,4,8}, --prioridad {0,4,8}
                                prioridad -> 0-normal | 4-urgente | 8-urgentísimo
          -t {0,2,3,6}, --tipo {0,2,3,6}
                                tipo de servicio -> 0-ordinaro | 2-interno |
                                3-vigilancia | 6-acuse recibo
          --incd {0,1,2,3,4}    incidencia en acuse -> 1-niebla | 2-ausencia |
                                3-ocupada | 4-avería
          -o origen, --origen origen
                                torre de origen
          -d destino, --destino destino
                                torre de destino
          -b, --breve           formato fecha y hora reducido
          --diccionario         mostrar diccionario codificación
          --password PASSWORD   Codificar mensaje con contraseña
          -r referencia, --referencia referencia
                                nº referencia despacho
          -m MENSAJE, --mensaje MENSAJE
                                texto del mensaje entre ' '
          --batch               sólo imprime mensaje resultante
          -v, --verbose         debug
          --version             show program's version number and exit
          -z {0,1}              proceso a ejecutar -> (auto) | 0-codificar |
                                1-descodificar


Diccionario codificación:

        $ telop --diccionario
        --------
        Nº - Valor
        --------
        00 - 0
        01 - 1
        02 - 2
        03 - 3
        04 - 4
        05 - 5
        06 - 6
        07 - 7
        08 - 8
        09 - 9
        10 - a
        11 - b
        12 - c
        13 - d
        14 - e
        15 - f
        16 - g
        17 - h
        18 - i
        19 - j
        20 - k
        21 - l
        22 - m
        23 - n
        24 - o
        25 - p
        26 - q
        27 - r
        28 - s
        29 - t
        30 - u
        31 - v
        32 - w
        33 - x
        34 - y
        35 - z
        36 - A
        37 - B
        38 - C
        39 - D
        40 - E
        41 - F
        42 - G
        43 - H
        44 - I
        45 - J
        46 - K
        47 - L
        48 - M
        49 - N
        50 - O
        51 - P
        52 - Q
        53 - R
        54 - S
        55 - T
        56 - U
        57 - V
        58 - W
        59 - X
        60 - Y
        61 - Z
        62 - !
        63 - "
        64 - #
        65 - $
        66 - %
        67 - &
        68 - '
        69 - (
        70 - )
        71 - *
        72 - +
        73 - ,
        74 - -
        75 - .
        76 - /
        77 - :
        78 - ;
        79 - <
        80 - =
        81 - >
        82 - ?
        83 - @
        84 - [
        85 - \
        86 - ]
        87 - ^
        88 - _
        89 - `
        90 - {
        91 - |
        92 - }
        93 - ~
        94 - Ñ
        95 - ñ
        96 - ¿
        97 -  
        98 - €
        99 -  


### Instalación

Requiere Python 3. Descargar y ejecutar el archivo "telop"



### Notas

- Cada dígito del mensaje de texto se codifica empleando el número de la posición que ocupa en un diccionario definido en el programa (telop --diccionario). Se sustituye así el diccionario frasológico del sistema original. Resulta un telegrama de mayor extensión, pero más polivalente y fácil de implementar.

- También se han normalizado y adaptado las instrucciones de Mathé para facilitar su tratamiento informático. En la cabecera, por defecto, la posición y formato de los valores se mantiene invariable entre los diferentes tipos de mensajes. El resultado es el siguiente:

	```
	A/B/___C__/___D____/E
	| |    |      |     |
	| |    |      |     - sufijo particular a cada tipo de mensaje([1-3])
	| |    |      ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------- torre de origen(3) + torre de destino(3)
	| ------------------- prioridad(1)
	--------------------- tipo de servicio(1)	


	  0/0x10x5/2341040x/013/252730141/1x0/0 -> Mensaje ordinario
	  |    |       |     |   \         /  |
	  |    |       |     |    \       /   - prioridad(1)
	  |    |       |     |     ------------ novenales de mensaje
	  |    |       |     ------------------ sufijo nº de novenales completos(2) y nº de digitos en el resto(1)
	  |    |       ------------------------ hora(2) + minutos(2) + dia(2) + referencia(2)
	  |    -------------------------------- torre de origen(3) + torre de destino(3)
	  ------------------------------------- prioridad(1)

	2/0/0x10x5/2341040x/013/252730141/1x0/0 -> Comunicación interna
	| |    |       |     |   \         /  |
	| |    |       |     |    \       /   - prioridad(1)
	| |    |       |     |     ------------ novenales de mensaje
	| |    |       |     ------------------ sufijo nº de novenales completos(2) y nº de digitos en el resto(1)
	| |    |       ------------------------ hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------------------------- torre de origen(3) + torre de destino(3)
	| ------------------------------------- prioridad(1)
        --------------------------------------- tipo de servicio(1)

	3/0/0x10x5/2341040x/0 -> Vigilancia
	| |    |      |     |
	| |    |      |     - prioridad(1)
	| |    |      ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------- torre de origen(3) + torre de destino(3)
	| ------------------- prioridad(1)
	--------------------- tipo de servicio(1)	

	6/0/0x10x5/2341040x/0x -> Acuse de recibo
	| |    |      |     |
	| |    |      |     - sufijo acuse de recibo([1-2])
	| |    |      ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------- torre de origen(3) + torre de destino(3)
	| ------------------- prioridad(1)
	--------------------- tipo de servicio(1)	
	```

- Cada mensaje puede llevar un sufijo opcional registrando las interrupciones sufridas durante la transmisión. Se puede repetir el número de veces necesario. El formato es el siguiente:

	```
	/_Y_/__Z__ -> Sufijo interrupción
	  |    |
	  |    ---- hora(2) + minutos(2) + causa(1)
	  --------- torre(3)

	/011/18302 -> Sufijo interrupción
	  |    |
	  |    ---- hora(2) + minutos(2) + causa(1)
	  --------- torre(3)
	```

- En la cabecera se puede emplear otro formato de fecha y hora más reducido (opción --breve), a costa de obtener una precisión de 15 minutos.
  Son dos dígitos los que representan la hora y los minutos, el resultado se obtiene teniendo en cuenta el cuarto de hora en que se encuentran los minutos. Se suma 0, 25, 50 o 75 a la hora (00 a 24) según si es el primer, segundo, tercer o último cuarto de hora. Como ejemplo las 12:05 sería un 12, las 12:20 sería 12+25 = 37, las 12:40 sería 12+50 = 62 y las 12:55 12+75 = 87.
  El día sólo mantiene el último dígito, es decir, se representa igual el día 1 que el 11 que el 21.
  Ésta fue la modificación más curiosa de las empleadas y conocidas, por eso su codificación, el resto básicamente conseguían reducir tamaño a base de omitir información fácilmente interpretable por la situación del emisor y receptor.
  El formato de la cabecera reducida quedaría así:

    
	```
	A/B/__C__/___D____/E
	| |   |      |     |
	| |   |      |     - sufijo particular a cada tipo de mensaje([1-3])
	| |   |      ------- horaminutos(2) + dia(1) + referencia(2)
	| |   -------------- torre de origen(3) + torre de destino(3)
	| ------------------ prioridad(1)
	-------------------- tipo de servicio(1)	
	```

- Opcionalmente, mediante el uso de una contraseña (telop --password '123'), se permite encriptar/desencriptar el contenido del mensaje, manteniendo libre la cabecera. El método emplea Format-preserving, Feistel-based encryption (FFX), generando una cadena de números de apariencia aleatoria para quien intente descodificar el mensaje sin emplear la contraseña de encriptación.


### Más información

```   
Wikiepdia:	https://es.wikipedia.org/wiki/Tel%C3%A9grafo_%C3%B3ptico

Título:		Historia de la telegrafía
Fecha de pub.:	2012
Autor:		Fernando Fernández de Villegas / Amateur radio club Orense
Url:		http://www.ea1uro.com/eb3emd/Telegrafia_hist/Telegrafia_hist.htm

Título:		Historia de la telegrafía óptica en España
Autor:		Olivé Roig, Sebastián
Fecha de pub.:	1990
Páginas: 	101
Fuente:		Foro Histórico de las Telecomunicaciones

Título:		Estudio de la red de telegrafía óptica en España
Autor:		Capdevila Montes, Enrique. Slepoy Benites, Paula
Fecha de pub.:	2012
Páginas: 	456
Fuente:		Internet

Título:		Telégrafos militares : instrucción para los torreros y cartilla de servicio interior y señales particulares
Autor:		José Maria Mathé
Fecha de pub.:	1849
Páginas:	25
Fuente:		Biblioteca Virtual de Defensa

Título:		Tratado de telegrafía
Autor:		Suárez Saavedra, Antonino  
Fecha de pub.:	1880-1882
Páginas:	665 tomo 1 (interesantes 148-153)
Fuente:		Biblioteca Digital Hispánica

Título:		Tratado de telegrafía y nociones suficientes de la posta 
Autor:		Suárez Saavedra, Antonino  
Fecha de pub.:	1870
Páginas:	605 (interesantes 51-55)
Fuente:		Biblioteca Digital Hispánica

Título:		Instrucción general para el servicio de transmisión 
Autor:		José Maria Mathé
Fecha de pub.:	1850
Páginas:	24
Fuente:		Biblioteca Museo Postal y Telegráfico

Título:		Diccionario y tablas de transmisión para el telégrafo militar de noche y día
Autor:		José Maria Mathé
Fecha de pub.:	1849
Páginas:	47
Fuente:		Biblioteca Nacional

Título:		Diccionario de Telégrafos (diccionario frasológico)
Autor:		Dirección General de Telégrafos
Fecha de pub.:	1858
Páginas:	415
Fuente:		Universidad Complutense / Google Books

Título:		De torre en torre: Mensajes codificados en los cielos de la meseta
Autor:		Pasquale de Dato / Yolanda Hernández Navarro
Fecha de pub.:	2015
Páginas:	18
Fuente:		Revista Oleana Nº 30 - Ayuntamiento de Requena
```   
