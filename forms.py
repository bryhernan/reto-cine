from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.widgets import HiddenInput
from wtforms.fields import SelectField, DateField

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