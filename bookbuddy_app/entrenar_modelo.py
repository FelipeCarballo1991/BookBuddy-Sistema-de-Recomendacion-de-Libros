import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import pickle

# Cargar datasets necesarios para mostrar info
books = pd.read_csv(r"..\Input\books.csv")
ratings = pd.read_csv(r"..\Input\ratings.csv") # Usuarios que calificaron libros

# Crear matriz de utilidad
matriz_utilidad = ratings.pivot_table(index='book_id', columns='user_id', values='rating')
matriz_utilidad.fillna(0, inplace=True)

# Convertir a matriz dispersa
matriz_sparse = csr_matrix(matriz_utilidad.values)

# Entrenar el modelo KNN
modelo_knn = NearestNeighbors(metric='cosine', algorithm='brute')
modelo_knn.fit(matriz_sparse)

# Guardar objetos
with open("modelo_knn.pkl", "wb") as f:
    pickle.dump(modelo_knn, f)

with open("matriz_utilidad.pkl", "wb") as f:
    pickle.dump(matriz_utilidad, f)

print("✅ Modelo entrenado y guardado.")
