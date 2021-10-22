from pyodbc import Row
import db


def categoriasS():
    sql= "EXEC CM_CATEGORIAS_S"
    return db.ejecutarSelect(sql,None)
def generosS():
    sql= "EXEC CM_GENEROS_S"
    return db.ejecutarSelect(sql,None)
def salasS():
    sql= "EXEC CM_SALAS_S"
    return db.ejecutarSelect(sql,None)
def tiposDocumentosS():
    sql= "EXEC CM_TIPO_DOCUMENTOS_S"
    return db.ejecutarSelect(sql,None)
def tipoPagoS():
    sql= "EXEC CM_TIPO_PAGO_S"
    return db.ejecutarSelect(sql,None)
def tipoTicketS():
    sql= "EXEC CM_TIPO_TIKETS_S"
    return db.ejecutarSelect(sql,None)
def tipoUsuarioS():
    sql= "EXEC CM_TIPO_USUARIOS_S"
    return db.ejecutarSelect(sql,None)

def usuarriosS(id_usuario,nombres_usuario,apellidos_usuario,correo_usuario,fecha_nacimiento,celular,id_tipo_documento,id_tipo_usuario):
    sql= "EXEC CA_USUARIOS_S @id_usuario = ?,@nombres_usuario = ?,@apellidos_usuario = ?,@correo_usuario = ?,@fecha_nacimiento = ?,@celular = ?,@id_tipo_documento = ?,@id_tipo_usuario = ?"
    return db.ejecutarSelect(sql,None)