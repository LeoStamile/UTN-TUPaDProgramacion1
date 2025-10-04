# 1- Crear una función llamada imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# 2- Crear una función llamada saludar_usuario(nombre)
def saludar_usuario(nombre):
    print("Hola " + nombre + "!")

nombre = input("Cual es tu nombre?: ")
saludar_usuario(nombre)


# 3- Crear una función llamada informacion_personal(nombre, apellido,edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy " + nombre + " " + apellido + ", tengo " + edad + " años y vivo en " + residencia + ".")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# 4- Crear dos funciones: calcular_area_circulo(radio)
def calcular_area_circulo(radio):
    area = 3.14 * radio * radio
    print("Area:", area)

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print("Perimetro:", perimetro)

radio = float(input("Ingresa el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


# 5- Crear una función llamada segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print("Horas:", horas)

segundos = int(input("Ingresa la cantidad de segundos: "))
segundos_a_horas(segundos)


# 6 - Crear una función llamada tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    print("Tabla del", numero)
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("Ingresa un numero: "))
tabla_multiplicar(numero)


# 7- Crear una función llamada operaciones_basicas(a, b)
def operaciones_basicas(a, b):
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicacion:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("No se puede dividir por cero.")

a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
operaciones_basicas(a, b)


# 8- Crear una función llamada calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    print("Tu IMC es:", round(imc, 2))

peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
calcular_imc(peso, altura)


# 9- Crear una función llamada celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("Temperatura en Fahrenheit:", fahrenheit)

celsius = float(input("Temperatura en Celsius: "))
celsius_a_fahrenheit(celsius)


# 10 - Crear una función llamada calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print("Promedio:", promedio)

a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
c = float(input("Tercer numero: "))
calcular_promedio(a, b, c)
