#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chapas (Juego de apuestas)"""
# Copyright (C) 2017 - Ricardo F.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, os, optparse, logging, random, time

__version__ = '1.0.3'


def get_arguments():
    """Leer argumentos"""

    def enable_verbose(*_):
        """Enable verbose mode"""
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    parser = optparse.OptionParser()
    parser.add_option(
        '-j',
        dest='jugadores',
        action='store',
        type='int',
        help='Numero de jugadores virtuales',
    )
    parser.add_option(
        '-t',
        dest='tiradas',
        action='store',
        type='int',
        help='Numero de tiradas',
    )
    parser.add_option(
        '-r',
        dest='reales',
        action='store',
        type='int',
        help='Numero de jugadores reales',
    )
    parser.add_option(
        '-x',
        dest='velocidad',
        default=False,
        action='store_true',
        help='Juego modo rápido'
    )
    parser.add_option(
        '-v',
        action='callback',
        callback=enable_verbose,
        help='Verbose'
    )

    arg, _ = parser.parse_args()

    # Entrar en modo manual si no se pasan estos argumentos
    if not arg.jugadores or not arg.reales or not arg.tiradas:
        cls()
        print('          __                                                                  ')
        print('    _____/ /_  ____ _____  ____ ______    // /// //// //                      ')
        print('   / ___/ __ \/ __ `/ __ \/ __ `/ ___/   // /// //// ///// ///                ')
        print('  / /__/ / / / /_/ / /_/ / /_/ (__  )   // /// //// ///// ////// ////         ')
        print('  \___/_/ /_/\__,_/ .___/\__,_/____/   // /// //// ///// ////// ////// ////// ')
        print('                 /_/                                                          ')
        print_linea(tipo=2)

    # Leer número de jugadores virtuales
    if not arg.jugadores and arg.jugadores != 0:
        while True:
            try:
                flush_input()
                arg.jugadores = int(input('\nNúmero de jugadores virtuales: '))
                break
            except ValueError:
                print('ERROR: ¡Tiene que ser un número entero!')

    # Leer número de jugadores reales
    if not arg.reales and arg.reales != 0:
        while True:
            try:
                flush_input()
                arg.reales = int(input('\nNúmero de jugadores reales: '))
                break
            except ValueError:
                print('ERROR: ¡Tiene que ser un número entero!')

    # Leer número de tiradas
    if not arg.tiradas:
        while True:
            try:
                flush_input()
                arg.tiradas = int(input('\nNúmero de tiradas: '))
                if arg.tiradas != 0:
                    break
            except ValueError:
                print('ERROR: ¡Tiene que ser un número entero!')

    # Asignar velocidad
    if not arg.velocidad:
        arg.velocidad = 2
    else:
        arg.velocidad = 0

    logging.info('Arguments: ' + str(arg))
    return arg


