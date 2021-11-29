telop
=======

Telop (TELégrafoÓPtico) - Utilidad para codificar y descodificar mensajes de texto empleando una interpretación del código telegráfico ideado por José María Mathé. Permite recrear el sistema utilizado por el servicio de transmisión en la red de telegrafía óptica de España a finales del s.XIX.


### Uso Básico

**Codificar mensaje:**
```
$ telop --mensaje 'Telegrama de prueba'
--------------------------------------------------------------------------------
Tipo:		 0 Telegrama general
Prioridad:	 0
T. Origen:	 001
T. Destino:	 052
Hora y Día:	 23:10 08
Referencia:	 00
Novenales:	 04.2
--------------------------------------------------------------------------------

Mensaje:	 0/0x1052/2310x80x/042/5x1421x41/627102x10/971314972/52730141x/10/0

--------------------------------------------------------------------------------
```

**Descodificar mensaje:**
```
$ telop --mensaje '0/0x1052/2310x80x/042/5x1421x41/627102x10/971314972/52730141x/10/0'
--------------------------------------------------------------------------------
Tipo:		 0 Telegrama general
Prioridad:	 0
T. Origen:	 001
T. Destino:	 052
Hora y Día:	 23:10 08
Referencia:	 00
Novenales:	 04.2
--------------------------------------------------------------------------------

Mensaje:	 Telegrama de prueba

--------------------------------------------------------------------------------
```

### Ejemplos de  cada tipo de mensaje

**0 - General**

Mensaje habitual. Su contenido era cifrado y se enviaba entre comandancias, normalmente situadas en capital de provincia.

Cuando es recibido por una torre, ya sea la de destino o alguna intermedia, se devuelve un mensaje de "Acuse de recibo" al emisor indicando el estado de la recepción. 

- Codificar texto de la manera más sencilla de la torre '001' (por defecto) a la '041':
    > telop -d 41 -m 'Texto ejemplo' 
- Prioridad '8' con referencia '12', origen '010' y destino '050' :
    > telop -p 8 -r 12 -o 10 -d 50 -m 'Texto'


**2 - Servicio interno**

Similar a un mensaje general, pero utilizado sólo para indicaciones de servicio entre cualquier operario de torre.

- Mensaje interno de la torre '001' (por defecto) a la '045' con formato de fecha breve:
    > telop -t 2 -d 45 -b -m 'Texto ejemplo'
- Mensaje interno de la torre '045'a la '001' con formato de fecha breve:
    > telop -t 2 -o 45 -d 1 -b -m 'Texto ejemplo'


**3 - Vigilancia**

Controlar y mantener la atención sobre la línea. En reposo se mandaban cada media hora desde el inicio de línea a los extermos.

Para confirmar su recepción se devuelve otro mensaje de vigilancia indicando las torres oportunas.

- Indicar sólo comandancia de destino, con valor '99' a modo de comodín a todos los extremos de línea y ramales, origen '0', formato breve:
    > telop -t 3 -o 0 -d 99 -c -b
- Confirmación al mensaje anterior. Comandancia de origen '07' y destino '01':
    > telop -t 3 -o 7 -d 1 -c


**5 - Continuación**

Aviso para indicar la reanudación de un mensaje detenido en cualquier torre intermedia, habitualmente por causas meteorológicas o cruce con otra comunicación en curso de mayor prioridad.

- Retomar la transmisión del mensaje con torre de origen '009' y refrencia '43':
    > telop -t 5 -o 9 -r 43


**6 - Acuse de recibo**

Confirmar la recepción de un mensaje, general o de servicio interno, junto con el motivo que lo provoca.

- Recepción correcta de mensaje con referencia '12' desde la torre '040' a la torre '001':
    > telop -t 6 -o 40 -d 1 -r 12
- Recepción por niebla de mensaje con referencia '17' desde la torre '030' a la torre '001':
    > telop -t 6 -o 30 -d 1 -r 17 --incd 1


**9 - Rectificar**

Solicitar la anulación o retransmisión de un mensaje por su referencia.

- Repetir mensaje con referencia '23' desde la torre '021' a la '001':
    > telop -t 9 -o 21 -d 1 --rect 6 -r 23
- Anular mensaje con referencia '12' desde la torre '021' a la '001':
    > telop -t 9 -o 21 -d 1 --rect 9 -r 12


### Modificaciones de formato

**Fecha con formato corto**

En cualquier mensaje con fecha se puede pasar el argumento '-b' para utilizar el formato reducido:

- Mensaje con origen '010', destino '021' y formato de fecha breve:
    > telop -o 10 -d 21 -b -m 'Texto'


