import numpy as np
# Santiago pacheco NC 0113
# Ejemplos de numpy Numerical python
print("-- Espaciis Linealmente en array -- 0113")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- matriz Linealmente en 2D array -- 0113")
matrix=np.eye(3)
print(matrix)
print("-- Generar numeros al azar(Alateorios) en 2D array -- 0113")
numale=np.random.random((3,4)) # genera 12 numeros alateorios
print(numale)
print(" generar 9 numeros alateorios entre 0 y 1")
numale=np.random.random((3,3)) # genera 12 numeros alateorios
print(numale)
# como generar 9 numeros alateorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros alateorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)

print("Santiago Pacheco NC 0113")