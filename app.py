from flask import Flask, request, render_template
import os
from forms import FormInicioSesion, FormRegistro

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
@app.route("/inicio")
def index():
    return render_template('inicio.html')

@app.route("/inicioSesion", methods=["GET","POST"])
def inicioSesion():
    if request.method == "GET":
            formularioI = FormInicioSesion()
            return render_template('inicioSesion.html', formI = formularioI)
    else:
        formularioI = FormInicioSesion(request.form)
        if formularioI.validate_on_submit():
            return render_template('inicio.html', errores ="Bienvenido" )
        return render_template('inicioSesion.html', formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/detallePelicula")
def detallePelicula():
    return render_template('detallePelicula.html')

@app.route("/cartelera")
def cartelera():
    return render_template('cartelera.html')

@app.route("/estrenos")
def estrenos():
    return render_template('estrenos.html')

@app.route("/registro")
def registro():
    if request.method == "GET":
            formularioI = FormRegistro()
            return render_template('registro.html', formI = formularioI)
    else:
        formularioI = FormRegistro(request.form)
        if formularioI.validate_on_submit():
            return render_template('inicio.html', errores ="Registrado" )
        return render_template('registro.html', formI = formularioI, errores = "Todos los datos son obligatorios")
