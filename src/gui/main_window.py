import tkinter as tk
from tkinter import ttk, messagebox
from sistema_experto import SistemaExperto
from fuzzy_system import SistemaDifusoFinanciero

class SistemaFinancieroGUI:
    """Interfaz gráfica principal que integra el sistema experto CLIPS y el sistema difuso"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Sistema Financiero Inteligente - CLIPS + Lógica Difusa")
        self.root.geometry("900x700")
        
        # Crear instancias de ambos sistemas
        self.sistema_experto = SistemaExperto()
        self.sistema_difuso = SistemaDifusoFinanciero()
        
        # Configurar interfaz con pestañas
        self._crear_interfaz()
    
    def _crear_interfaz(self):
        """Crea la interfaz gráfica con pestañas"""
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Pestaña 1: Sistema Experto CLIPS
        self.tab_experto = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_experto, text="🧠 Sistema Experto CLIPS")
        self._crear_tab_experto()
        
        # Pestaña 2: Sistema Difuso
        self.tab_difuso = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_difuso, text="🌊 Sistema Difuso")
        self._crear_tab_difuso()
        
        # Pestaña 3: Información del Sistema
        self.tab_info = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_info, text="ℹ️ Información")
        self._crear_tab_info()
    
    def _crear_tab_experto(self):
        """Crea la pestaña del sistema experto CLIPS"""
        # Frame principal con scroll
        main_frame = ttk.Frame(self.tab_experto)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        titulo = ttk.Label(main_frame, text="🧠 SISTEMA EXPERTO EN FINANZAS PERSONALES", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Frame para entradas y resultados
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True)
        
        # Frame izquierdo (entradas)
        frame_inputs = ttk.LabelFrame(content_frame, text="📥 Datos de Entrada", padding="10")
        frame_inputs.pack(side="left", fill="y", padx=(0, 10))
        
        # Campos de entrada
        self.entries_experto = {}
        campos = [
            ("ingresos", "👉 Ingresos mensuales (USD):"),
            ("ahorro", "👉 Ahorro actual (USD):"),
            ("gastos", "👉 Gastos mensuales (USD):"),
            ("deudas", "👉 Deudas actuales (USD):"),
            ("ocio", "👉 Gasto en ocio (USD):")
        ]
        
        for i, (key, label) in enumerate(campos):
            ttk.Label(frame_inputs, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = ttk.Entry(frame_inputs, width=20)
            entry.grid(row=i, column=1, pady=5, padx=(10, 0))
            self.entries_experto[key] = entry
        
        # Botón de consulta
        btn_consultar = ttk.Button(frame_inputs, text="🔍 Consultar Sistema Experto", 
                                  command=self._consultar_experto, style="Accent.TButton")
        btn_consultar.grid(row=len(campos), column=0, columnspan=2, pady=20)
        
        # Frame derecho (resultados)
        frame_output = ttk.LabelFrame(content_frame, text="📊 Recomendaciones del Sistema Experto", padding="10")
        frame_output.pack(side="right", fill="both", expand=True)
        
        # Texto con scroll
        text_frame = ttk.Frame(frame_output)
        text_frame.pack(fill="both", expand=True)
        
        self.text_resultado_experto = tk.Text(text_frame, wrap="word", font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.text_resultado_experto.yview)
        self.text_resultado_experto.configure(yscrollcommand=scrollbar.set)
        
        self.text_resultado_experto.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botón para mostrar estado del sistema
        btn_estado = ttk.Button(frame_output, text="📋 Mostrar Estado del Sistema", 
                               command=self._mostrar_estado_sistema)
        btn_estado.pack(pady=10)
    
    def _crear_tab_difuso(self):
        """Crea la pestaña del sistema difuso"""
        # Frame principal
        main_frame = ttk.Frame(self.tab_difuso)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        titulo = ttk.Label(main_frame, text="🌊 SISTEMA DIFUSO FINANCIERO", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Frame para entradas y resultados
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True)
        
        # Frame izquierdo (entradas)
        frame_inputs = ttk.LabelFrame(content_frame, text="📥 Variables de Entrada", padding="10")
        frame_inputs.pack(side="left", fill="y", padx=(0, 10))
        
        # Campo ahorro mensual
        ttk.Label(frame_inputs, text="💰 Ahorro mensual (0-1000 USD):").pack(anchor="w", pady=5)
        self.entry_ahorro = ttk.Entry(frame_inputs, width=20)
        self.entry_ahorro.pack(pady=5)
        self.entry_ahorro.insert(0, "700")  # Valor por defecto
        
        # Campo riesgo de inversión
        ttk.Label(frame_inputs, text="⚠️ Riesgo de inversión (0-10):").pack(anchor="w", pady=5)
        self.entry_riesgo = ttk.Entry(frame_inputs, width=20)
        self.entry_riesgo.pack(pady=5)
        self.entry_riesgo.insert(0, "3")  # Valor por defecto
        
        # Botones de evaluación
        btn_frame = ttk.Frame(frame_inputs)
        btn_frame.pack(pady=20)
        
        btn_mamdani = ttk.Button(btn_frame, text="🌊 Evaluar", 
                                command=self._evaluar_mamdani, style="Accent.TButton")
        btn_mamdani.pack(pady=5)
        
        # btn_tsk = ttk.Button(btn_frame, text="⚡ Evaluar TSK", 
        #                     command=self._evaluar_tsk, style="Accent.TButton")
        # btn_tsk.pack(pady=5)
        
        # btn_ambos = ttk.Button(btn_frame, text="🔄 Evaluar Ambos", 
        #                       command=self._evaluar_ambos, style="Accent.TButton")
        # btn_ambos.pack(pady=5)
        
        # Botón para visualizar conjuntos difusos
        btn_visualizar = ttk.Button(frame_inputs, text="📊 Ver Conjuntos Difusos", 
                                   command=self._visualizar_conjuntos)
        btn_visualizar.pack(pady=10)
        
        # Frame derecho (resultados)
        frame_output = ttk.LabelFrame(content_frame, text="📈 Resultados del Sistema Difuso", padding="10")
        frame_output.pack(side="right", fill="both", expand=True)
        
        # Texto con scroll
        text_frame = ttk.Frame(frame_output)
        text_frame.pack(fill="both", expand=True)
        
        self.text_resultado_difuso = tk.Text(text_frame, wrap="word", font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.text_resultado_difuso.yview)
        self.text_resultado_difuso.configure(yscrollcommand=scrollbar.set)
        
        self.text_resultado_difuso.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mostrar información del sistema difuso
        info_text = """
