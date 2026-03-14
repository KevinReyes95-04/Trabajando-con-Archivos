#--------------------------------------------------
# Ejercicio 2: Analizando datos estructurados (Diccionarios y Listas)
#---------------------------------------------------

import csv

# 1. Crear una función que lea el archivo CSV generado en el ejercicio anterior
#    y lo convierta en una lista de diccionarios.
def leer_inventario_csv(nombre_archivo):
    """
    Lee un archivo CSV con el inventario de árboles y lo convierte
    en una lista de diccionarios.
    Cada diccionario representa un árbol con las claves:
    'especie', 'latitud' y 'longitud'.
    """
    arboles = []

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)

            for fila in lector_csv:
                try:
                    arbol = {
                        "especie": fila["Especie"],
                        "latitud": float(fila["Latitud"]),
                        "longitud": float(fila["Longitud"])
                    }
                    arboles.append(arbol)

                except ValueError as e:
                    print(f"Error al convertir coordenadas para la especie '{fila['Especie']}': {e}")
                except KeyError as e:
                    print(f"Error: falta la columna {e} en el archivo CSV.")

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{nombre_archivo}'.")

    return arboles


# 2. Almacenar todos esos diccionarios en una lista principal
arboles_inventario = leer_inventario_csv("arboles_limpios.csv")
print(f"Se cargaron {len(arboles_inventario)} árboles desde el archivo CSV.")

# 3. Recorrer esa lista final y calcular la latitud promedio
if arboles_inventario:
    latitudes = [arbol["latitud"] for arbol in arboles_inventario]
    latitud_promedio = sum(latitudes) / len(latitudes)
    print(f"La latitud promedio de los árboles válidos es: {latitud_promedio:.4f}")
else:
    print("No se encontraron árboles válidos para calcular la latitud promedio.")
