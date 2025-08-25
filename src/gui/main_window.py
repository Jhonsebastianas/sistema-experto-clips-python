import tkinter as tk
from tkinter import ttk
from sistema_experto import SistemaExperto

class SistemaExpertoGUI:
    """Interfaz gráfica para el sistema experto de finanzas personales"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Sistema Experto de Finanzas Personales")
        
        # Crear instancia del sistema experto
        self.sistema = SistemaExperto()
        
        # Configurar interfaz
        self._crear_interfaz()
    
    def _crear_interfaz(self):
        """Crea la interfaz gráfica"""
        # Frame izquierdo (entradas)
        frame_inputs = ttk.Frame(self.root, padding="10")
        frame_inputs.grid(row=0, column=0, sticky="nsew")
        
        # Campos de entrada
        self.entries = {}
        campos = [
            ("ingresos", "👉 Ingresos mensuales:"),
            ("ahorro", "👉 Ahorro actual:"),
            ("gastos", "👉 Gastos mensuales:"),
            ("deudas", "👉 Deudas actuales:"),
            ("ocio", "👉 Gasto en ocio:")
        ]
        
        for i, (key, label) in enumerate(campos):
            ttk.Label(frame_inputs, text=label).grid(row=i, column=0, sticky="w")
            entry = ttk.Entry(frame_inputs)
            entry.grid(row=i, column=1, pady=5)
            self.entries[key] = entry
        
        # Botón de consulta
        btn_consultar = ttk.Button(frame_inputs, text="Consultar", command=self._consultar)
        btn_consultar.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        # Frame derecho (resultados)
        frame_output = ttk.Frame(self.root, padding="10")
        frame_output.grid(row=0, column=1, sticky="nsew")
        
        ttk.Label(frame_output, text="📊 Recomendaciones:").pack(anchor="w")
        self.text_resultado = tk.Text(frame_output, width=50, height=15, wrap="word")
        self.text_resultado.pack(fill="both", expand=True)
        
        # Botón para mostrar estado del sistema
        btn_estado = ttk.Button(frame_output, text="Mostrar Estado del Sistema", 
                               command=self._mostrar_estado_sistema)
        btn_estado.pack(pady=5)
    
    def _consultar(self):
        """Ejecuta la consulta del sistema experto"""
        try:
            # Obtener valores de los campos
            valores = {}
            for key, entry in self.entries.items():
                valor = float(entry.get())
                valores[key] = valor
            
            # Insertar hechos en el sistema experto
            self.sistema.insertar_hechos(**valores)
            
            # Ejecutar inferencia
            self.sistema.ejecutar_inferencia()
            
            # Obtener y mostrar resultado
            resultado = self.sistema.obtener_resultado()
            
            # Mostrar en el cuadro de texto
            self.text_resultado.delete("1.0", tk.END)
            self.text_resultado.insert(tk.END, resultado)
            
        except ValueError:
            self.text_resultado.delete("1.0", tk.END)
            self.text_resultado.insert(tk.END, "❌ Error: Ingresa solo números válidos.")
        except Exception as e:
            self.text_resultado.delete("1.0", tk.END)
            self.text_resultado.insert(tk.END, f"❌ Error: {str(e)}")
    
    def _mostrar_estado_sistema(self):
        """Muestra el estado completo del sistema experto"""
        estado = self.sistema.obtener_estado_completo()
        
        # Crear ventana emergente
        ventana_estado = tk.Toplevel(self.root)
        ventana_estado.title("Estado del Sistema Experto")
        ventana_estado.geometry("600x400")
        
        # Texto con scroll
        text_estado = tk.Text(ventana_estado, wrap="word")
        text_estado.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Mostrar información del estado
        text_estado.insert(tk.END, "📊 ESTADO DEL SISTEMA EXPERTO\n")
        text_estado.insert(tk.END, "=" * 50 + "\n\n")
        
        text_estado.insert(tk.END, f"🔢 Estadísticas:\n")
        text_estado.insert(tk.END, f"  - Reglas disponibles: {estado['reglas_count']}\n")
        text_estado.insert(tk.END, f"  - Hechos activos: {estado['hechos_count']}\n\n")
        
        text_estado.insert(tk.END, f"📜 Reglas del sistema:\n")
        for i, regla in enumerate(estado['reglas'], 1):
            text_estado.insert(tk.END, f"  {i}. {regla}\n")
        
        text_estado.insert(tk.END, f"\n📌 Hechos activos:\n")
        if estado['hechos']:
            for i, hecho in enumerate(estado['hechos'], 1):
                text_estado.insert(tk.END, f"  {i}. {hecho}\n")
        else:
            text_estado.insert(tk.END, "  No hay hechos activos\n")
        
        text_estado.insert(tk.END, f"\n💬 Último resultado:\n")
        text_estado.insert(tk.END, f"  {estado['resultado']}")
        
        # Deshabilitar edición
        text_estado.config(state="disabled")


def main():
    """Función principal"""
    root = tk.Tk()
    app = SistemaExpertoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
