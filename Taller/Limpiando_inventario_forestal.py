#--------------------------------------------------
# Ejercicio 1: Limpiando inventario Forestal
#---------------------------------------------------

# 1. Definimos los datos usando un string de múltiples líneas
arboles_crudos_txt = """Especie,Latitud,Longitud
Roble,4.6097,-74.0817
Pino,4.6XYZ,-74.0900
Cedro,4.6150,-74.0850
Eucalipto,NULA,-74.0700
Nogal,4.6200,-74.0650"""

# 2. Función que lee línea por línea, valida los datos y guarda
#    únicamente los registros correctos en un archivo CSV
def limpiar_inventario(arboles_crudos_txt):
    """
    Lee datos de un inventario forestal en formato de texto.
    Retorna una lista de diccionarios con la información limpia.
    Además, guarda las líneas válidas en un archivo llamado
    'arboles_limpios.csv'.
    """
    arboles_limpios = []

    # Dividimos el string en líneas
    lineas = arboles_crudos_txt.splitlines()

    # Abrimos el archivo de salida y escribimos el encabezado
    with open("arboles_limpios.csv", "w", encoding="utf-8") as archivo_salida:
        archivo_salida.write("Especie,Latitud,Longitud\n")

        # Omitimos el encabezado
        for num_linea, linea in enumerate(lineas[1:], start=2):
            partes = linea.strip().split(",")

            # Tomamos la especie desde el inicio para poder reportarla si hay error
            especie_nombre = partes[0] if len(partes) > 0 else "Desconocida"

            try:
                if len(partes) != 3:
                    raise ValueError("La línea no tiene exactamente 3 campos")

                latitud = float(partes[1])
                longitud = float(partes[2])

                # Guardamos en la lista
                arboles_limpios.append({
                    "especie": especie_nombre,
                    "latitud": latitud,
                    "longitud": longitud
                })

                # Si la línea es válida, la escribimos en el archivo CSV
                archivo_salida.write(f"{especie_nombre},{latitud},{longitud}\n")

            except ValueError:
                # Si falla, omitimos la línea y mostramos advertencia con la especie
                print(f"Advertencia: La especie '{especie_nombre}' tiene un error y no fue procesada.")
            else:
                print(f"Línea {num_linea} procesada correctamente: {linea.strip()}")
            finally:
                print(f"Finalizando procesamiento de la línea {num_linea}.\n")

    return arboles_limpios

# 3. Llamamos la función
resultado = limpiar_inventario(arboles_crudos_txt)

# 4. Mostramos la lista final de registros limpios
print("Inventario limpio:")
print(resultado)