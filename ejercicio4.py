"""
    autor: @erickgjs99
    file: ejercicio4.py
    
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Angel", "Jose", "Ana"]
#para sacar el promedio de la lista
prom = map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA)
#impresion de las resultados
print(list(zip(prom, nombres)))