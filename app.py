from flask import Flask, request, render_template
import os
from forms import FormInicioSesion, FormOpinarPelicula, FormRegistro, FormBuscarPeli, FormCrearPeli, FormEditarUsuario, FormEditarPelicula, FormRegistrarAdministradores, FormEditarAdministradores, FormRegistrarReparto, FormEditarReparto

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
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


@app.route("/crearPelicula")
def crearPelicula():
    if request.method == "GET":
            formularioI = FormCrearPeli()
            return render_template('crearPelicula.html', formI = formularioI)
    else:
        formularioI = FormCrearPeli(request.form)
        if formularioI.validate_on_submit():
            return render_template('crearPelicula.html', errores ="Registrada" )
        return render_template('crearPelicula.html', formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/DetallesUsuario")
def detallesUsuario():
    return render_template('detallesUsuario.html')

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

@app.route("/administrarAdministradores", methods=["GET","POST"])
def administrarAdministradores():
    if request.method == "GET":
        formularioI = FormEditarAdministradores()
        return render_template('administrarAdministradores.html', formI = formularioI)
    else:
        formularioI = FormEditarAdministradores(request.form)
        if formularioI.validate_on_submit():
            return render_template('administrarAdministradores.html', errores = "Editado")
        return render_template('administrarAdministradores.html',  formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/registroAdministradores", methods=["GET","POST"])
def registroAdministradores():
    if request.method == "GET":
        formularioI = FormRegistrarAdministradores()
        return render_template('registroAdministradores.html', formI = formularioI)
    else:
        formularioI = FormRegistrarAdministradores(request.form)
        if formularioI.validate_on_submit():
            return render_template('registroAdministradores.html', errores = "Editado")
        return render_template('registroAdministradores.html',  formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/registroReparto", methods=["GET","POST"])
def registroReparto():
    if request.method == "GET":
        formularioI = FormRegistrarReparto()
        return render_template('registroReparto.html', formI = formularioI)
    else:
        formularioI = FormRegistrarReparto(request.form)
        if formularioI.validate_on_submit():
            return render_template('registroReparto.html', errores = "Registrado")
        return render_template('registroReparto.html',  formI = formularioI, errores = "Todos los datos son obligatorios")

@app.route("/administrarReparto", methods=["GET","POST"])
def administrarReparto():
    if request.method == "GET":
        formularioI = FormEditarReparto()
        return render_template('administrarReparto.html', formI = formularioI)
    else:
        formularioI = FormEditarReparto(request.form)
        if formularioI.validate_on_submit():
            return render_template('administrarReparto.html', errores = "Editado")
        return render_template('administrarReparto.html',  formI = formularioI, errores = "Todos los datos son obligatorios")