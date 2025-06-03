# 📚 BookBuddy – Sistema de Recomendación de Libros

Este proyecto es una aplicación de recomendación de libros desarrollada con **Python**, **Flask** y **scikit-learn**. Permite ingresar un `book_id` y obtener libros similares en base a ratings colaborativos, mostrando título, autor, puntuación y portada.

---

## 🚀 Funcionalidades

- ✅ Recomendaciones basadas en filtrado colaborativo (KNN item-item)
- ✅ Visualización de portadas, autores y tags principales
- ✅ Aplicación web con Flask
- ✅ Modelo entrenado una sola vez y cargado con `pickle`

---

## 📄 Archivos de entrada
Voy a utilizar los archivos que se encuentran en el siguiente github : https://github.com/zygmuntz/goodbooks-10k

## 📁 Estructura del proyecto

📄 app.py – App Flask  
📄 modelo_recomendador.py – Lógica del modelo  
📄 entrenar_modelo.py – Reentrena el modelo desde cero creando matriz e utilidad y kkn en formato .pkl 
📁 templates/ – HTML de la app  
📁 static/ – (opcional) CSS e imágenes  

## 📊 ¿Cómo funciona?
Se utiliza filtrado colaborativo item-item con KNN (similaridad del coseno) para encontrar libros que fueron puntuados de manera similar por los usuarios. Los resultados se enriquecen con información como:

⭐ Rating promedio real

🏷️ Tags más usados (géneros, temas)

🖼️ Imagen de portada

## 🤓 Autor
Felipe Carballo – Científico de Datos / Ingeniero de Datos

[LinkedIn](https://www.linkedin.com/in/felipe-carballo/)
