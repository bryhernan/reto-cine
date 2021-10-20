import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=ASUS-PC;DATABASE=Cine_Colombia_Reto;UID=Support;PWD=20b10m22m')
    print("conexion exitosa")
    cursor=connection.cursor()
    cursor.execute("select @@version;")
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexion finalizada")