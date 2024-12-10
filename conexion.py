import mysql.connector

class CConexion:
  def ConexionBasedeDatos():
    try:
      conexion = mysql.connector.connect(user='root',password='Annie',
                                         host='127.0.0.1',
                                         database='municipiodb',
                                         port='3307') 
      print("conexion correcta")
      return conexion
    except mysql.connector.Error as error:
      print("Error al conectarse a la base de datos {}")

  ConexionBasedeDatos()