from fuzzywuzzy import process

# Definir un diccionario con las categorías correctas para cada variable
categorias_correctas_por_variable = {
    'Estado Civil': ['Soltero', 'Casado', 'Viudo', 'Divorciado'],
    'Estrato': [0, 1, 2, 3, 4, 5, 6]
}

# Función para corregir las categorías en una variable dada
def corregir_categorias(variable, categorias_correctas, datos_unificados):
    mapeo_categorias = {}
    categorias_correctas_str = [str(categoria) for categoria in categorias_correctas]
    for categoria in datos_unificados[variable].unique():
        categoria_str = str(categoria)
        # Encontrar la mejor coincidencia en la lista de categorías correctas
        mejor_coincidencia = process.extractOne(categoria_str, categorias_correctas_str)
        # Obtener la categoría correcta y su puntaje de coincidencia
        categoria_correcta, puntaje = mejor_coincidencia
        # Establecer la categoría correcta para la categoría original si el puntaje es lo suficientemente alto
        if puntaje >= 80:  # puedes ajustar este umbral según tu criterio
            mapeo_categorias[categoria] = int(categoria_correcta) if categoria_correcta.isdigit() else categoria_correcta
    # Reemplazar las categorías en el DataFrame
    datos_unificados[variable] = datos_unificados[variable].map(mapeo_categorias).fillna(datos_unificados[variable])
    return datos_unificados

# Aplicar la corrección de categorías a cada variable del DataFrame
for variable, categorias_correctas in categorias_correctas_por_variable.items():
    datos_unificados = corregir_categorias(variable, categorias_correctas, datos_unificados)

print(datos_unificados)
