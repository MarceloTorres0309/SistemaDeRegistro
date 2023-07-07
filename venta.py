import tkinter as tk
from cliente import Cliente
from venta_detalle import VentaDetalle

class Venta:
    """Clase que implementa venta"""
    def __init__(self, numero, cliente: Cliente, detalle: VentaDetalle = [], total = 0):
        self.serie = 'F005'
        self.numero = numero
        self.cliente: Cliente = cliente
        self.detalle: list = detalle
        self.base_imponible = total / 1.18
        self.igv = total - (total / 1.18)
        self.total = total
    
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|".format(self.serie, self.numero, self.base_imponible, self.igv, self.total)

def insertar_venta():
    numero = numero_entry.get()
    total = float(total_entry.get())
    cliente = Cliente(cliente_numero_documento_entry.get(), cliente_razon_social_entry.get(), cliente_direccion_entry.get(), cliente_telefono_entry.get())
    
    venta = Venta(numero, cliente, [], total)
    resultados_text.insert(tk.END, venta.convertir_a_texto() + "\n")

ventana = tk.Tk()
ventana.title("Insertar Venta")

numero_label = tk.Label(ventana, text="Número:")
numero_label.pack()
numero_entry = tk.Entry(ventana)
numero_entry.pack()

total_label = tk.Label(ventana, text="Total:")
total_label.pack()
total_entry = tk.Entry(ventana)
total_entry.pack()

cliente_numero_documento_label = tk.Label(ventana, text="Número de Documento del Cliente:")
cliente_numero_documento_label.pack()
cliente_numero_documento_entry = tk.Entry(ventana)
cliente_numero_documento_entry.pack()

cliente_razon_social_label = tk.Label(ventana, text="Razón Social del Cliente:")
cliente_razon_social_label.pack()
cliente_razon_social_entry = tk.Entry(ventana)
cliente_razon_social_entry.pack()

cliente_direccion_label = tk.Label(ventana, text="Dirección del Cliente:")
cliente_direccion_label.pack()
cliente_direccion_entry = tk.Entry(ventana)
cliente_direccion_entry.pack()

cliente_telefono_label = tk.Label(ventana, text="Teléfono del Cliente:")
cliente_telefono_label.pack()
cliente_telefono_entry = tk.Entry(ventana)
cliente_telefono_entry.pack()

insertar_button = tk.Button(ventana, text="Insertar", command=insertar_venta)
insertar_button.pack()

resultados_text = tk.Text(ventana, width=60, height=10)
resultados_text.pack()

ventana.mainloop()
