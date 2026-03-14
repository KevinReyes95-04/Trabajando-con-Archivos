# #| eval: false

# 1. Definimos las variables para los archivos de entrada y salida
f_in = "coordenadas_colombia_p.txt"
f_out = "coordenadas_formato_p.txt"

try:
    # 2. Abrimos el archivo de entrada en modo lectura ('r' de read)
    with open(f_in, "r", encoding="utf-8") as con_in:
        # readlines() lee todas las líneas y devuelve una lista.
        # Cada elemento de la lista incluye el salto de línea (\n) al final.
        coordenadas = con_in.readlines()

    # 3. Abrimos el archivo de salida en modo escritura ('w' de write)
    with open(f_out, "w", encoding="utf-8") as con_out:
        # Recorremos cada línea de la lista que leímos
        for linea in coordenadas:
            # strip() elimina espacios en blanco y el salto de línea (\n) de los extremos.
            # split(",") divide la cadena de texto en dos partes usando la coma como separador.
            lat, lon = linea.strip().split(",")

            # Escribimos el dato formateado en nuestro archivo de salida.
            # Usamos \n para asegurar que cada coordenada quede en una línea nueva.
            _ = con_out.write(f"Latitud: {lat}, Longitud: {lon}\n")

    print(f"Las coordenadas han sido guardadas con nuevo formato en '{f_out}'.")

except FileNotFoundError:
    # Este bloque específico atrapa el error si el archivo de entrada no existe
    print(f"Error: El archivo '{f_in}' no fue encontrado.")
    print("Asegúrate de haber ejecutado el chunk de Python anterior para crearlo.")
except Exception as e:
    # Atrapa cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}")