🌊 SISTEMA DIFUSO FINANCIERO

📥 Variables de Entrada:
• Ahorro mensual: 0-1000 USD (conjuntos triangulares)
• Riesgo de inversión: 0-10 (conjuntos gaussianos)

📤 Variable de Salida:
• Nivel de inversión: 0-50% (conjuntos triangulares)

🧠 Reglas de Inferencia:
• R1: Ahorro bajo ∨ Riesgo alto → Inversión conservadora
• R2: Ahorro medio ∧ Riesgo moderado → Inversión moderada
• R3: Ahorro alto ∧ Riesgo bajo → Inversión agresiva
• R4: Si ahorro es medio ∧ riesgo es bajo → inversión es moderada
• R5: Si ahorro es alto ∧ riesgo es moderado → inversión es agresiva

⚙️ Métodos de Inferencia:
• Mamdani con defuzzificación por centroide
• TSK con singletones y media de pesos
        """
        
        self.text_resultado_difuso.insert(tk.END, info_text)
        self.text_resultado_difuso.config(state="disabled")
    
    def _crear_tab_info(self):
        """Crea la pestaña de información del sistema"""
        # Frame principal con scroll
        main_frame = ttk.Frame(self.tab_info)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        titulo = ttk.Label(main_frame, text="ℹ️ INFORMACIÓN DEL SISTEMA FINANCIERO INTELIGENTE", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Texto con scroll
        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill="both", expand=True)
        
        text_info = tk.Text(text_frame, wrap="word", font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_info.yview)
        text_info.configure(yscrollcommand=scrollbar.set)
        
        text_info.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Información del sistema
        info_text = """
💰 SISTEMA FINANCIERO INTELIGENTE
================================

Este sistema integra dos enfoques de inteligencia artificial para 
proporcionar recomendaciones financieras personalizadas:

🧠 SISTEMA EXPERTO CLIPS (Pestaña 1)
====================================
• Basado en reglas lógicas y hechos
• Utiliza el motor de inferencia CLIPS
• Analiza múltiples variables financieras
• Proporciona recomendaciones basadas en reglas predefinidas

🌊 SISTEMA DIFUSO (Pestaña 2)
==============================
• Basado en lógica difusa (fuzzy logic)
• Utiliza scikit-fuzzy para inferencia
• Maneja incertidumbre y grados de pertenencia
• Implementa métodos Mamdani y TSK

📊 VARIABLES DEL SISTEMA DIFUSO
===============================

