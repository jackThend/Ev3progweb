from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para el formulario 1
@app.route('/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        # Recoger datos del formulario
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Determinar si está aprobado o reprobado
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

        # Enviar los resultados a la plantilla
        return render_template('resultado1.html', promedio=promedio, estado=estado)

    return render_template('form1.html')


# Ruta para el formulario 2
@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        # Recoger datos del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encontrar el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        # Enviar los resultados a la plantilla
        return render_template('resultado2.html', nombre=nombre_mas_largo, longitud=longitud)

    return render_template('form2.html')

if __name__ == '__main__':
    app.run(debug=True)
