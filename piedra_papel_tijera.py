import random

def obtener_opcion_usuario():
    opciones_validas = ['piedra', 'papel', 'tijera']
    while True:
        opcion = input("Elige: piedra, papel o tijera\n").lower()
        if opcion in opciones_validas:
            return opcion
        print("Opción no válida. Intenta de nuevo: piedra, papel o tijera")

def obtener_opcion_computadora():
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(opcion_usuario, opcion_computadora):
    reglas_ganadoras = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}
    return 'Empate' if opcion_usuario == opcion_computadora else 'Usuario' if opcion_computadora == reglas_ganadoras[opcion_usuario] else 'Computadora'

def imprimir_resultado_ronda(ganador):
    print("¡Empate! Nadie pierde vidas." if ganador == 'Empate' else "¡Ganaste esta ronda!" if ganador == 'Usuario' else "¡Perdiste esta ronda!")

def jugar():
    vidas_usuario, vidas_computadora = 3, 3
    while vidas_usuario > 0 and vidas_computadora > 0:
        print(f"\nVidas: Usuario = {vidas_usuario}, Computadora = {vidas_computadora}")
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()
        print(f"Tú eliges: {opcion_usuario}\nLa computadora elige: {opcion_computadora}")
        ganador = determinar_ganador(opcion_usuario, opcion_computadora)
        imprimir_resultado_ronda(ganador)
        vidas_computadora, vidas_usuario = (vidas_computadora-1, vidas_usuario) if ganador == 'Usuario' else (vidas_computadora, vidas_usuario-1) if ganador == 'Computadora' else (vidas_computadora, vidas_usuario)
    print("\n¡Lo siento! Has perdido todas tus vidas." if vidas_usuario == 0 else "\n¡Felicidades! Has derrotado a la computadora.")

if __name__ == "__main__":
    jugar()
    input("Presiona Enter para salir.")
