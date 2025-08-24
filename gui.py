# gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
from clips_engine import ClipsEngine

class ClipsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto con CLIPS")
        self.engine = ClipsEngine()

        # Área para reglas
        tk.Label(root, text="Definir reglas:").pack()
        self.txt_reglas = scrolledtext.ScrolledText(root, width=60, height=10)
        self.txt_reglas.pack()

        tk.Button(root, text="Cargar Reglas", command=self.cargar_reglas).pack()

        # Área para hechos
        tk.Label(root, text="Ingresar hecho:").pack()
        self.hecho_entry = tk.Entry(root, width=50)
        self.hecho_entry.pack()
        tk.Button(root, text="Agregar Hecho", command=self.agregar_hecho).pack()

        # Ejecutar motor
        tk.Button(root, text="Ejecutar Reglas", command=self.ejecutar).pack()

        # Mostrar salida
        tk.Label(root, text="Salida:").pack()
        self.txt_salida = scrolledtext.ScrolledText(root, width=60, height=15)
        self.txt_salida.pack()

    def cargar_reglas(self):
        reglas = self.txt_reglas.get("1.0", tk.END).strip()
        if reglas:
            try:
                self.engine.cargar_reglas(reglas)
                messagebox.showinfo("Éxito", "Reglas cargadas correctamente")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def agregar_hecho(self):
        hecho = self.hecho_entry.get().strip()
        if hecho:
            try:
                self.engine.agregar_hecho(hecho)
                self.hecho_entry.delete(0, tk.END)
                self.mostrar_estado()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def ejecutar(self):
        try:
            self.engine.ejecutar()
            self.mostrar_estado()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_estado(self):
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, "Hechos actuales:\n")
        for hecho in self.engine.listar_hechos():
            self.txt_salida.insert(tk.END, f"  {hecho}\n")

        self.txt_salida.insert(tk.END, "\nReglas cargadas:\n")
        for regla in self.engine.listar_reglas():
            self.txt_salida.insert(tk.END, f"  {regla}\n")

