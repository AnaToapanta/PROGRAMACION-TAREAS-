import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):  # Corregido aquí
        self.root = root
        self.root.title("Agenda Personal")

        # Configuración del Frame principal
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(pady=10)

        # Configuración del TreeView
        self.tree = ttk.Treeview(self.frame_principal, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack(side=tk.LEFT)

        # Barra de desplazamiento
        self.scrollbar = ttk.Scrollbar(self.frame_principal, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame de entrada
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0)
        self.entry_fecha = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.entry_fecha.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0)
        self.entry_hora = tk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entry_descripcion = tk.Entry(self.frame_entrada)
        self.entry_descripcion.grid(row=2, column=1)

        # Botones
        self.btn_agregar = tk.Button(self.frame_entrada, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=3, column=0, pady=10)

        self.btn_eliminar = tk.Button(self.frame_entrada, text="Eliminar Evento Seleccionado",
                                      command=self.eliminar_evento)
        self.btn_eliminar.grid(row=3, column=1, pady=10)

        self.btn_salir = tk.Button(self.frame_entrada, text="Salir", command=self.root.quit)
        self.btn_salir.grid(row=3, column=2, pady=10)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        self.entry_fecha.set_date('')  # Limpia el DateEntry
        self.entry_hora.delete(0, tk.END)  # Limpia el Entry de hora
        self.entry_descripcion.delete(0, tk.END)  # Limpia el Entry de descripción

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar el evento seleccionado?")
        if confirmacion:
            for item in seleccion:
                self.tree.delete(item)

if __name__ == "__main__":  # Corregido aquí
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()