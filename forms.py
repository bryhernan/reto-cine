from flask_wtf import FlaskForm
from wtforms.validators import required, length
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.fields import SelectField, RadioField, FileField
from wtforms.fields.html5 import TimeField, DateField


class FormInicioSesion(FlaskForm):
    correo = StringField('Correo electrónico', validators=[required(),length(max=150)] )
    contrasena = PasswordField('Contraseña', validators=[required(),length(max=30)])
    ingreso = SubmitField('INGRESAR')

class FormRegistro(FlaskForm):
    nombres = StringField('Nombres', validators=[required(),length(max=150)], id='nombre_registro')
    apellidos = StringField('Apellidos', validators=[required(),length(max=150)], id='apellidos_registro')
    contrasena = PasswordField('Contraseña', validators=[required(), length(max=30)], id='contrasena_registro')
    confirmarContrasena = PasswordField('Confirmar contraseña', validators=[required(), length(max=30)], id='confirmarContrasena')
    email = EmailField('Email', validators=[required(), length(max=50)], id='email_registro')
    confirmarEmail = EmailField('Confirmar email', validators=[required(), length(max=50)], id='email_registro')
    tipoDocumento = SelectField('Tipo de Documento', choices=[('cedulaCiudadania','Cédula de Ciudadanía'),('cedulaExtranjeria','Cédula de Extranjería'),('pasaporte','Pasaporte')])
    numeroDocumento = StringField('Numero de Documento', validators=[required(), length(max=11)], id='numeroDocumento_registro')
    fechaNacimiento = DateField('Fecha de Nacimiento', validators=[required()], format='%Y-%m-%d')
    celular = StringField('Numero celular', validators=[required(),length(max=10)], id='numeroCelular_registro')
    ingreso = SubmitField('REGISTRAR') 

