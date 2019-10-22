"""
    autor: @erickgjs99
    file: ejercicio5.py
    
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Angel", "Jose", "Ana"]
#para sacar el promedio de la lista
prom = map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA)
#impresion de las resultados
lista_f = (list(zip(prom, nombres)))
print(lista_f)
print(max(lista_f))
#para dar vuelta a la lita e imprimirla
lista_f.reverse()
print(lista_f)