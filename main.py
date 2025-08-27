#!/usr/bin/env python3
"""
Sistema Financiero Inteligente - Punto de Entrada Principal
==========================================================

Este archivo es el punto de entrada principal para ejecutar
el sistema financiero inteligente que integra:
- Sistema Experto CLIPS para finanzas personales
- Sistema Difuso para recomendaciones de inversión
"""

import sys
import os

# Agregar el directorio src al path para importar el módulo
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Función principal"""
    try:
        from gui.main_window import SistemaFinancieroGUI
        import tkinter as tk
        
        # Crear y ejecutar la interfaz gráfica
        root = tk.Tk()
        app = SistemaFinancieroGUI(root)
        root.mainloop()
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de que las dependencias estén instaladas: pip install -r requirements.txt")
        print("📁 Verifica que la estructura del proyecto sea correcta")
        return 1
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
