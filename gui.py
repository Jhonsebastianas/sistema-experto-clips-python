# gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox, Toplevel
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

        # Botones de control
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)

        tk.Button(frame_botones, text="Ejecutar Reglas", command=self.ejecutar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Reiniciar Hechos", command=self.reiniciar).grid(row=0, column=1, padx=5)

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
            self.mostrar_resultados_finales()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reiniciar(self):
        try:
            self.engine.reiniciar()
            self.mostrar_estado()
            messagebox.showinfo("Reiniciado", "Se han eliminado todos los hechos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_estado(self):
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, "Hechos:\n")
        for hecho in self.engine.listar_hechos():
            self.txt_salida.insert(tk.END, f"  {hecho}\n")

        self.txt_salida.insert(tk.END, "\nReglas:\n")
        for regla in self.engine.listar_reglas():
            self.txt_salida.insert(tk.END, f"  {regla}\n")

    def mostrar_resultados_finales(self):
        """Muestra los hechos y reglas en una ventana emergente final"""
        win = Toplevel(self.root)
        win.title("Resultados Finales")

        txt = scrolledtext.ScrolledText(win, width=70, height=20)
        txt.pack(padx=10, pady=10)

        txt.insert(tk.END, "📌 Hechos Finales:\n")
        for hecho in self.engine.listar_hechos():
            txt.insert(tk.END, f"  {hecho}\n")

        txt.insert(tk.END, "\n📜 Reglas Definidas:\n")
        for regla in self.engine.listar_reglas():
            txt.insert(tk.END, f"  {regla}\n")

        txt.config(state="disabled")