**Sustituir indicación de torre por comandancia**

Empleando el argumento '-c', en cualquier mensaje se puede cambiar el formato de torre, representado por tres cifras, al de comandancia, formado por dos cifras.

- Mensaje con origen '01', destino '07' y opción de comandancia:
    > telop -o 1 -d 7 -c -m 'Texto'


**Indicar sólo una torre o comandancia**

Es posible generar un mensaje con sólo un número de torre en vez del formato habitual que lleva dos, origen y destino. Con sólo una torre, se deduce el origen o destino según el sentido del mensaje y la posición que ocupa la torre en la línea. Para ello, se pasa el valor '0' a la opción de origen `telop -o 0` o destino `telop -d 0`.


### Opciones del programa:
```
usage: telop [-h] [-p {0,4,8}] [-t {0,2,3,5,6,9}] [--incd {0,1,2,3,4}]
             [-o origen] [-d destino] [-b] [--rect {6,9}] [-c]
             [--diccionario] [--password PASSWORD] [-r referencia]
             [-m MENSAJE] [--batch] [-v] [--version] [-z {0,1}]

optional arguments:
  -h, --help            show this help message and exit
  -p {0,4,8}, --prioridad {0,4,8}
                        prioridad -> 0-ordinario | 4-urgente | 8-urgentísimo
  -t {0,2,3,5,6,9}, --tipo {0,2,3,5,6,9}
                        tipo de servicio -> 0-general | 2-interno |
                        3-vigilancia | 5-continuación | 6-acuse recibo
                        | 9-rectificar
  --incd {0,1,2,3,4}    incidencia en acuse -> 1-niebla | 2-ausencia |
                        3-ocupada | 4-avería
  -o origen, --origen origen
                        torre de origen
  -d destino, --destino destino
                        torre de destino
  -b, --breve           formato fecha y hora reducido
  --rect {6,9}          tipo de rectificación -> 6-repetir | 9-anular
  -c, --comandancia     emplear n. de comandancia en origen / destino
  --diccionario         mostrar diccionario codificación
  --password PASSWORD   codificar mensaje con contraseña
  -r referencia, --referencia referencia
                        nº referencia despacho
  -m MENSAJE, --mensaje MENSAJE
                        texto del mensaje entre ' '
  --batch               sólo imprime mensaje resultante
  -v, --verbose         debug
  --version             show program's version number and exit
  -z {0,1}              proceso a ejecutar -> (auto) | 0-codificar |
                        1-descodificar
```

### Diccionario codificación:

```
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
```

### Instalación

Requiere Python 3. Descargar y ejecutar el archivo "telop"



### Notas

- Cada dígito del mensaje de texto se codifica empleando el número de la posición que ocupa en un diccionario definido en el programa (telop --diccionario). Se sustituye así el diccionario frasológico del sistema original. Resulta un telegrama de mayor extensión, pero más polivalente y fácil de implementar.

- La interpretación del código de transmisión definido por Mathé, requiere de una necesaria normalización y adaptación para facilitar su tratamiento informático. En la cabecera, la posición de los valores de cada grupo se mantiene invariable, en cambio, el formato de cada uno sí se adapta a cada tipo de mensaje. El resultado es el siguiente:

```
A/B/___C__/___D____/E
| |    |      |     |
| |    |      |     - E sufijo particular a cada tipo de mensaje([1-3])
| |    |      ------- D hora(2) + minutos(2) + dia(2) + referencia(2)
| |    -------------- C torre de origen(3) + torre de destino(3)
| ------------------- B prioridad(1)
--------------------- A tipo de servicio(1)


  0/0x10x5/2341040x/013/252730141/1x0/0 -> Mensaje general
  |    |       |     |   \         /  |
  |    |       |     |    \       /   - B prioridad(1)
  |    |       |     |     ------------ - novenales de mensaje
  |    |       |     ------------------ E sufijo nº de novenales completos(2) y nº de digitos en el resto(1)
  |    |       ------------------------ D hora(2) + minutos(2) + dia(2) + referencia(2)
  |    -------------------------------- C torre de origen(3) + torre de destino(3)
  ------------------------------------- B prioridad(1)

2  /0x10x5/2341040x/013/252730141/1x0/2 -> Comunicación interna
|      |       |     |   \         /  |
|      |       |     |    \       /   - A tipo de servicio(1)
|      |       |     |     ------------ - novenales de mensaje
|      |       |     ------------------ E sufijo nº de novenales completos(2) y nº de digitos en el resto(1)
|      |       ------------------------ D hora(2) + minutos(2) + dia(2) + referencia(2)
|      -------------------------------- C torre de origen(3) + torre de destino(3)
|
--------------------------------------- A tipo de servicio(1)

3  /0x10x5/234104 -> Vigilancia
|      |       |
|      |       |
|      |       -- D hora(2) + minutos(2) + dia(2)
|      ---------- C torre de origen(3) + torre de destino(3)
|
----------------- A tipo de servicio(1)

6/0/0x10x5/2341040x/0x -> Acuse de recibo
| |    |       |    |
| |    |       |    -- E sufijo acuse de recibo([1-2])
| |    |       ------- D hora(2) + minutos(2) + dia(2) + referencia(2)
| |    --------------- C torre de origen(3) + torre de destino(3)
| -------------------- B prioridad(1)
---------------------- A tipo de servicio(1)

5/0/0x1   /03 -> Continuación
| |    |   |
| |    |   |
| |    |   -- D referencia(2)
| |    ------ C torre de origen(3)
| ----------- B prioridad(1)
------------- A tipo de servicio(1)

9  /0x10x5/04/6 -> Rectificar
|      |   |  |
|      |   |  - E sufijo tipo de petición(1) 
|      |   ---- D referencia(2)
|      -------- C torre de origen(3) + torre de destino(3)
|
--------------- A tipo de servicio(1)
```

