# 1- Crea una función recursiva que calcule el factorial de un número

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales_hasta(n):
    i = 1
    while i <= n:
        print("factorial(", i, ") =", factorial(i))
        i = i + 1

num = int(input("Ingrese un numero entero: "))
mostrar_factoriales_hasta(num)

# 2- Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci_hasta(n):
    i = 0
    while i <= n:
        print("F(", i, ") =", fibonacci(i))
        i = i + 1

num = int(input("Ingrese la posicion hasta la que desea ver la serie de Fibonacci: "))
mostrar_serie_fibonacci_hasta(num)

# 3- Crea una función recursiva que calcule la potencia de un número base elevado a un exponente

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(base, "elevado a", exponente, "es:", resultado)

# 4- Crear una función recursiva en Python que reciba un número entero positivo en base decimal

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un numero entero positivo: "))
print("El numero", num, "en binario es:", decimal_a_binario(num))


# 5- Implementá una función recursiva llamada es_palindromo(palabra)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

texto = input("Ingrese una palabra: ")
if es_palindromo(texto):
    print("La palabra", texto, "es un palindromo.")
else:
    print("La palabra", texto, "no es un palindromo.")


# 6- Escribí una función recursiva en Python llamada suma_digitos(n)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un numero entero positivo: "))
print("La suma de los digitos de", num, "es:", suma_digitos(num))


# 7- Un niño está construyendo una pirámide con bloques

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en el nivel mas bajo: "))
print("Total de bloques necesarios:", contar_bloques(niveles))


# 8- Escribí una función recursiva llamada contar_digito(numero, digito)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        resto = numero // 10
        if ultimo == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return 0 + contar_digito(resto, digito)

numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese el digito que desea contar: "))

print("El digito", digito, "aparece", contar_digito(numero, digito), "veces en", numero)

