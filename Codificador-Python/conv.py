import tkinter as tk
from tkinter import messagebox, filedialog

def convertir_a_binario():
    instruccion = entrada_texto.get().replace(",", "")
    partes = instruccion.split()
    
    if not partes:
        messagebox.showerror("Error", "Ingrese una instrucción válida.")
        return
    
    opcode_dict = {"SUMA": "00", "RESTA": "01", "SLT": "10", "SW": "11"}
    
    try:
        opcode = opcode_dict.get(partes[0].upper(), None)
        if opcode is None:
            raise ValueError("Operación no reconocida")
        
        if partes[0].upper() in ["SUMA", "RESTA", "SLT"]:
            rd = format(int(partes[1][1:]), '05b')
            rs1 = format(int(partes[2][1:]), '05b')
            rs2 = format(int(partes[3][1:]), '05b')
            resultado = f"{opcode}{rd}{rs1}{rs2}"
        
        elif partes[0].upper() == "SW":
            x = "00000"  # Según la tabla, el campo RD en SW es siempre 00000
            direccion = format(int(partes[1][1:]), '05b')
            dato = format(int(partes[2][1:]), '05b')
            resultado = f"{opcode}{x}{direccion}{dato}"
        
        else:
            raise ValueError("Formato de instrucción incorrecto")
        
        etiqueta_resultado.config(text=f"Binario: {resultado}")
        guardar_en_archivo(resultado)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def guardar_en_archivo(resultado):
    if not ruta_archivo.get():
        messagebox.showerror("Error", "Seleccione una ruta para guardar el archivo.")
        return
    
    with open(ruta_archivo.get(), "a") as archivo:
        archivo.write(f"{resultado}\n")

def seleccionar_archivo():
    archivo_seleccionado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "")])
    if archivo_seleccionado:
        ruta_archivo.set(archivo_seleccionado)
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Instrucciones a Binario")
ventana.geometry("500x300")
ventana.configure(bg="#2C3E50")  # Color de fondo oscuro

ruta_archivo = tk.StringVar()

# Widgets con colores y estilos
etiqueta = tk.Label(ventana, text="Ingrese la instrucción:", bg="#2C3E50", fg="white", font=("Arial", 12))
etiqueta.pack(pady=5)

entrada_texto = tk.Entry(ventana, width=50, font=("Arial", 12), bg="#ECF0F1", fg="#2C3E50")
entrada_texto.pack(pady=5)

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_a_binario, bg="#3498DB", fg="white", font=("Arial", 12), padx=10, pady=5)
boton_convertir.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="Binario: ", bg="#2C3E50", fg="white", font=("Arial", 12))
etiqueta_resultado.pack(pady=5)

frame_guardado = tk.Frame(ventana, bg="#2C3E50")
frame_guardado.pack(pady=5)

entrada_archivo = tk.Entry(frame_guardado, textvariable=ruta_archivo, width=40, font=("Arial", 12), bg="#ECF0F1", fg="#2C3E50")
entrada_archivo.pack(side=tk.LEFT, padx=5)

boton_seleccionar = tk.Button(frame_guardado, text="Seleccionar Archivo", command=seleccionar_archivo, bg="#E74C3C", fg="white", font=("Arial", 12), padx=10, pady=5)
boton_seleccionar.pack(side=tk.RIGHT)

# Ejecutar la aplicación
ventana.mainloop()