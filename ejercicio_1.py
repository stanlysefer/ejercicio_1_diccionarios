from tkinter import *
import tkinter as tk

ventana_principal = Tk()
ventana_principal.title("NOMBRE Y TELEFONOS DE ESTUDIANTES")

def mostrar_menu():
    menu_text.set("--- Menú ---\n"
                  "1. Agregar estudiante y teléfono\n"
                  "2. Consultar o modificar teléfono de un estudiante\n"
                  "3. Eliminar estudiante y teléfono\n"
                  "4. Ver todos los estudiantes y teléfonos\n"
                  "5. Salir")

def guardar_datos():
    with open("estudiantes.txt", "w") as archivo:
        for nombre, telefono in diccionario_estudiantes.items():
            archivo.write(f"{nombre}:{telefono}\n")

def cargar_datos():
    try:
        with open("estudiantes.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(":")
                if len(datos) == 2:
                    nombre, telefono = datos
                    diccionario_estudiantes[nombre] = telefono
                else:
                    print(f"Advertencia: línea ignorada en el archivo 'estudiantes.txt': '{linea.strip()}'")
    except FileNotFoundError:
        # Si el archivo no existe, simplemente lo crea
        with open("estudiantes.txt", "w"):
            pass


def agregar_estudiante():
    nombre = entry_nombre.get().upper()
    telefono = entry_telefono.get()
    if nombre and telefono:
        diccionario_estudiantes[nombre] = telefono
        guardar_datos()
        mensaje.set(f"Estudiante '{nombre}' y teléfono '{telefono}' agregados.")
        actualizar_lista_estudiantes()
    else:
        mensaje.set("Por favor, ingrese el nombre y el teléfono del estudiante.")

def consultar_o_modificar():
    nombre = entry_nombre.get().upper()
    if nombre in diccionario_estudiantes:
        telefono_actual = diccionario_estudiantes[nombre]
        mensaje.set(f"El teléfono actual de '{nombre}' es: {telefono_actual}")
    else:
        mensaje.set(f"No se encontró al estudiante '{nombre}' en el diccionario.")

def eliminar_estudiante():
    nombre = entry_nombre.get().upper()
    if nombre in diccionario_estudiantes:
        del diccionario_estudiantes[nombre]
        guardar_datos()
        mensaje.set(f"Estudiante '{nombre}' y su teléfono eliminados.")
        actualizar_lista_estudiantes()
    else:
        mensaje.set(f"No se encontró al estudiante '{nombre}' en el diccionario.")

def ver_todos():
    if diccionario_estudiantes:
        lista_estudiantes = [f"{nombre}: {telefono}" for nombre, telefono in diccionario_estudiantes.items()]
        listbox_estudiantes.delete(0, END)
        for estudiante in lista_estudiantes:
            listbox_estudiantes.insert(END, estudiante)
    else:
        mensaje.set("El diccionario está vacío.")
    label_info_estudiante.config(text="")

def mostrar_info_estudiante(event):
    seleccionado = listbox_estudiantes.curselection()
    if seleccionado:
        indice = seleccionado[0]
        estudiante_seleccionado = listbox_estudiantes.get(indice)
        label_info_estudiante.config(text=f"Estudiante seleccionado: {estudiante_seleccionado}")
    else:
        label_info_estudiante.config(text="")

def salir():
    guardar_datos()
    ventana_principal.destroy()

def actualizar_lista_estudiantes():
    lista_estudiantes = [f"{nombre}: {telefono}" for nombre, telefono in diccionario_estudiantes.items()]
    listbox_estudiantes.delete(0, END)
    for estudiante in lista_estudiantes:
        listbox_estudiantes.insert(END, estudiante)

# Inicializar el diccionario de estudiantes
diccionario_estudiantes = {}

# Cargar datos existentes (si los hay)
cargar_datos()

# Variables Tkinter
menu_text = tk.StringVar()
mensaje = tk.StringVar()

# Widgets
label_menu = tk.Label(ventana_principal, textvariable=menu_text, justify="left", padx=10)
entry_nombre = tk.Entry(ventana_principal, width=30)
entry_telefono = tk.Entry(ventana_principal, width=30)
btn_agregar = tk.Button(ventana_principal, text="Agregar", command=agregar_estudiante)
btn_consultar = tk.Button(ventana_principal, text="Consultar", command=consultar_o_modificar)
btn_eliminar = tk.Button(ventana_principal, text="Eliminar", command=eliminar_estudiante)
btn_ver_todos = tk.Button(ventana_principal, text="Ver Todos", command=ver_todos)
label_mensaje = tk.Label(ventana_principal, textvariable=mensaje, fg="blue")
btn_salir = tk.Button(ventana_principal, text="Salir", command=salir)

# Listbox para mostrar la lista de estudiantes y teléfonos
listbox_estudiantes = Listbox(ventana_principal, width=40, height=10)

# Label para mostrar la información del estudiante seleccionado
label_info_estudiante = tk.Label(ventana_principal, text="", fg="green")

# Posicionar Widgets
label_menu.grid(row=0, column=0, columnspan=2)
entry_nombre.grid(row=1, column=0, padx=10, pady=5)
entry_telefono.grid(row=1, column=1, padx=10, pady=5)
btn_agregar.grid(row=2, column=0, padx=10, pady=5)
btn_consultar.grid(row=2, column=1, padx=10, pady=5)
btn_eliminar.grid(row=3, column=0, padx=10, pady=5)
btn_ver_todos.grid(row=3, column=1, padx=10, pady=5)
label_mensaje.grid(row=4, column=0, columnspan=2)
listbox_estudiantes.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
btn_salir.grid(row=6, column=0, columnspan=2, pady=10)
label_info_estudiante.grid(row=7, column=0, columnspan=2, pady=5)

# Mostrar el menú inicial
mostrar_menu()

# Asociar la función mostrar_info_estudiante al evento de selección del listbox
listbox_estudiantes.bind("<<ListboxSelect>>", mostrar_info_estudiante)

# Ejecutar la aplicación
ventana_principal.mainloop()
