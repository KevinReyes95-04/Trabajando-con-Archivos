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

# Almacenaremos todos los casos de prueba en una lista (list) de textos (str) llamada lineas_prueba
lineas_prueba = [
    "4.7110,-74.0721",      # Coordenadas válidas (Bogotá)
    "datos invalidos",      # Formato inválido (sin coma)
    "10.9685,-74.7813",     # Coordenadas válidas (Barranquilla)
    "10.9685,no_es_numero", # Longitud inválida (no se puede convertir a float)
    "solo_un_valor",        # Falta la coma (split falla al desempacar)
]

print("Probando el análisis de coordenadas:")

# Recorremos la lista. En cada iteración, 'linea' es un texto (str)
for linea in lineas_prueba:
    # 'coordenadas' recibirá una tupla (tuple) o un valor nulo (None)
    coordenadas = analizar_coordenadas(linea)
    
    if coordenadas:
        print(f"✓ Procesado exitosamente: {coordenadas}")
    else:
        print(f"✗ Falló al procesar: '{linea}'")