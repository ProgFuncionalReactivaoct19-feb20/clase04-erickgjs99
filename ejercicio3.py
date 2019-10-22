"""
    autor: @erickgjs99
    file: ejercicio3.py
    
"""
lista = [(100, 2), (20, 4), (30,1)]
lista2 = ["b", "a", "c"]

#lista para convertir la lista a mayusculas y que este alreves la lista
list_p = reversed(sorted(map(lambda x: x.upper(), lista2)))

#impresion de los resultados
print(list(zip(sorted(lista, key = lambda x: x[0]), list_p)))