- Cada mensaje puede llevar un sufijo indicando las interrupciones sufridas durante la transmisión, si así corresponde. Se puede repetir el número de veces necesario.
  El grupo que comprende la hora y día es opcional y puede estar compuesto de los dos valores o sólo de la hora. La causa corresponde a la misma numeración que se utiliza en el acuse de recibo -> 1-niebla | 2-ausencia | 3-ocupada | 4-avería. El formato es el siguiente:

```
/_X_/__Y__/Z -> Sufijo interrupción
  |    |   |
  |    |   -- Z causa(1)
  |    ------ Y hora(2) + minutos(2) + dia(2)
  ----------- X torre(3)

/011/183012/2 -> Sufijo interrupción
  |    |    |
  |    |    -- Z causa(1)
  |    ------- Y hora(2) + minutos(2) + dia(2)
  ------------ X torre(3)

/011/1830  /2 -> Sufijo interrupción
  |    |    |
  |    |    -- Z causa(1)
  |    ------- Y hora(2) + minutos(2)
  ------------ X torre(3)

/011       /2 -> Sufijo interrupción
  |         |
  |         -- Z causa(1)
  |
  ------------ X torre(3)
```

- En la cabecera se puede emplear un formato de fecha y hora reducido con la opción `--breve`, a costa de obtener una precisión de 15 minutos.
  Son dos dígitos los que representan la hora y los minutos, el resultado se obtiene teniendo en cuenta el cuarto de hora en que se encuentran los minutos. Se suma 0, 25, 50 o 75 a la hora (00 a 24) según si es el primer, segundo, tercer o último cuarto de hora. Como ejemplo las 12:05 sería un 12, las 12:20 sería 12+25 = 37, las 12:40 sería 12+50 = 62 y las 12:55 12+75 = 87.
  El día sólo mantiene el último dígito, es decir, se representa igual el día 1 que el 11 que el 21.
  Ésta fue la modificación más curiosa de las empleadas y conocidas, por eso su codificación, el resto básicamente conseguían reducir tamaño a base de omitir información fácilmente interpretable por la situación del emisor y receptor.
  El grupo de cabecera podría tener cualquiera de los siguientes formatos. Aunque el programa no genera todas ellas, sí las puede interpretar:
```
/12150199/ -> hora(2) + minutos(2) + dia(2) + referencia(2)
/121501/   -> hora(2) + minutos(2) + dia(2)
/37199/    -> hora_breve(2) + dia_breve(1) + referencia(2)
/371/      -> hora_breve(2) + dia_breve(1)
/99/       -> referencia(2)
```
- En la cabecera se puede indicar un número de comandancia en sustitución de la torre con la opción `--comandancia`. Pasando de emplear tres dígitos por torre a dos.
  El grupo de cabecera pasaría del formato `torre de origen(3) + torre de destino(3)` a `comandancia de origen(2) + comandancia de destino(2)`.

- Si se indica alguna torre con valor '0', se suprime la representación de la misma. El mensaje generado sólo lleva registro de una única torre o comandancia.
  El grupo de torre/comandancia podría tener cualquiera de los siguientes formatos:
