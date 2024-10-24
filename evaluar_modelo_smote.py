
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
from imblearn.over_sampling import SMOTE

def evaluar_modelo(nombre,dataframe, modelo):

    smote = SMOTE(random_state=42)

    # Dividir el dataframe en características y etiqueta
    X = dataframe.iloc[:, :-1]  # Todas las columnas menos la última
    y = dataframe.iloc[:, -1]   # La última columna

    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train, y_train = smote.fit_resample(X_train, y_train)

    # Registrar el tiempo de inicio
    start_time = time.time()

    # Entrenar el modelo
    modelo.fit(X_train, y_train)

    # Registrar el tiempo de finalización y calcular la duración
    tiempo_ejecucion = time.time() - start_time

    # Predecir con el conjunto de prueba
    y_pred = modelo.predict(X_test)

    # Calcular la efectividad del modelo
    exactitud = accuracy_score(y_test, y_pred)
    f1Score = f1_score(y_test, y_pred, average='weighted')
    presicion = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    Roc_auc = roc_auc_score(y_test, y_pred)

    # Imprimir los resultados
    print('--'*10,nombre,'--'*10)
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} segundos")
    print(f"exactitud del modelo: {exactitud:.2f}")
    print(f"F1 Score: {f1Score:.2}")
    print(f"Presición: {presicion:.2}")
    print(f"Recall: {recall:.2}")
    print(f"Roc Auc Score: {Roc_auc:.2}")

# Ejemplo de uso de la función
# Suponiendo que 'df' es tu DataFrame y 'modelo' es tu modelo de clasificación
# evaluar_modelo(df, modelo)
