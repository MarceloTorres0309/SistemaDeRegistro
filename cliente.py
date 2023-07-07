import tkinter as tk

class Cliente:
    """ Clase que implementa cliente"""
    def __init__(self, numero_documento="", razon_social="", direccion="", telefono=""):
        self.numero_documento = numero_documento
        self.razon_social = razon_social
        self.direccion = direccion
        self.telefono = telefono
    
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|".format(self.numero_documento,
                                      self.razon_social,
                                      self.direccion,
                                      self.telefono)

def insertar_cliente():
    numero_documento = numero_documento_entry.get()
    razon_social = razon_social_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()
    cliente = Cliente(numero_documento, razon_social, direccion, telefono)
    resultados_text.insert(tk.END, cliente.convertir_a_texto() + "\n")

ventana = tk.Tk()
ventana.title("Insertar Cliente")

numero_documento_label = tk.Label(ventana, text="Número de Documento:")
numero_documento_label.pack()
numero_documento_entry = tk.Entry(ventana)
numero_documento_entry.pack()

razon_social_label = tk.Label(ventana, text="Razón Social:")
razon_social_label.pack()
razon_social_entry = tk.Entry(ventana)
razon_social_entry.pack()

direccion_label = tk.Label(ventana, text="Dirección:")
direccion_label.pack()
direccion_entry = tk.Entry(ventana)
direccion_entry.pack()

telefono_label = tk.Label(ventana, text="Teléfono:")
telefono_label.pack()
telefono_entry = tk.Entry(ventana)
telefono_entry.pack()

insertar_button = tk.Button(ventana, text="Insertar", command=insertar_cliente)
insertar_button.pack()

resultados_text = tk.Text(ventana, width=40, height=10)
resultados_text.pack()

ventana.mainloop()