```
/001051/ -> torre de origen(3) + torre de destino(3)
/0109/   -> comandancia de origen(2) + comandancia de destino(2)
/051/    -> torre(3)
/09/     -> comandancia(2)
```
- Opcionalmente, mediante el uso de una contraseña `telop --password '123'`, se permite encriptar/desencriptar el contenido del mensaje, manteniendo libre la cabecera. El método emplea Format-preserving, Feistel-based encryption (FFX), generando una cadena de números de apariencia aleatoria para quien intente descodificar el mensaje sin emplear la contraseña de encriptación.


### Interpretación del original

En el resultado de este código telegráfico, destacan los siguientes títulos de referencia:

- *Historia de la telegrafía óptica en España. Sebastián Olivé Roig. 1990*: 
  Sobresaliente obra sobre la telegrafía óptica es España. Imprescindible para conocer tanto el contexto como los detalles del sistema. El autor aporta su interpretación del código de transmisión, fundada sobre documentos y telegramas originales. Excelente base sobre la que articular el resto de información.

- *Instrucción general para el servicio de transmisión. José María Mathé. 1850*: 
  Documento elemental del sistema de transmisión. Se define la estructura de los mensajes, la marcha de las comunicaciones, las confirmaciones, cómo actuar ante problemas en la transmisión, uso de la bola y reglas genarales. Permite reconstruir la lógica de transmisión, aunque llevado a la práctica se evidencian lagunas abiertas a distintas interpretaciones.

- *Instrucción general para los torreros en el servicio telegráfico. Manuel Varela y Limia. 1846*: 
  Documento previo a la Instrucción General de Mathé del que apenas quedan algunas hojas sueltas. Parece un proyecto aún por concretar, los números se dejan sin rellenar. Las indicaciones involucran más el uso de la bola, aparentemente de una manera menos clara. Algunos artículos complementan las indicaciones del documento posterior de Mathé, otros indican maniobras diferentes.

- *Telégrafos militares : instrucción para los torreros y cartilla de servicio interior y señales particulares. José Maria Mathé. 1849*: 
  Se puede considerar el antecesor directo de la Instrución General escrita también por Mathé, de hecho, algunos artículos son copias. Aunque el aparato militar empleado dispone de menos combinaciones, son equivalentes y el fundamento de trabajo es similar. Proporciona otra prespectiva del sistema y complementa bastantes indicaciones. 

- *Tratado de telegrafía y nociones suficientes de la posta. Suárez Saavedra, Antonino. 1880*: 
  Compendio de la evolución telegráfica, reúne en varios apartados los detalles relacionados con este sistema. Aporta algunos detalles del periodo final de funcionamiento, lo que evidencia la evolución del código.

El formato de mensaje resulta de interpretar y estandarizar la información anteriormente citada, teniendo como base la Instrucción de 1850. Cada tipo de mensaje tiene sus particularidades, las cuales se detallan a continuación:

- *General / Sin indicación de servicio*: 
  Se separan los dígitos de novenales entre arriadas. Se puede considerar equivalente al indicado en la instrucción de 1850.

- *Comunicación interna / Servicio interior*: 
  Según las indicaciones de la instrucción militar de 1849, normalizando fecha, añadiendo referencia y número de novenales. Así se puede confiar en la integridad de los mensajes y gestionar las incidencias de manera eficaz, de igual modo que con el tipo general.

- *Vigilancia / Vigilancia entre extremos de línea y recepción de las mismas*: 
  Olivé indica dos tipos de vigilancias, una con hora y otra con nº de torres. La instrucción militar confirma ese formato. Su normalización agrupa ambos valores en un único mensaje, adaptándose así también al formato general.

- *Vigilancia entre comandancias*: 
  No hay ninguna referencia más que en la enumeración de 1850. Se podría sutitir por el formato propuesto de vigilancia, pero con indicación de comandancia. No implementado.

- *Acuse de recibo / Recepción de despachos*: 
  Según indicación en la instrucción de 1850, se modifica la posición del nº de registro para mantenerlo en el lugar correspondiente, se añaden los minutos a la hora y se separa convenienemente con arriadas. El resto es equivalente.

- *Reanudar transmisión / Continuación*: 
  Según indicación en la instrucción de 1850, se modifica la posición de prioridad para mantenerla en el lugar correspondiente. El resto es equivalente.

- *Rectificar*: 
  Se indica someramente al final de la instrucción de 1850 sin detalles particulares, tampoco hay más referencias en el resto de documentos. Su implementación se subordina al formato general de la manera más lógica, con el objetivo de mostrar la existencia de este tipo de mensaje.