def cls():
    """Limpia pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')


def flush_input():
    """limpiar buffer entrada"""
    try:
        # Para unix
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    except ImportError:
        # Para windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except:
        logging.info('Sin flush_input')


def progreso(tirada, velocidad, tiradatot):
    """Barra progreso"""

    ancho = 49

    # Añadir un caracter más si lo tiene el n. de tirada
    ancho += len(str(tirada))

    # Añadir un caracter más si lo tiene el n. de tirada total
    ancho += len(str(tiradatot))

    sys.stdout.write("%s" % (" " * ancho))
    sys.stdout.flush()
    sys.stdout.write("\b" * (ancho + 1))

    for _ in range(ancho):
        time.sleep(velocidad / 50)
        sys.stdout.write("*")
        sys.stdout.flush()

    sys.stdout.write("\n")


def print_linea(tipo):
    """Imprime linea"""
    if tipo == 1:
        print('')
        print('-' * 51)

    if tipo == 2:
        print('-' * 78)


def print_tabla(jgo, tipo):
    """Imprimir valores como tabla"""

    jgocp = jgo[:]  # Trabajar con copia

    def maxwidth(table, index):
        """Anchura máxima de columna"""
        return max([len(str(row[index])) for row in table])

    tbl = []  # Inicializar tabla
    colpad = []

    # Tabla tipo juego
    if tipo == 'juego':
        side_spaces = 3  # Espacios entre columnas
        tbl.append(['Nombre', 'Cartera', 'Apuesta', 'Total', ''])  # Titulo
        tbl.append([''] * len(tbl[0]))
        jgocp.insert(-1, {'nombre': '', 'cartera': '', 'apuesta': '', 'total': '', 'ruina': ''})  # Espacio antes baratero

        # Construir tabla para imprimir
        for cas in jgocp:
            tbl.append([str(cas['nombre']),
                        str(cas['cartera']),
                        str(cas['apuesta']),
                        str(cas['total']),
                        str(cas['ruina'])])


    # Tabla tipo resumen
    if tipo == 'resumen':
        side_spaces = 2  # Espacios entre columnas
        tbl.append(['Nombre', 'Tiradas', 'Gan', 'Perd', 'Rep', 'Ctra inicial', 'Ctra final', 'Total juego'])  # Titulo
        tbl.append([''] * len(tbl[0]))
        jgocp.insert(-1, {'nombre': '', 'tiradas': '', 'tganadas': '', 'tperdidas': '', 'repetidas': '', 'cartinicial': '', 'cartfinal': '', 'totaljuego': ''})  # Espacio antes de baratero

        # Construir tabla para imprimir
        for cas in jgocp:
            tbl.append([str(cas['nombre']),
                        str(cas['tiradas']),
                        str(cas['tganadas']),
                        str(cas['tperdidas']),
                        str(cas['repetidas']),
                        str(cas['cartinicial']),
                        str(cas['cartfinal']),
                        str(cas['totaljuego'])])

    for i in range(len(tbl[0])):
        colpad.append(maxwidth(tbl, i))

    for row in tbl:
        sys.stdout.write(str(row[0]).ljust(colpad[0]))
        for i in range(1, len(row)):
            col = str(row[i]).rjust(colpad[i] + side_spaces)
            sys.stdout.write(str('' + col))
        print('')


def asignar_carteras(jgo, resumen):
    """Asignar carteras"""

    # Cartera jugadores [cantidad] * probabilidad
    cartera = [5] * 70 +  [10] * 70 +  [20] * 70 +  [30] * 70 +  [35] * 60 +    [40] * 60 +  [50] * 60 +\
             [70] * 50 + [100] * 40 + [120] * 30 + [150] * 30 + [200] * 20 +   [300] * 20 + [400] * 10 +\
            [500] *  7 + [600] *  5 + [700] *  2 + [800] *  2 + [900] *  1 +  [1000] *  1

    # Cartera baratero [cantidad] * probabilidad
    bcartera = [300] * 10 +   [400] * 10 +   [500] * 10 +   [600] * 20 +   [700] * 20 +    [800] * 30 +\
               [900] * 30 +  [1000] * 40 +  [1200] * 40 +  [1500] * 50 +  [1700] * 50 +   [2000] * 40 +\
              [2500] * 40 +  [3000] * 30 +  [3500] * 20 +  [4000] * 10 +  [4500] * 10 +   [5000] *  9 +\
              [6000] *  8 +  [7000] *  7 +  [8000] *  5 +  [9000] *  3 + [10000] *  2 +  [11000] *  1

    print('')
    print_linea(tipo=2)
    print('')

    # Para cada usuario...
    for q, _ in enumerate(jgo):

        # Limpiar valores resumen final
        jgo[q]['ruina'] = ''
        resumen[q]['tiradas'] = 0
        resumen[q]['tganadas'] = 0
        resumen[q]['tperdidas'] = 0
        resumen[q]['repetidas'] = 0

        # Asignar a usuarios virtuales
        if jgo[q]['virtual'] is True:

            if jgo[q]['nombre'] == 'Baratero':
                tmpbcartera = float(random.choice(bcartera))
                jgo[q]['cartera'] = tmpbcartera
                resumen[q]['cartinicial'] = tmpbcartera
            else:
                tmpcartera = float(random.choice(cartera))
                jgo[q]['cartera'] = tmpcartera
                resumen[q]['cartinicial'] = tmpcartera

        # Asignar a usuarios reales
        else:
            while True:
                try:
                    flush_input()
                    rcartera = input('Cartera inicial para ' + str(jgo[q]['nombre']) + ': ')
                    rcartera = float(rcartera.replace(',', '.'))
                    jgo[q]['cartera'] = rcartera
                    resumen[q]['cartinicial'] = rcartera
                    print('')
                    break
                except ValueError:
                    print('\nERROR: ¡Tiene que ser un número entero (Ej: 1, 10, 100) o decimal (Ej: 1.50, 5.50, 10.50)! \n')

    print_linea(tipo=2)

    return jgo, resumen


def asignar_apuestas(jgo, resumen, resultado_parejas):
    """Asignar apuestas"""

    # Apuestas [cantidad] * probabilidad
    apuestas = [0.50] * 20 +    [1] * 20 + [1.50] * 20 +  [2] * 20 + [2.50] * 20 +   [3] * 20 + [3.50] * 20 +\
                  [4] * 28 + [4.50] * 20 +    [5] * 30 +  [6] * 15 +    [7] * 15 +   [8] * 15 +    [9] * 15 +\
                 [10] * 20 +   [12] * 12 +   [15] * 13 + [20] * 14 +   [22] * 12 +  [25] * 13 +   [30] * 11 +\
                 [35] * 10 +   [40] * 10 +   [45] *  9 + [50] * 10 +   [55] *  8 +  [60] *  7 +   [65] *  6 +\
                 [70] *  5 +   [75] *  5 +   [80] *  2 + [90] *  2 +  [100] *  3 + [120] *  1 +  [150] *  1 +\
                [200] *  1 +  [250] *  1 +  [300] *  1 +  [0] *  5

    # Asignar apuestas a los jugadores
    for q, _ in enumerate(jgo):

        # Baratero no tiene apuesta
        if jgo[q]['nombre'] == 'Baratero':
            continue

        logging.info(' - Jugador: ' + str(jgo[q]['nombre']))
        logging.info(' - Cartera: ' + str(jgo[q]['cartera']))

        # El límite de la apuesta es el valor de la cartera
        if jgo[q]['cartera'] < 0.5:  # Límite inferior de apuesta
            logging.info(' - Cartera con menos de 0.5€, no se apuesta')
            tir = 0
        else:
            resumen[q]['tiradas'] = resumen[q]['tiradas'] + 1  # Contador tiradas

            # Si se repite la tirada por no haber salido parejas, no se hace apuesta
            if resultado_parejas < 0:
                continue

            # Proceso de asignación de apuesta a usuarios reales/virtuales
            if jgo[q]['virtual'] is False:

                # Leer apuesta de jugador real
                while True:
                    try:
                        flush_input()
                        tir = input('\nApuesta ' + jgo[q]['nombre'] + ': ')
                        tir = float(tir.replace(',', '.'))
                        break
                    except ValueError:
                        print('ERROR: ¡Tiene que ser un número entero (Ej: 1, 10, 100) o decimal (Ej: 1.50, 5.50, 10.50)!')
            else:
                # Asignar apuesta a jugador virtual
                tir = float(random.choice(apuestas))

            logging.info(' - Apuesta: ' + str(tir))

            # Si la apuesta es mayor que la cartera, se busca otro valor
            if tir > jgo[q]['cartera']:
                logging.info(' - Apuesta tirada mayor que la cartera')

                if jgo[q]['virtual'] is False:

                    # Leer apuesta de jugador real
                    while tir > jgo[q]['cartera']:
                        print('La apuesta tiene que ser igual o inferior al importe en cartera')
                        print('Cartera --> ' + str(jgo[q]['cartera']))
                        while True:
                            try:
                                flush_input()
                                tir = input('\nApuesta ' + jgo[q]['nombre'] + ': ')
                                tir = float(tir.replace(',', '.'))
                                break
                            except ValueError:
                                print('ERROR: ¡Tiene que ser un número entero (Ej: 1, 10, 100) o decimal (Ej: 1.50, 5.50, 10.50)!')

                else:
                    # Asignar apuesta a jugador virtual
                    while tir > jgo[q]['cartera']:
                        tir = random.choice(apuestas)
                        logging.info(' - Nueva apuesta generada: ' + str(tir))

                logging.info(' - Tirada final: ' + str(tir))

        # Asignar apuesta resultante
        jgo[q]['apuesta'] = float(tir)

    return jgo, resumen


def asignar_nvirtual(jugadorv, jgo, resumen):
    """Asignar nombre a cada jugador virtual"""

    for j in range(1, jugadorv + 1):
        jgo.append({'nombre': "Jugador " + str(j), 'cartera': '', 'tiradas': '', 'total': '', 'ruina': '', 'virtual': True})
        resumen.append({'nombre': "Jugador " + str(j), 'tiradas': 0, 'tganadas': 0, 'tperdidas': 0, 'repetidas': 0, 'cartinicial': '', 'cartfinal': '', 'totaljuego': ''})

    return jgo, resumen


def asignar_nreal(jugadorr, jgo, jreales, resumen):
    """Asignar nombre a cada jugador real"""

    # Por cada jugador real...
    for i in range(1, jugadorr + 1):

        # Leer nombre jugador real
        while True:
            flush_input()
            rnombre = input('\nNombre jugador real ' + str(i) + ': ')
            if rnombre.lower() == 'baratero' or rnombre == '':
                print('\nERROR: Nombre no válido, introduce otro nombre')
            else:
                jrepetido = False
                for jr in jreales:
                    if rnombre.lower() == jr.lower():
                        print('\nERROR: Nombre repetido, introduce otro nombre')
                        jrepetido = True

                if jrepetido is False:
                    jreales.append(rnombre)
                    break

        # Añadir valores a la tabla de juego y a la del resumen final
        jgo.append({'nombre': str(rnombre), 'cartera': '', 'tiradas': '', 'total': '', 'ruina': '', 'virtual': False})
        resumen.append({'nombre': str(rnombre), 'tiradas': 0, 'tganadas': 0, 'tperdidas': 0, 'repetidas': 0, 'cartinicial': '', 'cartfinal': '', 'totaljuego': ''})

    return jgo, jreales, resumen


def main():
    """Lógica principal"""

    arg = get_arguments()  # Arg
    jgo = []  # Lista con la informacion del juego para cada jugador
    jreales = []  # Lista de nombres de jugadores reales
    resumen = []  # Lista para resumen final
    seguir_jugando = True  # Para salir del bucle del juego
    resultado_parejas = 0  # Controlar resultado monedas


    # Asignar jugadores virtuales
    jgo, resumen = asignar_nvirtual(arg.jugadores, jgo, resumen)

    # Asignar jugadores reales
    if arg.reales:
        print('')
        print_linea(tipo=2)
        jgo, jreales, resumen = asignar_nreal(arg.reales, jgo, jreales, resumen)

    # Asignar baratero
    jgo.append({'nombre': 'Baratero', 'cartera': '', 'tiradas': '', 'total': '', 'ruina': '', 'virtual': True})
    resumen.append({'nombre': 'Baratero', 'tiradas': 0, 'tganadas': 0, 'tperdidas': 0, 'repetidas': 0, 'cartinicial': '', 'cartfinal': '', 'totaljuego': ''})

    # Asignar carteras
    jgo, resumen = asignar_carteras(jgo, resumen)

    # Repetir juego hasta que se diga lo contrario
    while seguir_jugando is True:

        # Proceso de tirada...
        for tirada in range(1, arg.tiradas + 1):

            apuesta_total = 0  # Apuesta total de cada tirada
            jugadores_ruina = True  # Cambia a False si alguien tiene dinero en cartera

            # Tiempo de espera entre apuestas
            if tirada > 1:
                time.sleep(arg.velocidad / 2)
            else:
                print('\n¡Hagan sus apuestas!')

            # Asignar apuestas
            jgo, resumen = asignar_apuestas(jgo, resumen, resultado_parejas)
            cls()

            # Asignar apuesta al baratero
            baratero = 'Cara'
            resumen[-1]['tiradas'] = resumen[-1]['tiradas'] + 1  # Contador tiradas baratero


            # Tirada de monedas
            monedas = (random.choice(['Cara', 'Lis']), random.choice(['Cara', 'Lis']))


            # Imprimir tirada, apuesta baratero y resultado monedas
            print('\nTirada ' + str(tirada) + ' de ' + str(arg.tiradas) +  ' <' + '-' * 36)
            progreso(tirada, arg.velocidad, arg.tiradas)  # Barra progreso
            print('')

            # Imprimir resultado monedas
            print('Moneda 1: ' + str(monedas[0]))
            print('Moneda 2: ' + str(monedas[1]) + '\n')

            time.sleep(arg.velocidad / 2)  # Tiempo espera

            # Repetir / Ganar / Perder
            if monedas[0] != monedas[1]:
                resultado_parejas = -1
                print('\"`-._,-\'\"`-._,-\'     ¡Repetir!     \'-,_.´\"\'-,_.-´\"\n')
                sitb = 'repetidas'
                sitj = 'repetidas'
            elif baratero == monedas[0] == monedas[1]:
                resultado_parejas = 1
                print('-- -- -- -- --    ¡Gana Baratero!    -- -- -- -- --\n')
                sitb = 'tganadas'
                sitj = 'tperdidas'
            else:
                resultado_parejas = 2
                print('= = = = = = = =  ¡Ganan Jugadores!  = = = = = = = =\n')
                sitb = 'tperdidas'
                sitj = 'tganadas'

            time.sleep(arg.velocidad / 2)  # Tiempo espera

            # Recorrer jugadores para calcular valores
            for q, _ in enumerate(jgo):

                # Contabilizar tirada ganada/perdida/repetidas
                if jgo[q]['nombre'] == 'Baratero':
                    resumen[-1][sitb] = resumen[-1][sitb] + 1
                    continue
                else:
                    if jgo[q]['ruina'] != 'Arruinado':
                        resumen[q][sitj] = resumen[q][sitj] + 1

                # Se suma/resta la apuesta a la cartera de los jugadores
                if resultado_parejas == 1:
                    jgo[q]['total'] = round(jgo[q]['cartera'] - jgo[q]['apuesta'], 1)
                elif resultado_parejas == 2:
                    jgo[q]['total'] = round(jgo[q]['cartera'] + jgo[q]['apuesta'], 1)
                else:
                    jgo[q]['total'] = round(jgo[q]['cartera'], 1)

                # Sumar todas las apuestas
                apuesta_total = apuesta_total + jgo[q]['apuesta']

            # La suma de las apuestas es la tirada del baratero
            jgo[-1]['apuesta'] = round(apuesta_total, 1)

            # Total del baratero
            if resultado_parejas == 1:
                jgo[-1]['total'] = round(jgo[-1]['cartera'] + apuesta_total, 1)
            elif resultado_parejas == 2:
                jgo[-1]['total'] = round(jgo[-1]['cartera'] - apuesta_total, 1)
            else:
                jgo[-1]['total'] = round(jgo[-1]['cartera'], 1)

            if resultado_parejas > 0:

                # Tareas post tirada previas a imprimir tabla
                for q, _ in enumerate(jgo):
    
                    # Añadir info a jugadores que se acaban de arruinar
                    if (jgo[q]['cartera'] != 0) and (jgo[q]['total'] <= 0):
                        jgo[q]['ruina'] = str('Arruinado')
    
                    # Cartera final es el total de la ultima tirada
                    resumen[q]['cartfinal'] = jgo[q]['total']
    
                    # Total juego es la perdida o ganancia entre la cartera inicial y la final
                    resumen[q]['totaljuego'] = format(resumen[q]['cartfinal'] - resumen[q]['cartinicial'], '+.01f')
   
                # Imprimir tabla del juego
                print_tabla(jgo, tipo='juego')

                print_linea(tipo=1)

                # Tareas post tirada posteriores a imprimir tabla
                for q, _ in enumerate(jgo):

                    # Avisar a jugadores reales que se acaban de arruinar
                    if (jgo[q]['cartera'] != 0) and (jgo[q]['total'] <= 0):
                        if jgo[q]['virtual'] is False:
                            print('¡Te has arruinado ' + jgo[q]['nombre'] + '!')
                            print('')
                            flush_input()
                            sjp = input("Terminar juego y salir (s/n): ")
                            while sjp.lower() not in ('s', 'n'):
                                flush_input()
                                print('')
                                sjp = input("Terminar juego y salir (s/n): ")
                            if sjp == 's':
                                seguir_jugando = False
                                print_linea(tipo=1)
                                print('')
    
                    # Actualizar importe de cartera al resultante de la tirada
                    jgo[q]['cartera'] = jgo[q]['total']
    
                    # Comprobar ruina de todos los jugadores
                    if jgo[q]['nombre'] == 'Baratero':
                        continue
                    else:
                        if jgo[q]['ruina'] != 'Arruinado':
                            jugadores_ruina = False

                # Comprobar ruinas
                if (jgo[-1]['cartera'] <= 0) or jugadores_ruina:
     
                    if jugadores_ruina:
                        print('\n### Jugadores arruinados...')
                    else:
                        print('\n### Baratero arruinado...')
    
                    seguir_jugando = False  # Salir de partida

                # Salir del proceso de tirada
                if seguir_jugando is False:
                    print_linea(tipo=1)
                    print('')
                    print_tabla(resumen, tipo='resumen')
                    print_linea(tipo=1)
                    _ = input('\nFin del juego.')
                    break


        # Si se han acabado las tiradas, preguntar para seguir jugando
        # (se seguirá la partida con las carteras resultantes de la tirada anterior)
        if tirada == arg.tiradas:

            # Imprimir tabla
            print('')
            print_tabla(resumen, tipo='resumen')

            print_linea(tipo=1)
            print('')

            print('Fin de tiradas.')
            flush_input()
            sjp = input("¿Seguir jugando otras " + str(arg.tiradas) + "? (s/n): ")
            while sjp.lower() not in ('s', 'n'):
                flush_input()
                sjp = input("¿Seguir jugando otras " + str(arg.tiradas) + "? (s/n): ")
            if sjp == 'n':
                seguir_jugando = False
            else:
                print('')
                flush_input()
                scmb = input("¿Mantener importe de las carteras actuales? (s/n): ")
                resultado_parejas = 0
                while scmb.lower() not in ('s', 'n'):
                    flush_input()
                    scmb = input("¿Mantener importe de las carteras actuales? (s/n): ")
                if scmb == 'n':
                    jgo, resumen = asignar_carteras(jgo, resumen)
                    # Volver a asignar apuestas

            print_linea(tipo=1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('')
