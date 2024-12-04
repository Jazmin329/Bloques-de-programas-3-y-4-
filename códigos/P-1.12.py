# Programa 1.12 
# Fecha: 2024/11/08
# Elaborado por: Jazmin Macias Sabas

# Inicialización de variables
palabra = ""
while True:
    palabra = input("ingresa una palabra o salir para terminar: ")
    palabra = palabra.lower() # Convertir la palabra a minúsculas
    print("Usted ingreso: ", palabra)
    if palabra == "salir":
        break

print("Fin del programa \U0001F601 \n\n") # Imprime un emoji feliz 
print("¡Hasta luego! \U0001F44B \n") # Imprime un emoji de saludo
