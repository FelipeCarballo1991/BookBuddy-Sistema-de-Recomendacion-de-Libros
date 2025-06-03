from flask import Flask, render_template, request
from modelo_recomendador import obtener_recomendaciones

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recomendaciones = []
    book_id_ingresado = None

    if request.method == 'POST':
        try:
            book_id_ingresado = int(request.form['book_id'])
            recomendaciones = obtener_recomendaciones(book_id_ingresado)
        except ValueError:
            recomendaciones = [{"error": "Por favor, ingresá un número válido como book_id."}]

    return render_template('index.html', recomendaciones=recomendaciones, book_id=book_id_ingresado)

if __name__ == '__main__':
    app.run(debug=True)