Entradas:
• Ahorro mensual: 0-1000 USD
  - Bajo: (0, 0, 400) - Triangular
  - Medio: (200, 500, 800) - Triangular  
  - Alto: (600, 1000, 1000) - Triangular

• Riesgo de inversión: 0-10
  - Bajo: μ=0, σ=1.5 - Gaussiano
  - Moderado: μ=5, σ=1.5 - Gaussiano
  - Alto: μ=10, σ=1.5 - Gaussiano

Salida:
• Nivel de inversión: 0-50%
  - Conservadora: (0, 10, 20) - Triangular
  - Moderada: (15, 25, 35) - Triangular
  - Agresiva: (30, 40, 50) - Triangular

🧠 REGLAS DE INFERENCIA DIFUSA
==============================

R1: Si ahorro es bajo ∨ riesgo es alto → inversión es conservadora
R2: Si ahorro es medio ∧ riesgo es moderado → inversión es moderada
R3: Si ahorro es alto ∧ riesgo es bajo → inversión es agresiva
R4: Si ahorro es medio ∧ riesgo es bajo → inversión es moderada
R5: Si ahorro es alto ∧ riesgo es moderado → inversión es agresiva

⚙️ MÉTODOS DE INFERENCIA
=========================

MAMDANI:
• Usa conjuntos difusos para la salida
• Defuzzificación por centroide
• Resultado más suave y continuo

TSK (Takagi-Sugeno-Kang):
• Usa singletones (valores fijos)
• Agregación por media de pesos
• Resultado más directo y computacionalmente eficiente

🎯 CASOS DE USO
===============

• Planificación financiera personal
• Evaluación de perfiles de riesgo
• Recomendaciones de inversión
• Análisis de capacidad de ahorro
• Educación financiera

📚 TECNOLOGÍAS UTILIZADAS
==========================

• Python 3.8+
• CLIPS (motor de inferencia)
• scikit-fuzzy (lógica difusa)
• tkinter (interfaz gráfica)
• numpy (cálculos numéricos)
• matplotlib (visualización)

🔧 INSTALACIÓN Y USO
====================

1. Instalar dependencias: pip install -r requirements.txt
2. Ejecutar: python main.py
3. Usar pestañas para alternar entre sistemas
4. Ingresar datos y evaluar resultados

📖 DOCUMENTACIÓN
================

• Cada función incluye documentación detallada
• Comentarios explicativos en el código
• Ejemplos de uso incluidos
• Visualización de conjuntos difusos disponible
        """
        
        text_info.insert(tk.END, info_text)
        text_info.config(state="disabled")
    
    def _consultar_experto(self):
        """Ejecuta la consulta del sistema experto CLIPS"""
        try:
            # Obtener valores de los campos
            valores = {}
            for key, entry in self.entries_experto.items():
                valor = float(entry.get())
                valores[key] = valor
            
            # Insertar hechos en el sistema experto
            self.sistema_experto.insertar_hechos(**valores)
            
            # Ejecutar inferencia
            self.sistema_experto.ejecutar_inferencia()
            
            # Obtener y mostrar resultado
            resultado = self.sistema_experto.obtener_resultado()
            
            # Mostrar en el cuadro de texto
            self.text_resultado_experto.config(state="normal")
            self.text_resultado_experto.delete("1.0", tk.END)
            self.text_resultado_experto.insert(tk.END, resultado)
            self.text_resultado_experto.config(state="disabled")
            
        except ValueError:
            messagebox.showerror("Error", "❌ Error: Ingresa solo números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {str(e)}")
    
    def _evaluar_mamdani(self):
        """Evalúa el sistema difuso usando el método Mamdani"""
        try:
            ahorro = float(self.entry_ahorro.get())
            riesgo = float(self.entry_riesgo.get())
            
            resultado = self.sistema_difuso.evaluar_mamdani(ahorro, riesgo)
            
            if 'error' in resultado:
                messagebox.showerror("Error", resultado['error'])
                return
            
            # Mostrar resultado
            self.text_resultado_difuso.config(state="normal")
            self.text_resultado_difuso.delete("1.0", tk.END)
            
            resultado_texto = f"""
🌊 RESULTADO MÉTODO DIFUSO
============================

📥 Entradas:
• Ahorro mensual: {resultado['ahorro_entrada']} USD
• Riesgo de inversión: {resultado['riesgo_entrada']}

📤 Resultado:
• Nivel de inversión: {resultado['nivel_inversion']}%
• Etiqueta lingüística: {resultado['etiqueta']}
• Método: {resultado['metodo']}

