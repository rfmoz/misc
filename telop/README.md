telop
=======

Telop (TELégrafoÓPtico) es una utilidad para codificar y descodificar mensajes de texto utilizando el código telegráfico ideado por José María Mathé. Fue utilizado por el servicio de transmisión en la red de telegrafía óptica de España a finales del s.XIX.


### Ejemplos

Codificar mensaje:

	```
	$ telop --mensaje 'Telegrama de prueba'
	--------------------------------------------------------------------------------
	Tipo:		 0 Telegrama ordinario
	Prioridad:	 0
	Origen:		 001
	Destino:	 005
	Día y Hora:	 04 23:32
	Referencia:	 00
	Novenales:	 05.2
	--------------------------------------------------------------------------------
	
	Mensaje:	 0/0x10x5/23x2040x/052/5x1421x41/627102x10/971314972/52730141x/10/0
	
	--------------------------------------------------------------------------------
	```


Descodificar mensaje:

	```
	$ telop --mensaje '0/0x10x5/23x2040x/052/5x1421x41/627102x10/971314972/52730141x/10/0'
	--------------------------------------------------------------------------------
	Tipo:		 0 Telegrama ordinario
	Prioridad:	 0
	Origen:		 001
	Destino:	 005
	Día y Hora:	 04 23:32
	Referencia:	 00
	Novenales:	 05.2
	--------------------------------------------------------------------------------
	
	Mensaje:	 Telegrama de prueba
	
	--------------------------------------------------------------------------------
	```


Opciones:

	```
	$ telop -h
	usage: telop [-h] [-p {0,4,8}] [-t {0,3,6}] [-o origen] [-d destino]
	             [--diccionario] [-r referencia] [-m MENSAJE] [-v] [-z {0,1}]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -p {0,4,8}, --prioridad {0,4,8}
        	                prioridad -> 0 ordinario | 4 urgente | 8 urgentísimo
	  -t {0,3,6}, --tipo {0,3,6}
        	                tipo -> 3 vigilancia | 6 recepción | 0 n/a
	  -o origen, --origen origen
        	                torre de origen
	  -d destino, --destino destino
        	                torre de destino
	  --diccionario         mostrar diccionario codificación
	  -r referencia, --referencia referencia
        	                nº referencia despacho
	  -m MENSAJE, --mensaje MENSAJE
        	                texto del mensaje entre ' '
	  --batch               sólo imprime mensaje
	  -v, --verbose         debug
	  -z {0,1}              servicio a ejecutar -> (auto) | 0 codificar | 1
	                        descodificar
	```



### Instalación

Requiere Python 3. Descargar y ejecutar el archivo "telop"



### Notas

- Cada dígito del mensaje de texto se codifica empleando el número de la posición que ocupa en un diccionario definido en el programa (telop --diccionario). Se sustituye así el diccionario frasológico del sistema original. Resulta un telegrama de mayor extensión, pero mucho más fácil de implementar.

- También se han normalizado y adaptado las instrucciones de Mathé para facilitar su tratamiento informático. En la cabecera, la posición y formato de los valores se mantiene invariable entre los diferentes tipos de mensajes. El resultado es el siguiente:

	```
	A/B/___C__/___D____/E
	| |    |      |     |
	| |    |      |     - sufijo particular a cada tipo de mensaje([1-3])
	| |    |      ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------- torre de origen(3) + torre de destino(3)
	| ------------------- prioridad(1)
	--------------------- tipo de servicio(1)	


	  0/0x10x5/2341040x/023/252730141/1x0/0
	  |    |       |     |      |      |  |
	  |    |       |     |      |      |  - prioridad(1)
	  |    |       |     |      ----------- novenales de mensaje
	  |    |       |     ------------------ nº de novenales(2) y nº de digitos en el último novenal(1)
	  |    |       ------------------------ hora(2) + minutos(2) + dia(2) + referencia(2)
	  |    -------------------------------- torre de origen(3) + torre de destino(3)
	  ------------------------------------- prioridad(1)


	3/0/0x10x5/2341040x/0
	| |    |      |     |
	| |    |      |     - prioridad(0)
	| |    |      ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------- torre de origen(3) + torre de destino(3)
	| ------------------- prioridad(1)
	--------------------- tipo de servicio(1)	


	6/0/0x10x5/2341040x/0x
	| |    |      |     |
	| |    |      |     - sufijo acuse de recibo(2)
	| |    |      ------- hora(2) + minutos(2) + dia(2) + referencia(2)
	| |    -------------- torre de origen(3) + torre de destino(3)
	| ------------------- prioridad(1)
	--------------------- tipo de servicio(1)	
	```



### Más información

```   
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
