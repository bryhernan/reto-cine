from flask import Flask, request, render_template
import os
from forms import FormEditarPelicula, FormEditarUsuario, FormInicioSesion, FormOpinarPelicula, FormRegistro, FormBuscarPeli, FormCrearPeli

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

@app.route("/detallePelicula", methods=["GET","POST"])
def detallePelicula():
    if request.method == "GET":
            formularioI = FormOpinarPelicula()
            return render_template('detallePelicula.html', formI = formularioI)
    else:
        formularioI = FormOpinarPelicula(request.form)
        if formularioI.validate_on_submit():
            return render_template('detallePelicula.html',formI = formularioI)
        return render_template('detallePelicula.html',formI = formularioI, errores = "campo invalidado")

@app.route("/cartelera", methods=["GET","POST"])
def cartelera():
    if request.method == "GET":
            formularioI = FormBuscarPeli()
            return render_template('cartelera.html', formI = formularioI)
    else:
        formularioI = FormBuscarPeli(request.form)
        if formularioI.validate_on_submit():
            return render_template('cartelera.html',formI = formularioI)
        return render_template('cartelera.html',formI = formularioI, errores = "campo invalidado")


@app.route("/estrenos")
def estrenos():
    return render_template('estrenos.html')

@app.route("/registro", methods=["GET","POST"])
def registro():
    if request.method == "GET":
            formularioI = FormRegistro()
            return render_template('registro.html', formI = formularioI)
    else:
        formularioI = FormRegistro(request.form)
        if formularioI.validate_on_submit():
            return render_template('inicio.html', errores ="Registrado" )
        return render_template('registro.html', formI = formularioI, errores = "Todos los datos son obligatorios")


@app.route("/crearPelicula", methods=["GET","POST"])
def crearPelicula():
    if request.method == "GET":
            formularioI = FormCrearPeli()
            return render_template('crearPelicula.html', formI = formularioI)
    else:
        formularioI = FormCrearPeli(request.form)
        if formularioI.validate_on_submit():
            return render_template('crearPelicula.html', errores ="Creada" )
        return render_template('crearPelicula.html', formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/editarPelicula", methods=["GET","POST"])
def editarPelicula():
    if request.method == "GET":
        formularioI = FormEditarPelicula()
        return render_template('editarPelicula.html', formI = formularioI)
    else:
        formularioI = FormEditarPelicula(request.form)
        if formularioI.validate_on_submit():
            return render_template('editarPelicula.html', errores = "Editado")
        return render_template('editarPelicula',  formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/administrarUsuarios", methods=["GET","POST"])
def administrarUsuarios():
    if request.method == "GET":
        formularioI = FormEditarUsuario()
        return render_template('administrarUsuarios.html', formI = formularioI)
    else:
        formularioI = FormEditarUsuario(request.form)
        if formularioI.validate_on_submit():
            return render_template('administrarUsuarios.html', errores = "Editado")
        return render_template('administrarUsuarios.html',  formI = formularioI, errores = "Todos los datos son obligatorios")