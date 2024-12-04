# Programa 1.8
# Fecha: 2024/11/07
# Elaborado por: Jazmin Macias Sabas

# Ejemplo 1 
# Imprimir los numeros del 1 al 10 
i = 1 #Inicializacion de la variable de control 
while i <= 10: # Condicion de parada
    print(i)
    i += 1 # Equivalente a i = i + 1 
# Sintaxis:
# while <condicional>:
# <cuerpo del while>

# Ejemplo 2 
# Imprimir los numeros del 10 al 1 
i = 10
while i >= 1:
    print(i)
    i -= 1 

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 # Equivalente a i = i + 1 
print("Fin del programa")

# Ejemplo 2 - continue 
# Imprimir los números del 1 al 10, pero si el número es 5 evitarlo 
i = 1 
while i <= 10 :
    if i == 5:
        i += 1
        continue 
    print(i)
    i += 1
print("Fin del programa")
