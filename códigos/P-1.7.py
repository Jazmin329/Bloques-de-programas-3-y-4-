# Programa 1.7 Programa que clasifica las edades de una lista menores de 18, entre 18 y 65 y mayores de 65 el programa debe imprimir cuales edades hay en cada grupo 
# Fecha: 2024/11/07
# Elaborado por: Jazmin Macias Sabas
edades = [10,15,18,8, 36,25,67,89,95,43,26,10,65,55,81,90,64]
menores_18 = [] # Lista vacía para menores de 18 
adultos = []    # lista vacía para adultos entre 18 y 65 
mayores_65 = [] # Lista vacía para mayores de 65 

for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad >= 18 and edad <= 65:
        adultos.append(edad)
    else:
        mayores_65.append(edad)
        
print("\nLa lista de edades es: ",edades)
print("\nLa lista de menores es: ",menores_18)
print("\nLa lista de adultos es: ",adultos)
print("\nLa lista de adultos mayores es: ",mayores_65)
