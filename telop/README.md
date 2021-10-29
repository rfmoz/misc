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
	Hora y Día:	 23:10 08
	Referencia:	 00
	Novenales:	 04.2
	--------------------------------------------------------------------------------
	
	Mensaje:	 0/0x1052/2310x80x/042/5x1421x41/627102x10/971314972/52730141x/10/0
	
	--------------------------------------------------------------------------------


Descodificar mensaje:

	$ telop --mensaje '0/0x1052/2310x80x/042/5x1421x41/627102x10/971314972/52730141x/10/0'
	--------------------------------------------------------------------------------
	Tipo:		 0 Telegrama ordinario
	Prioridad:	 0
	T. Origen:	 001
	T. Destino:	 052
	Hora y Día:	 23:10 08
	Referencia:	 00
	Novenales:	 04.2
	--------------------------------------------------------------------------------
	
	Mensaje:	 Telegrama de prueba
	
	--------------------------------------------------------------------------------


Opciones:

        usage: telop [-h] [-p {0,4,8}] [-t {0,2,3,6,9}] [--incd {0,1,2,3,4}]
                     [-o origen] [-d destino] [-b] [--rectf {6,9}] [--diccionario]
                     [--password PASSWORD] [-r referencia] [-m MENSAJE]
                     [--batch] [-v] [--version] [-z {0,1}]
        
        optional arguments:
          -h, --help            show this help message and exit
          -p {0,4,8}, --prioridad {0,4,8}
                                prioridad -> 0-normal | 4-urgente | 8-urgentísimo
          -t {0,2,3,5,6,9}, --tipo {0,2,3,5,6,9}
                                tipo de servicio -> 0-ordinaro | 2-interno
                                3-vigilancia | 5-reanudar transmisión | 6-acuse recibo
                                | 9-rectificar
          --incd {0,1,2,3,4}    incidencia en acuse -> 1-niebla | 2-ausencia |
                                3-ocupada | 4-avería
          -o origen, --origen origen
                                torre de origen
          -d destino, --destino destino
                                torre de destino
          -b, --breve           formato fecha y hora reducido
          --rectf {6,9}         tipo de rectificación -> 6-repetir | 9-anular
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
        00 - 0       20 - k       40 - E       60 - Y       80 - =
        01 - 1       21 - l       41 - F       61 - Z       81 - >
        02 - 2       22 - m       42 - G       62 - !       82 - ?
        03 - 3       23 - n       43 - H       63 - "       83 - @
        04 - 4       24 - o       44 - I       64 - #       84 - [
        05 - 5       25 - p       45 - J       65 - $       85 - \
        06 - 6       26 - q       46 - K       66 - %       86 - ]
        07 - 7       27 - r       47 - L       67 - &       87 - ^
        08 - 8       28 - s       48 - M       68 - '       88 - _
        09 - 9       29 - t       49 - N       69 - (       89 - `
        10 - a       30 - u       50 - O       70 - )       90 - {
        11 - b       31 - v       51 - P       71 - *       91 - |
        12 - c       32 - w       52 - Q       72 - +       92 - }
        13 - d       33 - x       53 - R       73 - ,       93 - ~
        14 - e       34 - y       54 - S       74 - -       94 - Ñ
        15 - f       35 - z       55 - T       75 - .       95 - ñ
        16 - g       36 - A       56 - U       76 - /       96 - ¿
        17 - h       37 - B       57 - V       77 - :       97 -  
        18 - i       38 - C       58 - W       78 - ;       98 - €
        19 - j       39 - D       59 - X       79 - <       99 -  


### Instalación

Requiere Python 3. Descargar y ejecutar el archivo "telop"



### Notas

- Cada dígito del mensaje de texto se codifica empleando el número de la posición que ocupa en un diccionario definido en el programa (telop --diccionario). Se sustituye así el diccionario frasológico del sistema original. Resulta un telegrama de mayor extensión, pero más polivalente y fácil de implementar.

- El código de transmisión definido por Mathé se ha interpretado siendo lo más fiel posible, aunque ha sido necesaria una ligera normalización y adaptación para facilitar su tratamiento informático. En la cabecera, la posición de los valores se mantiene invariable, el formato sí varía para adaptarse a cada tipo de mensaje. El resultado es el siguiente:

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

	3  /0x10x5/234104 -> Vigilancia
	|      |       |
	|      |       |
	|      |       -- hora(2) + minutos(2) + dia(2)
	|      ---------- torre de origen(3) + torre de destino(3)
	|
	----------------- tipo de servicio(1)	

	6/0/0x10x5/2341040x/0x -> Acuse de recibo
	| |    |       |    |
	| |    |       |     - sufijo acuse de recibo([1-2])
	| |    |       ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    --------------- torre de origen(3) + torre de destino(3)
	| -------------------- prioridad(1)
	---------------------- tipo de servicio(1)	

	5/0/0x1   /03 -> Reanudar transmisión
	| |    |   |
	| |    |   |
	| |    |   -- referencia(2)
	| |    ------ torre de origen(3)
	| ----------- prioridad(1)
	------------- tipo de servicio(1)	

	9  /0x10x5/04 -> Rectificar
	|      |   |
	|      |   |
	|      |   -- referencia(2)
	|      ------ torre de origen(3) + torre de destino(3)
	|
	------------- tipo de servicio(1)	
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
Wikipedia:	https://es.wikipedia.org/wiki/Tel%C3%A9grafo_%C3%B3ptico

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

Título:		Diccionario y tablas de transmisión para el telégrafo militar de noche y día compuesto de órden del Exmo. señor Marqués del Duero
Autor:		José Maria Mathé
Fecha de pub.:	1849
Páginas:	310
Fuente:		Biblioteca Virtual de Defensa

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

### Versión web

https://rfrail3.github.io/misc/telop.htm

