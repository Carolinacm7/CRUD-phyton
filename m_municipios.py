from conexion import *

class Mmunicipios:
  def mostrarMunicipio():
    try:
      cone = CConexion.ConexionBasedeDatos() 
      cursor = cone.cursor()
      cursor.execute("select * from municipio;")
      miResultado= cursor.fetchall()  
      cone.commit()
      print(cursor.rowcount,"registro ingresado")
      cone.close()
      return miResultado
    except mysql.connector.Error as error:
      print("Error de ingreso de datos {}".format(error))
      
  def ingresarMunicipio(Municipio,Altitud,NumeroVereda):
   try:
    cone = CConexion.ConexionBasedeDatos() 
    cursor = cone.cursor()
    sql = "insert into municipio values(null,%s,%s,%s);"
    #La variable valores 
    valores=(Municipio,Altitud,NumeroVereda)
    cursor.execute(sql,valores)
    cone.commit()
    print(cursor.rowcount,"registro ingresado")
    cone.close()
    
    
   except mysql.connector.Error as error:
    print("Error de ingreso de datos {}".format(error))
    
  def ModificarMunicipio(Id,Municipio,Altitud,NumeroVereda):
   try:
    cone = CConexion.ConexionBasedeDatos() 
    cursor = cone.cursor()
    sql = "update municipio set municipio.municipio = %s, municipio.altitud=%s,municipio.numeroVeredas=%s where municipio.id=%s;"
    #La variable valores 
    valores=(Municipio,Altitud,NumeroVereda,Id)
    cursor.execute(sql,valores)
    cone.commit()
    print(cursor.rowcount,"registro actualizado")
    cone.close()
    
    
   except mysql.connector.Error as error:
    print("Error de  actualizado de datos {}".format(error))
    
  def EliminarMunicipio(Id):
    try:
        cone = CConexion.ConexionBasedeDatos()
        cursor = cone.cursor()
        sql = "delete from municipio where municipio.id= %s;"
        # Asegúrate de que `valores` sea una tupla, incluso para un solo elemento
        valores = (Id,)  # Nota la coma al final para crear una tupla
        cursor.execute(sql, valores)
        cone.commit()
        print(cursor.rowcount, "registro eliminado")
        cone.close()
    except mysql.connector.Error as error:
        print("Error de eliminación de datos: {}".format(error))