from flask import Flask, request, render_template
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
@app.route("/inicio")
def index():
    return render_template('inicio.html')

@app.route("/inicioSesion")
def inicioSesion():
    return render_template('inicioSesion.html')