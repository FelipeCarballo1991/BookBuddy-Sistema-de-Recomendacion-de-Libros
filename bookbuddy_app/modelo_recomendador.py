import pickle
import pandas as pd

# Cargar datasets necesarios para mostrar info
books = pd.read_csv(r"..\Input\books.csv")
books_tags = pd.read_csv(r"..\Input\book_tags.csv")
ratings = pd.read_csv(r"..\Input\ratings.csv") # Usuarios que calificaron libros
tags = pd.read_csv(r"..\Input\tags.csv")
to_read = pd.read_csv(r"..\Input\to_read.csv") # Usuarios que marcaron libros como "quiero leer" (DESCARTADO PARA EL MODELO)

book_tags = books_tags.merge(tags, on='tag_id')

# Cargar modelo y matriz ya entrenados
with open("modelo_knn.pkl", "rb") as f:
    modelo_knn = pickle.load(f)

with open("matriz_utilidad.pkl", "rb") as f:
    matriz_utilidad = pickle.load(f)

def mostrar_tags_de_libro(libro_id, top_n=3):
    try:
        goodreads_id = books[books["book_id"] == libro_id]["goodreads_book_id"].values[0]
        tags_libro = book_tags[book_tags["goodreads_book_id"] == goodreads_id]
        top_tags = tags_libro.sort_values("count", ascending=False)["tag_name"].head(top_n).tolist()
        return ", ".join(top_tags) if top_tags else "Sin tags"
    except:
        return "Sin tags"

def obtener_recomendaciones(book_id, n=5):
    resultados = []

    try:
        idx = list(matriz_utilidad.index).index(book_id)
        distancias, indices = modelo_knn.kneighbors([matriz_utilidad.iloc[idx]], n_neighbors=n+1)

        for i in range(1, len(indices.flatten())):
            libro_id = matriz_utilidad.index[indices.flatten()[i]]
            fila = books[books['book_id'] == libro_id].iloc[0]
            promedio = ratings[ratings['book_id'] == libro_id]['rating'].mean()
            tags = mostrar_tags_de_libro(libro_id)

            resultados.append({
                'titulo': fila['title'],
                'autor': fila['authors'],
                'rating': round(promedio, 2),
                'tags': tags,
                'imagen': fila['image_url']
            })

    except Exception as e:
        resultados.append({'error': f"No se encontró el libro: {book_id} ({str(e)})"})

    return resultados
