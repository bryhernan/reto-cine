import pyodbc



def conectar():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=ASUS-PC;DATABASE=Cine_Colombia_Reto;UID=Support;PWD=20b10m22m')
        print("conexion exitosa")
        return connection
    except Exception as ex:
        return None


def ejecutarInsert(_sql, listaParametros):
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            filas = cursor.execute(_sql, listaParametros).rowcount
            cursor.close()
            conn.commit()
            conn.close()
            return filas
        else:
            print("no se pudo conectar a la base de datos")
            return -1
    except Exception as ex:
        print("ocurrio un error")
        return -1

def ejecutarSelect(_sql,listaParametros):
    try:
        conn = conectar()
        if conn:
            conn.row_factory = fabricaDiccionarios()
            cursor = conn.cursor()
            if listaParametros:
                cursor.execute(_sql,listaParametros)
            else:
                cursor.execute(_sql)

            filas = cursor.fetchall()
            cursor.close()
            conn.close()
            return filas
        else:
            print("no se pudo establecer conexion")
            return None
    except Exception as ex:
        print("Error en la ejecucion" + str(ex))
        return None

def fabricaDiccionarios(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]]= row[idx]
    return d 
