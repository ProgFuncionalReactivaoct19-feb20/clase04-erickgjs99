"""
    autor: @erickgjs99
    file: ejercicio2.py
    
"""
lista = [(100, 2), (20, 4), (30,1)]
lista2 = ["b", "a", "c"]
#funcion para ordenar el segundo elemento de menor a mayor
#lista_n = sorted(lista, key = lambda x: x[1])
#funcion para ordenar la lista tipo cadena
#lista_p = sorted(lista2)
#funcion para juntar las dos listas
#listaF = zip(lista_p, lista_n)
#impresion de los resultados
print(list(zip(sorted(lista2), sorted(lista, key = lambda x: x[1] ))))