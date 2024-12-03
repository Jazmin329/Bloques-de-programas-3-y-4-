Explicación
```
Ejercicio 9 Igualdad en listas 
# Programa 9 Compare puntos con todas las demás listas 
# Fecha: 2024/10/31
# Elaborado por: Jazmin Macias Sabas
puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]
print(puntos==puntos_2) #True
print(puntos==ordenados) #False
print(puntos==puntos_texto) #False
print(puntos!=puntos_2) #False
print(puntos!=ordenados) #True 
print(puntos!=puntos_texto) #True 
```
1. Se crean cuatro listas diferentes: "puntos", "puntos\_2", "ordenados", y "puntos\_texto". Las listas "puntos" y "puntos\_2" tienen el mismo contenido pero diferente en la variable en la que se almacena. La lista "ordenados" tiene los mismos números pero en orden ascendente. La lista "puntos\_texto" contiene las cadenas de texto de los números presentes en las otras listas:
puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]

2. Se imprime la comparación de igualdad entre las listas "puntos" y "puntos\_2" usando el operador ==:
print(puntos==puntos_2) #True
El resultado será True ya que las listas son idénticas en contenido y orden.

3. Se imprime la comparación de igualdad entre las listas "puntos" y "ordenados" usando el operador ==:
print(puntos==ordenados) #False
El resultado será False ya que, aunque tienen los mismos elementos, las listas tienen diferente orden.

4. Se imprime la comparación de igualdad entre las listas "puntos" y "puntos\_texto" usando el operador ==:
print(puntos==puntos_texto) #False
El resultado será False ya que las listas tienen contenido diferente: una contiene enteros y la otra contiene strings (cadenas de texto).

5. Se imprime la comparación de desigualdad entre las listas "puntos" y "puntos\_2" usando el operador !=:
print(puntos!=puntos_2) #False
El resultado será False ya que las listas son idénticas en contenido y orden.

6. Se imprime la comparación de desigualdad entre las listas "puntos" y "ordenados" usando el operador !=:
print(puntos!=ordenados) #True
El resultado será True ya que las listas tienen diferente orden.

7. Se imprime la comparación de desigualdad entre las listas "puntos" y "puntos\_texto" usando el operador !=:
print(puntos!=puntos_texto) #True
El resultado será True ya que las listas tienen contenido diferente: una contiene enteros y la otra contiene strings (cadenas de texto).

Este programa muestra cómo evaluar la igualdad y desigualdad entre listas en Python y cómo se toman en cuenta el contenido, el orden y los tipos de datos de los elementos en la comparación.
