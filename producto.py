import tkinter as tk

class Producto:
    """ Clase que implementa producto"""
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def convertir_a_texto(self):
        return "|{}|{}|{}|".format(self.codigo, self.nombre, self.precio)

def insertar_producto():
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    precio = precio_entry.get()
    producto = Producto(codigo, nombre, precio)
    resultados_text.insert(tk.END, producto.convertir_a_texto() + "\n")

ventana = tk.Tk()
ventana.title("Insertar Producto")

codigo_label = tk.Label(ventana, text="Código:")
codigo_label.pack()
codigo_entry = tk.Entry(ventana)
codigo_entry.pack()

nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

precio_label = tk.Label(ventana, text="Precio:")
precio_label.pack()
precio_entry = tk.Entry(ventana)
precio_entry.pack()

insertar_button = tk.Button(ventana, text="Insertar", command=insertar_producto)
insertar_button.pack()

resultados_text = tk.Text(ventana, width=40, height=10)
resultados_text.pack()

ventana.mainloop()
