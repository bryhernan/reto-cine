from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.widgets import HiddenInput
from wtforms.fields import SelectField, RadioField
from wtforms.fields.html5 import TimeField, DateField


class FormInicioSesion(FlaskForm):
    correo = StringField('Correo electrónico', validators=[validators.required(),validators.length(max=150)] )
    contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=30)])
    ingreso = SubmitField('INGRESAR')

class FormRegistro(FlaskForm):
    nombres = StringField('Nombres', validators=[validators.required(),validators.length(max=150)], id='nombre_registro')
    apellidos = StringField('Apellidos', validators=[validators.required(),validators.length(max=150)], id='apellidos_registro')
    contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=30)], id='contrasena_registro')
    confirmarContrasena = PasswordField('Confirmar contraseña', validators=[validators.required(), validators.length(max=30)], id='confirmarContrasena')
    email = EmailField('Email', validators=[validators.required(), validators.length(max=50)], id='email_registro')
    confirmarEmail = EmailField('Confirmar email', validators=[validators.required(), validators.length(max=50)], id='email_registro')
    tipoDocumento = SelectField('Tipo de Documento', choices=[('cedulaCiudadania','Cédula de Ciudadanía'),('cedulaExtranjeria','Cédula de Extranjería'),('pasaporte','Pasaporte')])
    numeroDocumento = StringField('Numero de Documento', validators=[validators.required(), validators.length(max=11)], id='numeroDocumento_registro')
    fechaNacimiento = DateField('Fecha de Nacimiento', validators=[validators.required()], format='%Y-%M-%D')
    celular = StringField('Numero celular', validators=[validators.required(),validators.length(max=10)], id='numeroCelular_registro')
    ingreso = SubmitField('REGISTRAR') 

class FormBuscarPeli(FlaskForm):
    nombrePelicula = StringField('Pelicula ', validators=[validators.length(max=150)] )
    director = StringField('Director ', validators=[validators.length(max=150)] )
    actor = StringField('Actor ', validators=[validators.length(max=150)] )
    genero = SelectField('Genero', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    clasificacion = SelectField('Clasificacion', choices=[('+18','+18'),('+16','+16'),('+12','+12')])
    buscar = SubmitField('Buscar')

class FormOpinarPelicula(FlaskForm):
    calificacion = RadioField("Calificación", choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")], id="calificacion_opinarPelicula")
    comentario = StringField("Comentario", validators=[validators.length(max=1000)], id="comentario_opinarPelicula")
    comentar = SubmitField('Comentar')

class FormCrearPeli(FlaskForm):
    nombrePelicula = StringField('Pelicula ', validators=[validators.required(),validators.length(max=150)] )
    nombrePeliculaOriginal = StringField('Pelicula ', validators=[validators.required(),validators.length(max=150)])
    fechaEstreno = DateField('Fecha de estreno', validators=[validators.required(),validators.required()], format='%Y-%M-%D')
    duracion = TimeField('duracion ', validators=[validators.required()])
    resena = TextAreaField('Reseña',validators=[validators.required(),validators.required()])
    actor = SelectField('Actor', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    Director = SelectField('Director', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    genero = SelectField('Genero', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    clasificacion = SelectField('Clasificacion', choices=[('+18','+18'),('+16','+16'),('+12','+12')])
    crear = SubmitField('crear')

