# 1-Crear una lista con las notas de 10 estudiantes.
notas = [6, 9, 6, 8, 8, 7, 5, 10, 9, 7]

print("Notas de los estudiantes:")
for i in range(10):
    print(notas[i])

suma = 0
for i in range(10):
    suma += notas[i]

promedio = suma / 10
print("Promedio de notas:", promedio)

notamaxima = notas[0]
notaminima = notas[0]

for i in range(1, 10):
    if notas[i] > notamaxima:
        notamaxima = notas[i]
    if notas[i] < notaminima:
        notaminima = notas[i]

print("Nota más alta:", notamaxima)
print("Nota más baja:", notaminima)

# 2- Pedir al usuario que cargue 5 productos en una lista

productos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

productosordenados = sorted(productos)
print("Lista de productos ordenados alfabéticamente: ")
print(productosordenados)

productoaeliminar = input("Ingrese el producto que deseas eliminar: ")

if productoaeliminar in productos:
    productos.remove(productoaeliminar)
    print(f"has eliminado el Producto '{productoaeliminar}'")
else:
    print(f"El producto '{productoaeliminar}' no se encontró en la lista.")

print("Lista actualizada:")
print(productos)

# 3 - Generar una lista con 15 números enteros al azar entre 1 y 100.

import random

numeros = [random.randint(1, 100) for i in range(15)]

par = []
impar = []

for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

cantidadpares = 0
for elemento in par:
    cantidadpares += 1

cantidadimpares = 0
for elemento in impar:
    cantidadimpares += 1

print("Números generados:")
for n in numeros:
    print(n)

print("Lista de pares:")
for p in par:
    print(p)

print("Lista de impares:")
for i in impar:
    print(i)

print("Cantidad de pares:", cantidadpares)
print("Cantidad de impares:", cantidadimpares)

# 4- Dada una lista con valores repetidos: Crear una nueva lista sin elementos repetidos y mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sinrepetir = []

for elemento in datos:
    if elemento not in sinrepetir:
        sinrepetir.append(elemento)

print("Lista de numeros sin repetir:")
for numero in sinrepetir:
    print(numero)

# 5 - Crear una lista con los nombres de 8 estudiantes presentes en clase.

estudiantes = ["Leonardo", "Soledad", "Walter", "Juan", "Santiago", "Carlos", "Valeria", "Susana"]

print("lista de estudiantes: ")

for nombre in estudiantes:
    print(nombre)

pregunta = input("¿Querés agregar o eliminar un estudiante? (escribí 'agregar' o 'eliminar'): ")

if pregunta == "agregar":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif pregunta == "eliminar":
    nombre = input("Nombre del estudiante que querés eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
    else:
        print("Ese nombre no está en la lista.")

print("Lista actualizada: ")
for nombre in estudiantes:
    print(nombre)

# 6 - Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero)

numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo = numeros[-1]

for i in range(6, 0, -1):
    numeros[i] = numeros[i - 1]

numeros[0] = ultimo

for n in numeros:
    print(n)

# 7 - Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [[13, 19], [14, 20], [10, 18], [9, 20], [11, 17], [12, 19], [15, 20]]

sumamin = 0
sumamax = 0

for temp in temperaturas:
    sumamin += temp[0]
    sumamax += temp[1]

prommin = sumamin / 7
prommax = sumamax / 7

mayoramplitudtermica = 0
diamayoramplitud = ""

for i in range(7):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayoramplitudtermica:
        mayoramplitudtermica = amplitud
        diamayoramplitud = dias[i]

print("Promedio temperatura mínima:", prommin)
print("Promedio temperatura máxima:", prommax)
print("Mayor amplitud térmica:", mayoramplitudtermica)
print("Día con mayor amplitud térmica:", diamayoramplitud)

# 8 - Crear una matriz con las notas de 5 estudiantes en 3 materias.

notas = [
    [7, 8, 9],
    [6, 7, 8],
    [8, 9, 10],
    [5, 6, 7],
    [9, 9, 10]
]

materias = ["Materia1", "Materia2", "Materia3"]

for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    promedio = suma / 3
    print(f"Promedio Estudiante{i+1}: {promedio}")

print()

for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print(f"Promedio {materias[j]}: {promedio}")

# 9 - Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).

tablero = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

def mostrar_tablero(tab):
    for fila in tab:
        print(" ".join(fila))
    print()

mostrar_tablero(tablero)

jugadores = ["X", "O"]
turno = 0

for i in range(9):
    jugador = jugadores[turno % 2]
    print(f"Turno jugador {jugador}")
    
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        mostrar_tablero(tablero)
        turno += 1
    else:
        print("Casilla ocupada, intente de nuevo.")

# 10 - Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7

productos = ["Harina", "Detergente", "Leche", "Huevos"]
ventas = [
    [15, 5, 5, 7, 6, 12, 4],
    [8, 10, 4, 1, 5, 15, 3],
    [10, 8, 7, 6, 18, 4, 3],
    [2, 6, 5, 20, 7, 18, 6]
]

totalporproducto = []
for i in range(4):
    suma = 0
    for j in range(7):
        suma += ventas[i][j]
    totalporproducto.append(suma)

for i in range(4):
    print(f"Total vendido de {productos[i]}: {totalporproducto[i]}")

ventaspordia = []
for j in range(7):
    sumadia = 0
    for i in range(4):
        sumadia += ventas[i][j]
    ventaspordia.append(sumadia)

maxventas = ventaspordia[0]
diamaxventas = 0
for j in range(1,7):
    if ventaspordia[j] > maxventas:
        maxventas = ventaspordia[j]
        diamaxventas = j

diasdesemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(f"Día con mayores ventas totales: {diasdesemana[diamaxventas]} con {maxventas} ventas.")

maxventasproducto = totalporproducto[0]
productomasvendido = productos[0]
for i in range(1,4):
    if totalporproducto[i] > maxventasproducto:
        maxventasproducto = totalporproducto[i]
        productomasvendido = productos[i]

print(f"Producto más vendido en la semana: {productomasvendido} con {maxventasproducto} ventas.")

