# Programa 1.11 Programa que se repite hasta que ingrese la palabra salir 
# Fecha: 2024/11/08
# Elaborado por: Jazmin Macias Sabas

# Iniciación de variables 
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o salir para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a minúscula
    print("Usted ingreso:", palabra)
print("Fin del programa")
