# Programa 1.5 
# Fecha: 2024/11/05
# Elaborado por: Jazmin Macias Sabas
letras = ["a","b","c","d","e"]
contador = 0 #inicializa variable 
for letra in letras:
    contador = contador +1 
print("La lista \"letras\" tiene",contador,"letras")
números = [100,200,300,400]
sumatoria = 0 # inicialización 
for número in números:
    sumatoria = sumatoria + número
print("La sumatoria es", sumatoria)
palabras = ["Hoy"," ","hace"," ","frío"]
mensaje = ""
for palabra in palabras:
    mensaje = mensaje + palabra
print(mensaje)
lista_anterior = ["Manzana","Piña","Uva"]
lista_nueva = []
print("La lista vacia", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es:", lista_nueva)
