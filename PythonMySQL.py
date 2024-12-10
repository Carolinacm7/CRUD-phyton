import tkinter as tk
#importacion modulos restantes 

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from m_municipios import *
from conexion import *


class FormularioMunicipios:
   global base 
   base = None
   
   global textBoxId
   textBoxId = None
   
   
   global texBoxtMunicipio
   texBoxtMunicipio = None
   
   global texBoxtAltitud
   texBoxtAltitud = None 
   
   global texBoxtNumeroVereda
   texBoxtNumeroVereda= None 
   
   global tree
   tree = None
   
  
  
def Formulario():
      global textBoxId
      global texBoxtMunicipio
      global texBoxtAltitud
      global texBoxtNumeroVereda
      global base 
      global groupBox
      global tree
      try:
        base = Tk()
        base.geometry("1200x300")
        base.title("Formulario Python")
        groupBox= LabelFrame(base,text="Datos del Municipio",padx=5,pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)
        
        LabelId = Label(groupBox,text="Id:",width=16,font=("arial",12)).grid(row=0,column=0)
        textBoxId = Entry(groupBox) 
        textBoxId.grid(row=0,column=1)
        
        LabelMunicipio = Label(groupBox,text="Municipio:",width=16,font=("arial",12)).grid(row=1,column=0)
        texBoxtMunicipio = Entry(groupBox)
        texBoxtMunicipio.grid(row=1,column=1)
        
        LabelAltitud = Label(groupBox,text="Altitud:",width=16,font=("arial",12)).grid(row=2,column=0)
        texBoxtAltitud = Entry(groupBox)
        texBoxtAltitud.grid(row=2,column=1)
        
        LabelNumeroVereda = Label(groupBox,text="Numero de Veredas:",width=16,font=("arial",12)).grid(row=3,column=0)
        texBoxtNumeroVereda = Entry(groupBox)
        texBoxtNumeroVereda.grid(row=3,column=1)
        
        Button(groupBox,text="Guardar",width=10, command=guardarRegistros).grid(row=4,column=0)
        Button(groupBox,text="Modificar",width=10 , command=modificarRegistros).grid(row=4,column=1)
        Button(groupBox,text="Eliminar",width=10, command=eliminarRegistros).grid(row=4,column=2)
        
        
        groupBox= LabelFrame(base,text="Lista de Municipio",padx=5,pady=5,)
        groupBox.grid(row=0,column=1,padx=5,pady=5)
        #Crear un Treeview
        tree = ttk.Treeview(groupBox,columns=("Id","Municipios","Altitud","numero de veredas"),show='headings',height=5)
        tree.column("#1",anchor=CENTER)
        tree.heading("#1",text="id")
        
        tree.column("#2",anchor=CENTER)
        tree.heading("#2",text="Municipio")
        tree.pack()
        
        tree.column("#3",anchor=CENTER)
        tree.heading("#3",text="Altitud")
        
        tree.column("#4",anchor=CENTER)
        tree.heading("#4",text="Numero de Veredas")
        
        #agregar datos a la tabla 
        
        for row in Mmunicipios.mostrarMunicipio():
          tree.insert("","end",values=row)
        
        # funcion click 
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro )
        
        
        tree.pack()
         
        base.mainloop()
        
      except ValueError as error:
        print("Error al mostrar la interfaz,error:{}".format(error))



def guardarRegistros():
     global texBoxtMunicipio,texBoxtAltitud,texBoxtNumeroVereda,groupBox
     try:
       if texBoxtMunicipio is None or texBoxtAltitud is None or texBoxtNumeroVereda is None:
            print("los witgets no estan inicializados")
            return 
       Municipio =texBoxtMunicipio.get()
       Altitud =texBoxtAltitud.get()
       NumeroVereda =texBoxtNumeroVereda.get()
          
       Mmunicipios.ingresarMunicipio(Municipio,Altitud,NumeroVereda) 
       messagebox.showinfo("Informacion", "los datos fueron guardados")
       
       actualizarTreeView()
       
       #Limpiar campos 
       texBoxtMunicipio.delete(0,END)
       texBoxtAltitud.delete(0,END)
       texBoxtNumeroVereda.delete(0,END)
     except ValueError as error:
       print("error a ingresar los datos {}",format(error))

def modificarRegistros():
     global textBoxId,texBoxtMunicipio,texBoxtAltitud,texBoxtNumeroVereda,groupBox
     try:
       if textBoxId is None or texBoxtMunicipio is None or texBoxtAltitud is None or texBoxtNumeroVereda is None:
            print("los witgets no estan inicializados")
            return 
       Id = textBoxId.get()   
       Municipio =texBoxtMunicipio.get()
       Altitud =texBoxtAltitud.get()
       NumeroVereda =texBoxtNumeroVereda.get()
          
       Mmunicipios.ModificarMunicipio(Id,Municipio,Altitud,NumeroVereda) 
       messagebox.showinfo("Informacion", "los datos fueron actualizada")
       
       actualizarTreeView()
       
       #Limpiar campos 
       textBoxId.delete(0,END)
       texBoxtMunicipio.delete(0,END)
       texBoxtAltitud.delete(0,END)
       texBoxtNumeroVereda.delete(0,END)
     except ValueError as error:
       print("error a modificar los datos {}",format(error))
       
def eliminarRegistros():
     global textBoxId,texBoxtMunicipio,texBoxtAltitud,texBoxtNumeroVereda
     try:
       if textBoxId is None:
            print("los witgets no estan inicializados")
            return 
       Id = textBoxId.get()   
      
       Mmunicipios.EliminarMunicipio(Id) 
       messagebox.showinfo("Informacion", "los datos fueron eliminados")
       
       actualizarTreeView()
       
       #Limpiar campos 
       textBoxId.delete(0,END)
       texBoxtMunicipio.delete(0,END)
       texBoxtAltitud.delete(0,END)
       texBoxtNumeroVereda.delete(0,END)
       
     except ValueError as error:
       print("error a modificar los datos {}",format(error))

 
def actualizarTreeView():
  global tree
  try:
   
    tree.delete(*tree.get_children())
    #obtener los nuevos datos a mostrar 
    datos = Mmunicipios.mostrarMunicipio()
    #insertar nuevos datos en tabla 
    for row in Mmunicipios.mostrarMunicipio():
      tree.insert("","end",values=row)
  except ValueError as error:
    print("error al actualizar tabla {}".format(error))
    
def seleccionarRegistro(event):
  try:
    #obtener el id seleccionado
    itemSeleccionado = tree.focus()
    
    if itemSeleccionado:
      #obtener columnas 
      values = tree.item(itemSeleccionado)['values']
      
      textBoxId.delete(0,END)
      textBoxId.insert(0,values[0])
      
      
      texBoxtMunicipio.delete(0,END)
      texBoxtMunicipio.insert(0,values[1])
      
      texBoxtAltitud.delete(0,END)
      texBoxtAltitud.insert(0,values[2])
      
      texBoxtNumeroVereda.delete(0,END)
      texBoxtNumeroVereda.insert(0,values[3])
      
  except ValueError as error:
    print("Error al seleccionar registro:{}".format(error))
    
       
Formulario()