class FormBuscarPeli(FlaskForm):
    nombrePelicula = StringField('Pelicula ', validators=[length(max=150)] )
    director = StringField('Director ', validators=[length(max=150)] )
    actor = StringField('Actor ', validators=[length(max=150)] )
    genero = SelectField('Genero', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    clasificacion = SelectField('Clasificacion', choices=[('+18','+18'),('+16','+16'),('+12','+12')])
    buscar = SubmitField('Buscar')

class FormOpinarPelicula(FlaskForm):
    calificacion = RadioField("Calificación", choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")], id="calificacion_opinarPelicula")
    comentario = StringField("Comentario", validators=[length(max=1000)], id="comentario_opinarPelicula")
    comentar = SubmitField('Comentar')

class FormCrearPeli(FlaskForm):
    nombrePelicula = StringField('Titulo película ', validators=[required(),length(max=150)] )
    nombrePeliculaOriginal = StringField('Titulo original película', validators=[required(),length(max=150)])
    fechaEstreno = DateField('Fecha de estreno', validators=[required(),required()], format='%Y-%M-%D')
    duracion = TimeField('duracion ', validators=[required()])
    resena = TextAreaField('Sinopsis',validators=[required()])
    actor = SelectField('Actor', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    Director = SelectField('Director', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    genero = SelectField('Genero', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    clasificacion = SelectField('Clasificacion', choices=[('+18','+18'),('+16','+16'),('+12','+12')])
    poster = FileField("Poster")
    crear = SubmitField('crear')

class FormEditarPelicula(FlaskForm):
    peliculaModificar = SelectField('Película a modificar', choices=[('0000','007: Sin tiempo para morir'),('0001','Hello Kitty')])
    nombrePelicula = StringField('Titulo película ', validators=[required(),length(max=150)] )
    nombrePeliculaOriginal = StringField('Titulo original película', validators=[required(),length(max=150)])
    fechaEstreno = DateField('Fecha de estreno', validators=[required(),required()], format='%Y-%M-%D')
    duracion = TimeField('duracion ', validators=[required()])
    resena = TextAreaField('Sinopsis',validators=[required(),required()])
    actor = SelectField('Actor', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    Director = SelectField('Director', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    genero = SelectField('Genero', choices=[('terror','terror'),('Accion','Accion'),('Aventura','Aventura')])
    clasificacion = SelectField('Clasificacion', choices=[('+18','+18'),('+16','+16'),('+12','+12')])
    poster = FileField("Poster")
    crear = SubmitField('Editar')

class FormEditarUsuario(FlaskForm):
    idUsuario = StringField('ID usuario', validators=[length(max=5)], id="idUsuario_editar")
    nombres = StringField('Nombres', validators=[length(max=150)], id='nombre_editar')
    apellidos = StringField('Apellidos', validators=[length(max=150)], id='apellidos_editar')
    contrasena = PasswordField('Contraseña', validators=[length(max=30)], id='contrasena_editar')
    email = EmailField('Email', validators=[length(max=50)], id='email_editar')
    tipoDocumento = SelectField('Tipo de Documento', choices=[('cedulaCiudadania','Cédula de Ciudadanía'),('cedulaExtranjeria','Cédula de Extranjería'),('pasaporte','Pasaporte')])
    numeroDocumento = StringField('Numero de Documento', validators=[length(max=11)], id='numeroDocumento_editar')
    fechaNacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d')
    celular = StringField('Numero celular', validators=[length(max=10)], id='numeroCelular_editar')
    editar = SubmitField('Editar')
    eliminar = SubmitField('Eliminar')

class FormRegistrarAdministradores(FlaskForm):
    nombre = StringField('Nombres', validators=[required(),length(max=150)], id='nombre_registroAdministrador')
    email = EmailField('Email', validators=[required(),length(max=50)], id='email_registroAdministrador')
    contrasena = PasswordField('Contraseña', validators=[required(),length(max=30)], id='contrasena_registroAdministrador')
    tipoDocumento = SelectField('Tipo de Documento', choices=[('cedulaCiudadania','Cédula de Ciudadanía'),('cedulaExtranjeria','Cédula de Extranjería'),('pasaporte','Pasaporte')])
    numeroDocumento = StringField('Numero de Documento', validators=[required(),length(max=11)], id='numeroDocumento_registroAdministrador')
    registrar = SubmitField('Registrar')

class FormEditarAdministradores(FlaskForm):
    nombre = StringField('Nombres', validators=[length(max=150)], id='nombre_registroAdministrador')
    email = EmailField('Email', validators=[length(max=50)], id='email_registroAdministrador')
    contrasena = PasswordField('Contraseña', validators=[length(max=30)], id='contrasena_registroAdministrador')
    tipoDocumento = SelectField('Tipo de Documento', choices=[('cedulaCiudadania','Cédula de Ciudadanía'),('cedulaExtranjeria','Cédula de Extranjería'),('pasaporte','Pasaporte')])
    numeroDocumento = StringField('Numero de Documento', validators=[length(max=11)], id='numeroDocumento_registroAdministrador')
    registrar = SubmitField('Editar')
    eliminar = SubmitField('Eliminar')

class FormRegistrarReparto(FlaskForm):
    nombres = StringField('Nombres', validators=[required(),length(max=150)], id='nombreRegistro_reparto')
    apellidos = StringField('Apellidos', validators=[required(),length(max=150)], id='apellidosRegistro_reparto')
    tipoPersona = RadioField("Tipo", validators=[required()],choices=[("actor","Actor"),("director","Director")], id="tipoPersonaRegistro_opinarPelicula")
    resena = StringField('Reseña', validators=[required(),length(max=1000)], id='reseñaRegistro_reparto')
    registrar = SubmitField('Registrar')

class FormEditarReparto(FlaskForm):
    nombres = StringField('Nombres', validators=[length(max=150)], id='nombreRegistroEditar_reparto')
    apellidos = StringField('Apellidos', validators=[length(max=150)], id='apellidosRegistroEditar_reparto')
    tipoPersona = RadioField("Tipo", choices=[("actor","Actor"),("director","Director")], id="tipoPersonaRegistroEditar_opinarPelicula")
    resena = StringField('Reseña', validators=[length(max=1000)], id='reseñaRegistroEditar_reparto')
    editar = SubmitField('Editar')
    eliminar = SubmitField('Eliminar')

