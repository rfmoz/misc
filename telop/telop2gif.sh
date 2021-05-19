#!/bin/bash

#
# telop2gif.sh - Crea un GIF animado en base a un mensaje codificado por telop
#
# Ejecutar:
#            telop2gif.sh '0/0x1052/1917130x/0x8/172421x0/0'
#            telop --batch -m 'test1' | telop2gif.sh
#

D_TMP=$(mktemp -d)
F_TMP=$(mktemp).gif

# Arg1 o stdin como mensaje
if (( $# == 0 )) ; then
    txt1=$(< /dev/stdin) 
else
    txt1=${1}
fi
echo \'"$txt1"\'

# Sustituir '/' por 'a' y recoger sólo caracteres convertibles
var1=$(echo "$txt1" | tr '/' 'a' | sed 's/[^0-9,x,m,a]//g')
total=${#var1}

# Recorrer mensaje, descargar imágenes y añadir número de frame
for (( i=0; i<${#var1}; i++ )); do

	dgt=${var1:$i:1}  # Digito a procesar
	nform=$(printf "%03d" $i)  # Numero en formato '000'
	num=$(($i + 1))  # Número frame

	echo "$num/$total"
	
	wget https://rfrail3.github.io/misc/static/"$dgt".gif -qO "$D_TMP"/"$nform".gif

	convert "$D_TMP"/"$nform".gif -gravity NorthEast -fill darkgrey -pointsize 30 -annotate +10+10 "$num"/"$total" "$D_TMP"/"$nform".gif
done

# Crear gif
convert -delay 150 -loop 0 "$D_TMP"/* "$F_TMP"

# Añadir final
wget https://rfrail3.github.io/misc/static/fin.gif -qO /tmp/fin.gif && convert -delay 150 -loop 0 "$F_TMP" /tmp/fin.gif "$F_TMP"

# Optimizar
mogrify -layers optimize "$F_TMP"

echo -n 'Gif -> ' && ls "$F_TMP"
