import tkinter as tk

class VentaDetalle:
    """Clase que implementa detalle de una venta"""
    def __init__(self, item, codigo, descripcion, cantidad, precio_unitario):
        self.item = item
        self.codigo = codigo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.base_imponible = (cantidad * precio_unitario) / 1.18
        self.igv = (cantidad * precio_unitario) - (cantidad * precio_unitario) / 1.18
        self.total = cantidad * precio_unitario
    
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.item,
                                                  self.codigo,
                                                  self.descripcion,
                                                  self.cantidad,
                                                  self.precio_unitario,
                                                  self.base_imponible,
                                                  self.igv,
                                                  self.total)

def insertar_detalle_venta():
    item = item_entry.get()
    codigo = codigo_entry.get()
    descripcion = descripcion_entry.get()
    cantidad = float(cantidad_entry.get())
    precio_unitario = float(precio_unitario_entry.get())
    
    venta_detalle = VentaDetalle(item, codigo, descripcion, cantidad, precio_unitario)
    
    resultados_text.insert(tk.END, venta_detalle.convertir_a_texto() + "\n")

ventana = tk.Tk()
ventana.title("Insertar Detalle de Venta")

item_label = tk.Label(ventana, text="Item:")
item_label.pack()
item_entry = tk.Entry(ventana)
item_entry.pack()

codigo_label = tk.Label(ventana, text="Código:")
codigo_label.pack()
codigo_entry = tk.Entry(ventana)
codigo_entry.pack()

descripcion_label = tk.Label(ventana, text="Descripción:")
descripcion_label.pack()
descripcion_entry = tk.Entry(ventana)
descripcion_entry.pack()

cantidad_label = tk.Label(ventana, text="Cantidad:")
cantidad_label.pack()
cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack()

precio_unitario_label = tk.Label(ventana, text="Precio Unitario:")
precio_unitario_label.pack()
precio_unitario_entry = tk.Entry(ventana)
precio_unitario_entry.pack()

insertar_button = tk.Button(ventana, text="Insertar", command=insertar_detalle_venta)
insertar_button.pack()

resultados_text = tk.Text(ventana, width=60, height=10)
resultados_text.pack()

ventana.mainloop()
