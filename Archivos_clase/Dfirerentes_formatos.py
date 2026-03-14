# #| eval: false

# 1. Creamos los datos CSV como una cadena de texto (str) con un encabezado
datos_csv = """Ciudad,Latitud,Longitud
Bogotá,4.7110,-74.0721
Medellín,6.2442,-75.5812
Cali,3.4516,-76.5320
Barranquilla,10.9685,-74.7813
Cartagena,10.3910,-75.4794"""

# Guardamos el nombre del archivo en una variable de texto (str)
f_csv = "ciudades_colombia_p.csv"

# Bloque try-except para crear el archivo CSV
try:
    with open(f_csv, "w", encoding="utf-8") as con_csv:
        _ = con_csv.write(datos_csv)
    print(f"Archivo CSV '{f_csv}' creado exitosamente.\n")
except Exception as e:
    print(f"Error al crear el archivo CSV: {e}\n")

    # 2. Definimos una función para leer y estructurar esos datos
def leer_coordenadas_ciudades(nombre_archivo):
    """
    Lee datos de coordenadas desde un archivo estilo CSV.
    Retorna una lista (list) de diccionarios (dict) con la información.
    """
    # Inicializamos una lista vacía (list) para almacenar nuestros registros
    ciudades = []

    try:
        # Abrimos conexión de lectura
        with open(nombre_archivo, "r", encoding="utf-8") as con_csv:
            # readlines() nos devuelve una lista (list) de textos (str)
            lineas = con_csv.readlines()

            # Omitimos el encabezado usando segmentación de listas (slicing): lineas[1:]
            # enumerate(..., 2) indica que el contador entero (int) inicia en 2
            for num_linea, linea in enumerate(lineas[1:], 2):
                try:
                    # Limpiamos y dividimos la línea de texto (str)
                    partes = linea.strip().split(",")
                    
                    # Verificamos que la lista 'partes' tenga 3 elementos
                    if len(partes) == 3:
                        ciudad_nombre = partes[0]          # str
                        latitud = float(partes[1])         # float
                        longitud = float(partes[2])        # float

                        # Creamos un diccionario (dict) y lo agregamos (append) a la lista
                        ciudades.append({
                            "nombre": ciudad_nombre,
                            "latitud": latitud,
                            "longitud": longitud
                        })

                except ValueError as e:
                    # Este try interno evita que una línea mala detenga todo el ciclo
                    print(f"Advertencia: No se pudo procesar la línea {num_linea}: {linea.strip()}")
                    continue

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return [] # Retornamos lista vacía en caso de error crítico
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

    return ciudades


# 3. Llamamos a la función y guardamos el resultado (lista de diccionarios)
lista_ciudades = leer_coordenadas_ciudades(f_csv)

print(f"Se cargaron exitosamente {len(lista_ciudades)} ciudades:")
for ciudad in lista_ciudades:
    print(f"- {ciudad['nombre']}: Latitud {ciudad['latitud']}, Longitud {ciudad['longitud']}")