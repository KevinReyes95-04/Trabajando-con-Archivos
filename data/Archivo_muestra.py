# #| eval: false

# 1. Definimos los datos usando un string de múltiples líneas (triple comilla).
# Orden: Latitud, Longitud (Bogotá, Medellín, Cali, Barranquilla, Cartagena)
datos_muestra = """4.7110,-74.0721
6.2442,-75.5812
3.4516,-76.5320
10.9685,-74.7813
10.3910,-75.4794
7.1254,-73.1198
7.8891,-72.4967
4.4389,-75.2322
4.1420,-73.6266
5.0689,-75.5174
5.5353,-73.3678
4.8143,-75.6946
2.4448,-76.6147
2.9273,-75.2819
11.2408,-74.1990
8.7479,-75.8814
9.3047,-75.3978
7.9069,-72.5053
11.5444,-72.9072
1.2136,-77.2811
2.9273,-75.2819
5.0703,-75.5138
3.5430,-73.7580
1.6144,-75.6062
0.8280,-77.6319
3.8854,-77.0708
5.6947,-76.6611
7.3756,-72.6482
8.0926,-76.7282
8.5847,-75.9749
4.5339,-75.6811
6.1738,-67.4924"""

# 2. Definimos la variable 'f_txt' que almacena la ruta y nombre del archivo
f_txt = "coordenadas_colombia_p.txt"

# 3. Manejo de excepciones completo para la creación del archivo
try:
    # 'w' indica modo escritura (write). 'with' cierra el archivo automáticamente.
    # Asignamos el archivo abierto a la variable 'con' (conexión)
    with open(f_txt, "w", encoding="utf-8") as con:
        # Escribimos los datos en la conexión. 
        # Python retorna la cantidad de caracteres escritos.
        caracteres_escritos = con.write(datos_muestra)
        #
        # Imprime automáticamente caracteres_escritos en modo interactivo
        #con.write(datos_muestra)
        #
        # Evita que se imprima el número de caracteres_escritos usando '_'
        #_ = con.write(datos_muestra)
except Exception as e:
    # Bloque que se ejecuta solo si ocurre un error en la apertura/escritura
    print(f"Ocurrió un error al crear el archivo: {e}")
else:
    # Bloque que se ejecuta solo si el 'try' fue exitoso (sin errores)
    print(f"El archivo '{f_txt}' ha sido creado exitosamente. Se guardaron {caracteres_escritos} caracteres.")
finally:
    # Bloque que se ejecuta SIEMPRE, haya ocurrido un error o no, ideal para limpieza
    print("Done.")