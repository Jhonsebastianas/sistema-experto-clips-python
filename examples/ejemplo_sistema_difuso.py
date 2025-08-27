#!/usr/bin/env python3
"""
Ejemplo de Uso del Sistema Difuso Financiero
============================================

Este archivo demuestra cómo usar el sistema difuso financiero
para obtener recomendaciones de inversión basadas en ahorro
mensual y perfil de riesgo.

Autor: Sistema Experto Financiero
Fecha: 2024
"""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def ejemplo_basico():
    """Ejemplo básico de uso del sistema difuso"""
    print("🎯 EJEMPLO BÁSICO - SISTEMA DIFUSO FINANCIERO")
    print("=" * 60)
    
    try:
        from fuzzy_system import SistemaDifusoFinanciero
        
        # Crear instancia del sistema
        sistema = SistemaDifusoFinanciero()
        
        # Mostrar información del sistema
        info = sistema.obtener_info_sistema()
        print(f"\n📊 {info['nombre']}")
        print(f"📝 {info['descripcion']}")
        
        # Ejemplo 1: Perfil conservador
        print("\n🧪 EJEMPLO 1: PERFIL CONSERVADOR")
        print("Entradas: Ahorro = 200 USD, Riesgo = 8")
        
        resultado1 = sistema.evaluar_ambos_metodos(200, 8)
        
        print(f"📈 Resultado Mamdani: {resultado1['resultados']['mamdani']['nivel_inversion']}% "
              f"({resultado1['resultados']['mamdani']['etiqueta']})")
        print(f"📈 Resultado TSK: {resultado1['resultados']['tsk']['nivel_inversion']}% "
              f"({resultado1['resultados']['tsk']['etiqueta']})")
        
        # Ejemplo 2: Perfil moderado
        print("\n🧪 EJEMPLO 2: PERFIL MODERADO")
        print("Entradas: Ahorro = 500 USD, Riesgo = 5")
        
        resultado2 = sistema.evaluar_ambos_metodos(500, 5)
        
        print(f"📈 Resultado Mamdani: {resultado2['resultados']['mamdani']['nivel_inversion']}% "
              f"({resultado2['resultados']['mamdani']['etiqueta']})")
        print(f"📈 Resultado TSK: {resultado2['resultados']['tsk']['nivel_inversion']}% "
              f"({resultado2['resultados']['tsk']['etiqueta']})")
        
        # Ejemplo 3: Perfil agresivo
        print("\n🧪 EJEMPLO 3: PERFIL AGRESIVO")
        print("Entradas: Ahorro = 800 USD, Riesgo = 2")
        
        resultado3 = sistema.evaluar_ambos_metodos(800, 2)
        
        print(f"📈 Resultado Mamdani: {resultado3['resultados']['mamdani']['nivel_inversion']}% "
              f"({resultado3['resultados']['mamdani']['etiqueta']})")
        print(f"📈 Resultado TSK: {resultado3['resultados']['tsk']['nivel_inversion']}% "
              f"({resultado3['resultados']['tsk']['etiqueta']})")
        
        return sistema
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de que scikit-fuzzy esté instalado: pip install scikit-fuzzy")
        return None
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        return None


def ejemplo_analisis_comparativo():
    """Ejemplo de análisis comparativo entre métodos"""
    print("\n🔄 ANÁLISIS COMPARATIVO ENTRE MÉTODOS")
    print("=" * 60)
    
    try:
        from fuzzy_system import SistemaDifusoFinanciero
        
        sistema = SistemaDifusoFinanciero()
        
        # Casos de prueba
        casos_prueba = [
            (100, 9, "Bajo ahorro, alto riesgo"),
            (300, 7, "Ahorro medio-bajo, riesgo alto"),
            (500, 5, "Ahorro medio, riesgo moderado"),
            (700, 3, "Ahorro alto, riesgo bajo"),
            (900, 1, "Ahorro muy alto, riesgo muy bajo")
        ]
        
        print(f"{'Caso':<30} {'Mamdani':<15} {'TSK':<15} {'Diferencia':<12}")
        print("-" * 75)
        
        for ahorro, riesgo, descripcion in casos_prueba:
            resultado = sistema.evaluar_ambos_metodos(ahorro, riesgo)
            
            mamdani_val = resultado['resultados']['mamdani']['nivel_inversion']
            tsk_val = resultado['resultados']['tsk']['nivel_inversion']
            diferencia = resultado['comparacion']['diferencia']
            
            print(f"{descripcion:<30} {mamdani_val:<15.2f} {tsk_val:<15.2f} {diferencia:<12.2f}")
        
        print("\n💡 Interpretación:")
        print("• Valores similares indican consistencia entre métodos")
        print("• Diferencias pequeñas son normales debido a diferentes enfoques")
        print("• Ambos métodos validan la lógica del sistema difuso")
        
    except Exception as e:
        print(f"❌ Error en análisis comparativo: {e}")


def ejemplo_visualizacion():
    """Ejemplo de visualización de conjuntos difusos"""
    print("\n📊 VISUALIZACIÓN DE CONJUNTOS DIFUSOS")
    print("=" * 60)
    
    try:
        from fuzzy_system import SistemaDifusoFinanciero
        
        sistema = SistemaDifusoFinanciero()
        
        print("🎨 Generando visualización de conjuntos difusos...")
        print("💡 Se abrirá una ventana con los gráficos")
        print("📁 También puedes guardar la imagen como 'conjuntos_difusos_financieros.png'")
        
        # Mostrar visualización
        sistema.visualizar_conjuntos_difusos()
        
        print("✅ Visualización completada")
        
    except Exception as e:
        print(f"❌ Error en visualización: {e}")


def main():
    """Función principal del ejemplo"""
    print("🚀 INICIANDO EJEMPLOS DEL SISTEMA DIFUSO FINANCIERO")
    print("=" * 70)
    
    # Ejemplo básico
    sistema = ejemplo_basico()
    
    if sistema:
        # Análisis comparativo
        ejemplo_analisis_comparativo()
        
        # Visualización (opcional)
        try:
            respuesta = input("\n¿Deseas ver la visualización de conjuntos difusos? (s/n): ")
            if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
                ejemplo_visualizacion()
        except KeyboardInterrupt:
            print("\n\n👋 Ejemplo interrumpido por el usuario")
        
        print("\n✅ Ejemplos completados exitosamente")
        print("💡 Puedes ejecutar la interfaz gráfica con: python main.py")
    else:
        print("\n❌ No se pudo completar los ejemplos")


if __name__ == "__main__":
    main()
