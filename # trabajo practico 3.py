# trabajo practico 3

# 1- Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# 2-Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Por favor, ingresa la nota de 1 a 10: "))

if nota >= 6:
    print("Aprobado")
else:
    print("desaprobado")

# 3- Escribir un programa que permita ingresar solo números pares.

numero = int(input("Por favor, ingresa un numero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"Por favor, ingrese un número par.")

# 4-Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:niño/a, adolescente, adulto/a joven, adulto/a

edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12:
    print("Perteneces a la categoria: Niño/a.")
elif 12 <= edad < 18:
    print("Perteneces a la categoria: Adolescente.")
elif 18 <= edad < 30:
    print("Perteneces a la categoria: Adulto/a joven.")
else:
    print("Perteneces a la categoria: Adulto/a.")

# 5- Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14)

contraseña = input("Por favor, ingresa una contraseña entre 8 y 14 caracteres: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6- escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean, random
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Lista de números: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
if media > mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "No se puede determinar claramente el sesgo con los datos"

print(f"Tipo de sesgo: {sesgo}")

# 7- # Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto = input("Ingresa una frase o palabra: ")

if texto[-1] in "aeiouAEIOU":
    print (f"{texto}!")
else:
    print (texto)

# 8- Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee

nombre = input("Ingresa tu nombre por favor: ")
print ("ingresa la opcion que desees")
print ("1- Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO")
print ("2- Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print ("3- Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

numero = int(input("Por favor, ingresa un numero: "))

if numero == 1:
    print (nombre.upper())
elif numero == 2:
    print (nombre.lower())
elif numero == 3:
    print (nombre.title())

# 9 - Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Terremoto Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Terremoto Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Terremoto Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Terremoto Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Terremoto Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
     print("Terremoto Extremo (puede causar graves daños a gran escala).")

# 10 - Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

hemisferio = input("En que hemisferio te encuestras? (N/S): ")
mes = int(input("Que mes es?: "))
dia = int(input("Y que dia es?: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    norte = "Verano"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    norte = "Otoño"
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    sur = "verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    sur = "otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    sur = "invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    sur = "primavera"

if hemisferio == "N":
    estacion = norte
elif hemisferio == "S":
    estacion = sur
else:
    estacion = "Hemisferio no válido"

print("La estación del año es:", estacion)