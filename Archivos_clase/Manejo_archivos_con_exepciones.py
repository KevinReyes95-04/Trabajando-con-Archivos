# #| eval: false


# #| eval: false

# Ejemplo de manejo de excepciones al analizar coordenadas
def analizar_coordenadas(linea):
    """
    Analiza una línea de texto y la convierte en coordenadas de latitud y longitud.

    Argumentos:
        linea (str): Una cadena de texto con las coordenadas en formato "lat,lon"

    Retorna:
        tuple: (latitud, longitud) como flotantes (floats), o None si el análisis falla
    """
    try:
        # split() divide la cadena y retorna una lista (list) de textos (str).
        # Desempacamos esa lista directamente en dos variables de texto: lat_str y lon_str
        lat_str, lon_str = linea.strip().split(",")
        
        # Convertimos las variables de texto (str) a números decimales (float)
        # Esto puede generar un ValueError si el texto no es un número válido
        lat = float(lat_str)
        lon = float(lon_str)
        
        # Retornamos los valores empaquetados en una tupla (tuple) de floats
        return lat, lon

    except ValueError as e:
        # Este bloque se ejecuta si no se puede convertir a float o si split() no devuelve 2 valores
        print(f"Error de formato: {e}. No se pudo procesar la línea (tipo str): '{linea.strip()}'")
        # Retornamos un tipo nulo (NoneType)
        return None

    except Exception as e:
        # Este bloque captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")
        return None

# Ejemplo de manejo robusto de archivos con excepciones
def procesar_archivo_espacial(f_in):
    """
    Procesa un archivo con coordenadas, manejando varios errores potenciales.
    Argumentos:
        f_in (str): La ruta del archivo a leer.
    """
    # Contadores enteros (int) para el resumen final
    procesados = 0
    errores = 0

    try:
        print(f"Iniciando el procesamiento del archivo: {f_in}")

        # Abrimos la conexión al archivo en modo lectura ('r')
        with open(f_in, "r", encoding="utf-8") as con_in:
            # enumerate() nos da un índice entero (int) y la línea de texto (str)
            # El '1' indica que queremos empezar a contar desde la línea 1
            for num_linea, linea in enumerate(con_in, 1):
                
                # Omitimos líneas vacías. strip() quita espacios, y 'not' evalúa si quedó vacío
                if not linea.strip():
                    continue

                # 'coordenadas' recibirá una tupla (tuple) o un nulo (None)
                coordenadas = analizar_coordenadas(linea)
                
                if coordenadas:
                    # Desempacamos la tupla en dos decimales (float)
                    lat, lon = coordenadas
                    # Usamos .4f para formatear los floats a 4 decimales en el texto
                    print(f"Línea {num_linea}: Coordenadas procesadas ({lat:.4f}, {lon:.4f})")
                    procesados += 1
                else:
                    print(f"Línea {num_linea}: Omitida debido a un error de formato")
                    errores += 1

    except FileNotFoundError:
        # Atrapa específicamente el error si el archivo (str) no existe
        print(f"Error: El archivo '{f_in}' no fue encontrado.")
        print("Por favor verifica la ruta y asegúrate de que el archivo exista.")
        return

    except PermissionError:
        # Atrapa el error si no tenemos derechos de lectura en el sistema operativo
        print(f"Error: Permiso denegado al intentar leer '{f_in}'.")
        print("Por favor verifica si tienes permisos de lectura para este archivo.")
        return

    except Exception as e:
        # Atrapa cualquier otro error genérico
        print(f"Ocurrió un error inesperado al procesar el archivo: {e}")
        return

    finally:
        # Este bloque SIEMPRE se ejecuta, independientemente de si hubo errores o retornos previos
        print(f"\n--- Resumen del Procesamiento ---")
        print(f"Procesadas con éxito: {procesados} coordenadas")
        print(f"Errores encontrados: {errores} líneas")
        print(f"Finalizó el procesamiento de '{f_in}'")

# Llamada de ejemplo usando nuestro archivo (tipo str)
procesar_archivo_espacial("coordenadas_colombia_p.txt")