import random

print("¡Bienvenida al juego de Adivina el Número! 🎯")
numero_secreto = random.randint(1, 100)
intentos = 0
adivinaste = False

while not adivinaste:
    intento = input("Adiviná un número entre 1 y 100: ")

    if not intento.isdigit():
        print("Por favor, ingresá solo números.")
        continue

    intento = int(intento)
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo ⬇️")
    elif intento > numero_secreto:
        print("Demasiado alto ⬆️")
    else:
        adivinaste = True
        print(f"🎉 ¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intentos.")


