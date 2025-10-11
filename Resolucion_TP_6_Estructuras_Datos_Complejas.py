# Práctico 6: Estructuras de datos complejas

# 1 - Diccionario precios_frutas y agregar frutas nuevas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario con frutas agregadas:", precios_frutas)

# 2 - Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print("Diccionario con precios actualizados:", precios_frutas)

# 3 - Lista con frutas (solo claves del diccionario)

solo_frutas = list(precios_frutas.keys())
print('Solo frutas (claves):', solo_frutas)

# 4 - Escribí un programa que permita almacenar y consultar números telefónicos

agenda = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero telefonico: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre para consultar el numero: ")

if consulta in agenda:
    print("Numero de", consulta, ":", agenda[consulta])
else:
    print("El contacto no existe.")


# 5 - Frase del usuario: palabras únicas y recuento

frase = input("Ingresa una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

print("Palabras unicas:", palabras_unicas)

frecuencias = {}
for palabra in palabras_unicas:
    frecuencias[palabra] = palabras.count(palabra)

print("Cantidad de veces que aparece cada palabra:", frecuencias)

# 6 - Promedio de 3 alumnos
alumnos = {}
for i in range(3):
    nombre = input('Nombre del alumno: ')
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f'Nota {j+1} de {nombre}: '))
                break
            except ValueError:
                print('Valor invalido. Intenta de nuevo.')
        notas.append(nota)
    alumnos[nombre] = tuple(notas)  # tupla de 3 notas

print('Promedio de alumnos:')
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(alumno, '-> Promedio:', promedio)

# 7 - Sets de estudiantes que aprobaron parciales
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

print("Aprobados en ambos:", parcial1 & parcial2)
print("Solo uno de los dos:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)

# 8 - Diccionario de stock de productos
stock = {"Pan": 10, "Leche": 5}

producto = input("Producto para consultar o modificar stock: ")

if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = int(input("Cuantos queres agregar? "))
    stock[producto] += agregar
else:
    nuevo = int(input("Producto nuevo. Cuantos queres agregar? "))
    stock[producto] = nuevo

print("Stock actualizado:", stock)

# 9 - Agenda con tuplas como clave
agenda = {
    ("Lunes", "10:00"): "Reunion",
    ("Martes", "15:00"): "Clase de ingles"
}

dia = input("Dia a consultar: ")
hora = input("Hora a consultar: ")

clave = (dia, hora)

if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad.")

# 10 - Invertir diccionario de países y capitales
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais in original:
    capital = original[pais]
    invertido[capital] = pais

print("Diccionario invertido:", invertido)
