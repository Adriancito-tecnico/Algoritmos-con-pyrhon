import time
while True:
    texto = input("Escribe 'contar' para contar palabras o '!salir' para terminar: ").strip().lower()
    if texto == '!salir':
        print("Saliendo del programa...")
        time.sleep(2)
        break
    palabras = texto.split()
    numero_de_palabras = len(palabras)
    print(f"Número de palabras: {numero_de_palabras}")