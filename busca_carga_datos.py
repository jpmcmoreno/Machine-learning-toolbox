
import os
import pandas as pd

def busca_carga_datos(ruta_principal, nombre, nombre_hoja=None, columnas = None):
    # Recorre todas las subcarpetas y archivos dentro de la ruta principal
    for dirpath, dirnames, filenames in os.walk(ruta_principal):
        for archivo in filenames:
            if archivo.endswith('.xlsx') and nombre == archivo:
                # Construye la ruta completa al archivo
                ruta_completa = os.path.join(dirpath, archivo)
                try:
                    if nombre_hoja:
                        df = pd.read_excel(ruta_completa, sheet_name=nombre_hoja, usecols=columnas)
                    else:
                        df = pd.read_excel(ruta_completa)
                    return df
                except pd.errors.EmptyDataError:
                    print(f"El archivo {archivo} está vacío.")
                    return None

    print(f"No se encontró ningún archivo con el nombre '{nombre}' en las subcarpetas.")
    return None
