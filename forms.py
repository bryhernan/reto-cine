from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField

class FormInicioSesion(FlaskForm):
    correo = StringField('Correo electrónico', validators=[validators.required(),validators.length(max=150)] )
    contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=30)])
    ingreso = SubmitField('INGRESAR') 