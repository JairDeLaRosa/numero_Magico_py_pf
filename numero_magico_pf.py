import random

def generar_numero_magico():
    return random.randint(1, 100)

def pedir_numero():
    return int(input("Adivina el número: "))
    
def puntaje(a):
    return 7-a
        

def verificar_numero(numero_magico, numero_usuario,intentos):
    if numero_usuario < numero_magico:
        return "Más alto"
    elif numero_usuario > numero_magico:
        return "Más bajo"
    elif intentos>=10:
        return "Perdiste :("
    else:
        return "¡Correcto!"

def jugar_juego():
    numero_magico = generar_numero_magico()
    intentos = 0
    while True:
        intentos += 1
        numero_usuario = pedir_numero()
        resultado = verificar_numero(numero_magico, numero_usuario,intentos)
        puntajes=puntaje(intentos)
        print(resultado)
        if resultado == "¡Correcto!":
            print(f"¡Felicidades! Adivinaste el número en {intentos} intento(s) y obtuviste un puntaje de {puntajes}")
            break
        elif resultado=="Perdiste :(":
            print(f"Perdiste :(, sobrepasaste los 10 intentos.")
            break  
        else:
            print(f"Intentos restantes = {7-intentos}")
if __name__ == "__main__":
    print("¡Bienvenido al juego del número mágico!, Adivina el numero del 1-100 en 6 intentos.")
    jugar_juego()
