texto = "Este es un ejemplo de texto para contar el número de palabras."

palabras = texto.split() 
total_palabras = len(palabras)

print ("Texto:", texto)
print(f"El texto contiene {total_palabras} palabras.")