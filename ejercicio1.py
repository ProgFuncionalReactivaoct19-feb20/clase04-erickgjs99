"""
    autor: @erickgjs99
    file: ejercicio1.py
    
"""
#Listas con las cuales trabajamos
listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]
#Funcion para ordenar listas
lista_1 = sorted(listaA)
#Funcion poner la lista en reversa
lista_2 = sorted(listaB, reverse = True)
#lista que junta ambas listas
listaF = list(zip(lista_1, lista_2))
print(list(listaF))
print(max(listaF))