import random
import time

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """

    lista = ['Piedra', 'Papel', 'Tijera']
    eleccion = int(input('Piedra (0)| Papel (1) | Tijera (2): '))

    if eleccion not in [0, 1, 2]:
        print('Opcion invalida, ingrese el numero correspondiente a su eleccion.')
        eleccion = int(input('Piedra (0)| Papel (1) | Tijera (2): '))

    compu = random.choice([0, 1, 2])
    print('\n------------------------------------------------')
    print(f'Tu elegiste {lista[eleccion]} y el compu eligio {lista[compu]}')
    mensaje = ''

    if eleccion == compu:
        mensaje = 'Empate'

    elif (eleccion == 0 and compu == 2) or (eleccion == 1 and compu == 0) or (eleccion == 2 and compu == 1):
        mensaje = 'Ganaste!'

    else:
        mensaje = 'Perdiste :('

    mensaje += '\n------------------------------------------------'

    return mensaje



def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    numero_secreto = random.randint(1, 10)
    numero = int(input('Adivine el numero del 1 al 10: '))
    print('\n------------------------------------------------')
    print(f'El compu eligio el numero {numero_secreto} y tu el numero {numero}.')
    mensaje = 'Perdiste :('

    if numero_secreto == numero:
        mensaje = 'Ganaste!'

    mensaje += '\n------------------------------------------------'

    return mensaje

def reaccion_rapida():
    """
    Esta función representa el juego de reacción rápida.
    Debes pedir al usuario que presione Enter lo más rápido posible después de que vea "GO!".
    Debes medir el tiempo que tarda el usuario en reaccionar y mostrarlo al final del juego.
    """
    print('Preparate para presionar espacio apenas veas "GO!"...')
    espera = random.randint(2, 5)
    time.sleep(espera)
    print('GO!')
    inicio = time.time()
    usuario = input()
    fin = time.time()

    print('\n------------------------------------------------')
    mensaje = f'Te demoraste {fin - inicio} segundos en reaccionar'
    mensaje += '\n------------------------------------------------'

    return mensaje


def suma_rapida():
    """
    Esta función representa el juego de suma rápida.
    Debes generar dos números al azar y pedir al usuario que los sume lo más rápido posible.
    Debes medir el tiempo que tarda el usuario en responder y mostrarlo al final del juego.
    """
    print('Preparate para sumar rapido dos numeros que apareceran...')
    espera = random.randint(1, 3)
    time.sleep(espera)
    n1 = random.randint(1,9)
    n2 = random.randint(1,9)
    print(f'{n1} + {n2}')
    inicio = time.time()
    n_usuario = int(input())
    fin = time.time()

    print('\n------------------------------------------------')
    mensaje = f'Te demoraste {fin - inicio} segundos en sumar \n'
    mensaje += f'La suma daba {n1 + n2} y respondiste {n_usuario}\n'

    if n1 + n2 == n_usuario:
        mensaje += 'Sumaste correctamente\n'
    else:
        mensaje += 'Sumaste incorrectamente\n'

    mensaje += '------------------------------------------------'

    return mensaje

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    secuencia = f'{random.randint(1,9)} {random.randint(1,9)} {random.randint(1,9)} {random.randint(1,9)} {random.randint(1,9)}'

    print('A continuacion se le mostrara una secuencia, memoricela y repitala (ingrese los numeros que vio con espacios entre medio)')
    print(secuencia)
    time.sleep(2)
    for i in range(20):
        print('')
    
    usuario = input('Repita la secuencia que vio: ')
    print('\n------------------------------------------------')
    mensaje = f'La secuencia era {secuencia} y tu ingresaste {usuario}\n'

    if usuario.split() == secuencia.split():
        mensaje += 'Acertaste :D\n'

    else:
        mensaje += 'Fallaste :(\n'

    mensaje += '------------------------------------------------'

    return mensaje