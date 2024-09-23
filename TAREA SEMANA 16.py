import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("𝓖𝓮𝓼𝓽𝓸𝓻 𝓭𝓮 𝓣𝓪𝓻𝓮𝓪𝓼")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="𝓐ñ𝓪𝓭𝓲𝓻 𝓣𝓪𝓻𝓮𝓪", command=self.add_task, bg="pink", fg="black")
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="𝓣𝓪𝓻𝓮𝓪 𝓒𝓸𝓶𝓹𝓵𝓮𝓽𝓪𝓭𝓪", command=self.complete_task, bg="PaleGreen", fg="black")
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="𝓔𝓵𝓲𝓶𝓲𝓷𝓪𝓻 𝓣𝓪𝓻𝓮𝓪", command=self.delete_task, bg="NavajoWhite", fg="black")
        self.delete_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.task_listbox.bind("<<ListboxSelect>>", self.on_task_select)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('c', lambda event: self.complete_task())
        self.root.bind('d', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

        self.selected_task_index = None

    def on_task_select(self, event):
        selection = self.task_listbox.curselection()
        if selection:
            self.selected_task_index = selection[0]

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea!")

    def complete_task(self):
        if self.selected_task_index is not None:
            self.tasks[self.selected_task_index]['completed'] = True
            self.update_task_listbox()
            self.selected_task_index = None

    def delete_task(self):
        if self.selected_task_index is not None:
            del self.tasks[self.selected_task_index]
            self.update_task_listbox()
            self.selected_task_index = None

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task['completed']:
                self.task_listbox.insert(tk.END, f"[Completada] {task['task']}")
            else:
                self.task_listbox.insert(tk.END, task['task'])

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()