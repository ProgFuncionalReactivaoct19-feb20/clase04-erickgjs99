"""
    autor: @erickgjs99
    file: ejercicio6.py
    
"""
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Angel", "Jose", "Ana"]
#elegir la posicion 
n_angel = [paraleloA[1]]
n_ana = [paraleloA[3]]

#promedios
prom_angel = map(lambda x: (x[0] + x[1] + x[2])/3, n_angel)
prom_ana = map(lambda x: (x[0] + x[1] + x[2])/3, n_ana)
#suma
sum_angel = map(lambda x: x[0] + x[1] + x[2] , n_angel)
sum_ana = map(lambda x: x[0] + x[1] + x[2] , n_ana)
#impresion de los resultados
lista_angel = list(zip(prom_angel, sum_angel, nombres[1]))
lista_ana = list(zip(prom_ana, sum_ana, nombres[3]))
lista_f = list(zip(lista_angel, lista_ana))
print(lista_f)