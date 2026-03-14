#| eval: false

import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Construcción segura de la ruta relativa
ruta_archivo = Path("data/vector/geojson/COL.geo.geojson").resolve()

try:
    # 2. Verificar si el archivo existe
    if not ruta_archivo.exists():
        raise FileNotFoundError(f"El archivo no existe: {ruta_archivo}")

    # 3. Leer el archivo espacial
    colombia_gdf = gpd.read_file(ruta_archivo)

    # 4. Crear figura
    fig, ax = plt.subplots(figsize=(6, 6))

    # 5. Graficar el mapa
    colombia_gdf.plot(
        ax=ax,
        color="lightgreen",
        edgecolor="black",
        linewidth=0.5
    )

    # 6. Estética del mapa
    ax.set_title("Límites de Colombia (Python)", fontsize=12)
    ax.set_axis_off()

    plt.show()

except FileNotFoundError as e:
    print(f"Archivo no encontrado: {e}")

except Exception as e:
    print("No se pudo generar el mapa.")
    print(f"Ruta intentada: {ruta_archivo}")
    print(f"Error: {e}")