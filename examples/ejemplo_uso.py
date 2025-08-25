#!/usr/bin/env python3
"""
Ejemplo de uso del módulo sistema_experto.py
Demuestra cómo usar el sistema experto CLIPS desde otros archivos Python
"""

from sistema_experto import (
    SistemaExperto, 
    cargar_reglas, 
    insertar_hechos, 
    ejecutar_inferencia, 
    obtener_resultado
)

def ejemplo_basico():
    """Ejemplo básico de uso del sistema experto"""
    print("=== EJEMPLO BÁSICO ===")
    
    # Crear instancia del sistema experto
    sistema = SistemaExperto()
    
    # Insertar hechos financieros
    insertar_hechos(
        sistema,
        ingresos=5000,
        ahorro=300,      # Solo 6% de ingresos (menos del 10%)
        gastos=3000,
        deudas=2500,     # 50% de ingresos (más del 40%)
        ocio=1200        # 40% de gastos (más del 30%)
    )
    
    # Ejecutar inferencia
    ejecutar_inferencia(sistema)
    
    # Obtener y mostrar resultado
    resultado = obtener_resultado(sistema)
    print("📊 Recomendaciones del sistema experto:")
    print(resultado)
    
    # Mostrar estado del sistema
    estado = sistema.obtener_estado_completo()
    print(f"\n📈 Estado del sistema:")
    print(f"  - Hechos activos: {estado['hechos_count']}")
    print(f"  - Reglas disponibles: {estado['reglas_count']}")
    print(f"  - Hechos: {estado['hechos']}")


def ejemplo_con_reglas_personalizadas():
    """Ejemplo usando reglas personalizadas adicionales con assert"""
    print("\n=== EJEMPLO CON REGLAS PERSONALIZADAS ===")
    
    # Reglas adicionales personalizadas usando assert
    reglas_adicionales = """
    (defrule reglaAhorroObjetivo
        (ahorro-bajo)
        (gastos-alto)
        =>
        (assert (mensaje "🚨 CRÍTICO: Ahorras poco y gastas mucho. Revisa tu presupuesto.")))
    
    (defrule reglaDeudaEmergencia
        (deuda-alta)
        (sin-emergencia)
        =>
        (assert (mensaje "⚠️ ALERTA: Deudas altas sin fondo de emergencia. Prioriza pagar deudas.")))
    
    (defrule reglaGastosAltos
        (gastos-alto)
        =>
        (assert (mensaje "📊 Tus gastos representan más del 80% de tus ingresos. Considera reducir gastos.")))
    """
    
    # Crear sistema con reglas adicionales
    sistema = cargar_reglas(reglas_adicionales)
    
    # Insertar hechos que activen las nuevas reglas
    insertar_hechos(
        sistema,
        ingresos=4000,
        ahorro=200,      # 5% de ingresos
        gastos=3500,     # 87.5% de ingresos (gastos altos)
        deudas=2000,     # 50% de ingresos
        ocio=800
    )
    
    # Agregar hecho adicional para gastos altos
    sistema.sistema.assert_string("(gastos-alto)")
    
    # Ejecutar inferencia
    ejecutar_inferencia(sistema)
    
    # Mostrar resultado
    resultado = obtener_resultado(sistema)
    print("📊 Recomendaciones con reglas personalizadas:")
    print(resultado)


def ejemplo_programatico():
    """Ejemplo de uso programático sin interfaz gráfica"""
    print("\n=== EJEMPLO PROGRAMÁTICO ===")
    
    # Crear sistema
    sistema = SistemaExperto()
    
    # Simular diferentes escenarios financieros
    escenarios = [
        {
            'nombre': 'Escenario Conservador',
            'datos': {'ingresos': 6000, 'ahorro': 1200, 'gastos': 4000, 'deudas': 1000, 'ocio': 800}
        },
        {
            'nombre': 'Escenario Riesgoso',
            'datos': {'ingresos': 3000, 'ahorro': 100, 'gastos': 2800, 'deudas': 2000, 'ocio': 1000}
        },
        {
            'nombre': 'Escenario Equilibrado',
            'datos': {'ingresos': 5000, 'ahorro': 1000, 'gastos': 3500, 'deudas': 800, 'ocio': 600}
        }
    ]
    
    for escenario in escenarios:
        print(f"\n🔍 Analizando: {escenario['nombre']}")
        
        # Insertar hechos del escenario
        insertar_hechos(sistema, **escenario['datos'])
        
        # Ejecutar inferencia
        ejecutar_inferencia(sistema)
        
        # Obtener resultado
        resultado = obtener_resultado(sistema)
        print(f"Resultado: {resultado}")
        
        # Reiniciar para el siguiente escenario
        sistema.reiniciar_sistema()


