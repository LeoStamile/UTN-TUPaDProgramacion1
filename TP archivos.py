# TP Archivos - practica

ARCHIVO = "productos.txt"

# 1) Crear archivo inicial con productos
def crear_archivo_inicial():
    archivo = open(ARCHIVO, "w")
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,950.0,15\n")
    archivo.write("Regla,300.0,20\n")
    archivo.close()
    return "Archivo creado con 3 productos."

# 2) Leer y mostrar productos con strip y split
def leer_y_formatear_productos():
    archivo = open(ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    salida = []
    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if linea != "":
            partes = linea.split(",")
            if len(partes) == 3:
                nombre = partes[0]
                precio = partes[1]
                cantidad = partes[2]
                salida.append("Producto: " + nombre + " | Precio: $" + precio + " | Cantidad: " + cantidad)
        i = i + 1

    if len(salida) == 0:
        return "No hay productos para mostrar."
    else:
        return "\n".join(salida)

# 3) Agregar producto desde teclado (append sin borrar contenido)

def pedir_y_agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacio. Ingresa de nuevo: ").strip()

    precio_txt = input("Precio (punto para decimales): ").strip()
    
    valido = False
    while valido == False:
        j = 0
        tiene_punto = False
        es_num = True
        if precio_txt == "":
            es_num = False
        while j < len(precio_txt) and es_num == True:
            c = precio_txt[j]
            if c == ".":
                if tiene_punto == False:
                    tiene_punto = True
                else:
                    es_num = False
            elif c < "0" or c > "9":
                es_num = False
            j = j + 1
        if es_num == True and precio_txt != ".":
            valido = True
        else:
            precio_txt = input("Precio invalido. Ingresa nuevamente: ").strip()

    cantidad_txt = input("Cantidad (entero): ").strip()
    valido = False
    while valido == False:
        es_entero = True
        if cantidad_txt == "":
            es_entero = False
        k = 0
        while k < len(cantidad_txt) and es_entero == True:
            c = cantidad_txt[k]
            if c < "0" or c > "9":
                es_entero = False
            k = k + 1
        if es_entero == True:
            valido = True
        else:
            cantidad_txt = input("Cantidad invalida. Ingrese nuevamente: ").strip()

    archivo = open(ARCHIVO, "a")
    archivo.write(nombre + "," + precio_txt + "," + cantidad_txt + "\n")
    archivo.close()
    return "Producto agregado."


# 4) Cargar productos en una lista de diccionarios
def cargar_en_lista_diccionarios():
    productos = []
    archivo = open(ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if linea != "":
            partes = linea.split(",")
            if len(partes) == 3:
                nombre = partes[0]
                precio = float(partes[1])
                cantidad = int(partes[2])
                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        i = i + 1
    return productos

# 5) Buscar producto por nombre

def buscar_por_nombre(productos, nombre_buscar):
    nombre_buscar = nombre_buscar.strip().lower()
    i = 0
    while i < len(productos):
        if productos[i]["nombre"].lower() == nombre_buscar:
            p = productos[i]
            return "Producto: " + p["nombre"] + " | Precio: $" + str(p["precio"]) + " | Cantidad: " + str(p["cantidad"])
        i = i + 1
    return "No existe un producto con ese nombre."

# 6) Guardar los productos actualizados
def guardar_desde_lista(productos):
    archivo = open(ARCHIVO, "w")
    i = 0
    while i < len(productos):
        p = productos[i]
        archivo.write(p["nombre"] + "," + str(p["precio"]) + "," + str(p["cantidad"]) + "\n")
        i = i + 1
    archivo.close()
    return "Archivo sobrescrito con la lista actual."