💡 Interpretación:
El sistema recomienda una estrategia de inversión {resultado['etiqueta'].lower()}
con un nivel del {resultado['nivel_inversion']}% de los ingresos.
            """
            
            self.text_resultado_difuso.insert(tk.END, resultado_texto)
            self.text_resultado_difuso.config(state="disabled")
            
        except ValueError:
            messagebox.showerror("Error", "❌ Error: Ingresa solo números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {str(e)}")
    
    def _evaluar_tsk(self):
        """Evalúa el sistema difuso usando el método TSK"""
        try:
            ahorro = float(self.entry_ahorro.get())
            riesgo = float(self.entry_riesgo.get())
            
            resultado = self.sistema_difuso.evaluar_tsk(ahorro, riesgo)
            
            if 'error' in resultado:
                messagebox.showerror("Error", resultado['error'])
                return
            
            # Mostrar resultado
            self.text_resultado_difuso.config(state="normal")
            self.text_resultado_difuso.delete("1.0", tk.END)
            
            resultado_texto = f"""
⚡ RESULTADO MÉTODO TSK
========================

📥 Entradas:
• Ahorro mensual: {resultado['ahorro_entrada']} USD
• Riesgo de inversión: {resultado['riesgo_entrada']}

📤 Resultado:
• Nivel de inversión: {resultado['nivel_inversion']}%
• Etiqueta lingüística: {resultado['etiqueta']}
• Método: {resultado['metodo']}

💡 Interpretación:
El sistema recomienda una estrategia de inversión {resultado['etiqueta'].lower()}
con un nivel del {resultado['nivel_inversion']}% de los ingresos.
            """
            
            self.text_resultado_difuso.insert(tk.END, resultado_texto)
            self.text_resultado_difuso.config(state="disabled")
            
        except ValueError:
            messagebox.showerror("Error", "❌ Error: Ingresa solo números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {str(e)}")
    
    def _evaluar_ambos(self):
        """Evalúa el sistema difuso usando ambos métodos"""
        try:
            ahorro = float(self.entry_ahorro.get())
            riesgo = float(self.entry_riesgo.get())
            
            resultado = self.sistema_difuso.evaluar_ambos_metodos(ahorro, riesgo)
            
            # Mostrar resultado
            self.text_resultado_difuso.config(state="normal")
            self.text_resultado_difuso.delete("1.0", tk.END)
            
            resultado_texto = f"""
🔄 COMPARACIÓN AMBOS MÉTODOS
=============================

📥 Entradas:
• Ahorro mensual: {resultado['entradas']['ahorro_mensual']} USD
• Riesgo de inversión: {resultado['entradas']['riesgo_inversion']}

📤 Resultados:

🌊 MAMDANI:
• Nivel de inversión: {resultado['resultados']['mamdani']['nivel_inversion']}%
• Etiqueta: {resultado['resultados']['mamdani']['etiqueta']}

⚡ TSK:
• Nivel de inversión: {resultado['resultados']['tsk']['nivel_inversion']}%
• Etiqueta: {resultado['resultados']['tsk']['etiqueta']}

🔍 Comparación:
• Diferencia entre métodos: {resultado['comparacion']['diferencia']:.2f}%

💡 Análisis:
Ambos métodos proporcionan recomendaciones similares,
validando la consistencia del sistema difuso.
            """
            
            self.text_resultado_difuso.insert(tk.END, resultado_texto)
            self.text_resultado_difuso.config(state="disabled")
            
        except ValueError:
            messagebox.showerror("Error", "❌ Error: Ingresa solo números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {str(e)}")
    
    def _visualizar_conjuntos(self):
        """Visualiza los conjuntos difusos del sistema"""
        try:
            self._evaluar_mamdani()
            self.sistema_difuso.visualizar_conjuntos_difusos()
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error al visualizar: {str(e)}")
    
    def _mostrar_estado_sistema(self):
        """Muestra el estado completo del sistema experto"""
        estado = self.sistema_experto.obtener_estado_completo()
        
        # Crear ventana emergente
        ventana_estado = tk.Toplevel(self.root)
        ventana_estado.title("Estado del Sistema Experto CLIPS")
        ventana_estado.geometry("700x500")
        
        # Texto con scroll
        text_estado = tk.Text(ventana_estado, wrap="word", font=("Consolas", 10))
        text_estado.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Mostrar información del estado
        text_estado.insert(tk.END, "📊 ESTADO DEL SISTEMA EXPERTO CLIPS\n")
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
    app = SistemaFinancieroGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