def ejemplo_estado_sistema():
    """Ejemplo de monitoreo del estado del sistema"""
    print("\n=== EJEMPLO MONITOREO DE ESTADO ===")
    
    sistema = SistemaExperto()
    
    # Mostrar estado inicial
    estado_inicial = sistema.obtener_estado_completo()
    print("📊 Estado inicial del sistema:")
    print(f"  - Reglas disponibles: {estado_inicial['reglas_count']}")
    print(f"  - Hechos activos: {estado_inicial['hechos_count']}")
    
    # Insertar algunos hechos
    insertar_hechos(sistema, ingresos=5000, ahorro=400, gastos=3000, deudas=1500, ocio=600)
    
    # Mostrar estado después de insertar hechos
    estado_con_hechos = sistema.obtener_estado_completo()
    print(f"\n📊 Estado después de insertar hechos:")
    print(f"  - Hechos activos: {estado_con_hechos['hechos_count']}")
    print(f"  - Hechos: {estado_con_hechos['hechos']}")
    
    # Ejecutar inferencia
    ejecutar_inferencia(sistema)
    
    # Mostrar estado final
    estado_final = sistema.obtener_estado_completo()
    print(f"\n📊 Estado final después de inferencia:")
    print(f"  - Resultado: {estado_final['resultado']}")


def ejemplo_reglas_avanzadas():
    """Ejemplo con reglas más complejas y hechos anidados"""
    print("\n=== EJEMPLO REGLAS AVANZADAS ===")
    
    # Reglas más complejas que crean hechos intermedios
    reglas_avanzadas = """
    (defrule evaluar_riesgo_financiero
        (ahorro-bajo)
        (deuda-alta)
        =>
        (assert (riesgo-alto "Riesgo financiero alto detectado")))
    
    (defrule recomendacion_riesgo_alto
        (riesgo-alto ?mensaje)
        =>
        (assert (mensaje "🚨 ALERTA: Tu situación financiera presenta alto riesgo.")))
    
    (defrule recomendacion_riesgo_alto_detalle
        (riesgo-alto ?mensaje)
        =>
        (assert (mensaje "💡 Recomendación: Prioriza pagar deudas y aumentar ahorro.")))
    """
    
    # Crear sistema con reglas avanzadas
    sistema = cargar_reglas(reglas_avanzadas)
    
    # Insertar hechos que activen las reglas de riesgo
    insertar_hechos(
        sistema,
        ingresos=2000,
        ahorro=50,       # 2.5% de ingresos (muy bajo)
        gastos=1800,
        deudas=1200,     # 60% de ingresos (muy alto)
        ocio=500
    )
    
    # Ejecutar inferencia
    ejecutar_inferencia(sistema)
    
    # Mostrar resultado
    resultado = obtener_resultado(sistema)
    print("📊 Recomendaciones con reglas avanzadas:")
    print(resultado)
    
    # Mostrar todos los hechos generados
    hechos = sistema.listar_hechos_actuales()
    print(f"\n🔍 Hechos generados por las reglas:")
    for hecho in hechos:
        print(f"  - {hecho}")


if __name__ == "__main__":
    print("🚀 DEMOSTRACIÓN DEL SISTEMA EXPERTO CLIPS")
    print("=" * 50)
    
    try:
        # Ejecutar todos los ejemplos
        ejemplo_basico()
        ejemplo_con_reglas_personalizadas()
        ejemplo_programatico()
        ejemplo_estado_sistema()
        ejemplo_reglas_avanzadas()
        
        print("\n✅ Todos los ejemplos ejecutados correctamente!")
        print("\n💡 Ahora puedes usar este módulo en otros archivos:")
        print("""
from sistema_experto import SistemaExperto

sistema = SistemaExperto()
sistema.insertar_hechos(ingresos=5000, ahorro=300, gastos=3000, deudas=2500, ocio=1200)
sistema.ejecutar_inferencia()
resultado = sistema.obtener_resultado()
print(resultado)
        """)
        
        print("\n🔧 Las reglas ahora usan 'assert' en lugar de 'printout':")
        print("""
(defrule reglaEjemplo
    (condicion)
    =>
    (assert (mensaje "Tu mensaje aquí")))
        """)
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        print("Asegúrate de que el módulo clips esté instalado: pip install clips")
