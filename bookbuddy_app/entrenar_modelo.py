import os
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import pickle

# 🚮 Paso 1: Eliminar archivos .pkl si existen
for archivo in ["modelo_knn.pkl", "matriz_utilidad.pkl"]:
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"🗑️ {archivo} eliminado.")

# 📥 Paso 2: Cargar datasets
print("📊 Cargando datos...")
books = pd.read_csv(r"..\Input\books.csv")
ratings = pd.read_csv(r"..\Input\ratings.csv") # Usuarios que calificaron libros

# 🧱 Paso 3: Crear matriz de utilidad
print("🔧 Construyendo matriz de utilidad...")
matriz_utilidad = ratings.pivot_table(index='book_id', columns='user_id', values='rating')
matriz_utilidad.fillna(0, inplace=True)

# 💡 Paso 4: Convertir a formato disperso
matriz_sparse = csr_matrix(matriz_utilidad.values)

# 🤖 Paso 5: Entrenar modelo KNN
print("🚀 Entrenando modelo KNN...")
modelo_knn = NearestNeighbors(metric='cosine', algorithm='brute')
modelo_knn.fit(matriz_sparse)

# 💾 Paso 6: Guardar objetos entrenados
with open("modelo_knn.pkl", "wb") as f:
    pickle.dump(modelo_knn, f)

with open("matriz_utilidad.pkl", "wb") as f:
    pickle.dump(matriz_utilidad, f)

print("✅ Modelo reentrenado y guardado.")