Hay varias modificaciones que tuvieron aplicación sobre el formato principal con el objetivo de acortar caracteres. Aunque algunas sólo se empleaban sobre un tipo de mensaje, en esta interpretación se deja libre la modificación sobre cualquiera de ellos. Son las siguientes:

- *Sufijo final de interrupción*: 
  Mantiene los tres formatos posibles, con hora y día, sólo con hora o sin ese grupo. Hay referencias exactas en la instrucción de 1850 y en Olivé.

- *Formato de hora en cabecera*: 
  Aunque la instrucción de 1850 documenta una variación de formato horario con precisión a media hora, el tratado de Saavedra de 1880 propone una fórmula para aumentar la precisión a 15 minutos. Olivé confirma su uso en la época final.

- *Formato de torre o comandancia*: 
  En la época final también confirma Olivé y Saavedra la sustitución del número de torre por el de comandancia, totalmente lógico. Por otra parte, Olivé comenta la indicación única de torre o comandancia cuando el mensaje se origina en el comienzo de línea o va destinado al mismo desde cualquier otro lugar. Mathé igualmente lo registra en los ejemplos manuscritos al final de la instrucción de 1850.

- *Cifrado*: 
  Se da la opción de encriptar el mensaje con una contraseña, de esta manera el contenido es indescrifrable aún conociendo el diccionario. Viene a ser la equivalencia de la encriptación que se aplicaba sobre los mensajes entre comandancias, de la cual se recoge una indicación al inicio de uno de los diccionarios telegráfios que no se quiso dar conocimiento escrito alguno.

En el transcurso de la transmisión se podían emplear distintas combinaciones del indicador tanto para salvar los posibles problemas internos del mensaje (corregir dígitos erróneos o la extension incorrecta de novenales), como para solventar las causas que podían detener o interrumpir la correcta marcha de un mensaje (el paso de una comunicación superior o interrupcones y su posterior continuación). Al tratarse de indicaciones fuera del formato del mensaje, su implementación no procede.

La última versión de la máquina con las franjas abatibles, indicada por Saavedra, no se llegó a utilizar ni tampoco se conoce las ventajas que venía a aportar. Después de toda esta interpretación del sistema, y conociendo la finalidad de sencillez y eficiencia que regía en su diseño, es posible intuir su evolución de funcionamiento. Quizá la ampliación de signos se orientaba más en el sentido de simplificar combinaciones en situaciones complejas de control, como las interrupciones y continuaciones, que en ampliar los dígitos de transmisión, lo que hubiera requerido una revisión completa del sistema.


### Más información

```   
Título:		Historia de la telegrafía óptica en España
Autor:		Olivé Roig, Sebastián
Fecha de pub.:	1990
Páginas: 	101
Fuente:		Foro Histórico de las Telecomunicaciones

Título:		Instrucción general para el servicio de transmisión 
Autor:		José Maria Mathé
Fecha de pub.:	1850
Páginas:	24
Fuente:		Biblioteca Museo Postal y Telegráfico

Título:		Instrucción general para los torreros en el servicio telegráfico
Autor:		Manuel Varela y Limia
Fecha de pub.:	1846
Páginas:	22(incompleto)
Fuente:		Biblioteca Museo Postal y Telegráfico

Título:		Telégrafos militares : instrucción para los torreros y cartilla de servicio interior y señales particulares
Autor:		José Maria Mathé
Fecha de pub.:	1849
Páginas:	25
Fuente:		Biblioteca Virtual de Defensa

Wikipedia:	https://es.wikipedia.org/wiki/Tel%C3%A9grafo_%C3%B3ptico

Título:		Historia de la telegrafía
Fecha de pub.:	2012
Autor:		Fernando Fernández de Villegas / Amateur radio club Orense
Url:		http://www.ea1uro.com/eb3emd/Telegrafia_hist/Telegrafia_hist.htm

Título:		Estudio de la red de telegrafía óptica en España
Autor:		Capdevila Montes, Enrique. Slepoy Benites, Paula
Fecha de pub.:	2012
Páginas: 	456
Fuente:		Internet

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

Título:		The early history of data networks
Autor:		Gerard J. Holzmann / Björn Pehrson
Fecha de pub.:	1994
Páginas:	304
Fuente:		Internet Archive Open Library / https://archive.org/details/earlyhistoryofda0000holz

Título:		El progreso con retraso: La telegrafía óptica en la provincia de Cuenca
Autor:		Jesús López Requena
Fecha de pub.:	2012
Páginas:	354

VV/AA:		https://forohistorico.coit.es/index.php/wiki-telegrafia-optica/category/bibliografia-y-referencias
```   

### Versión web

https://rfrail3.github.io/misc/telop.htm

