#!/usr/bin/env python3
"""
Demostración simple del Sistema Experto CLIPS
Muestra cómo funciona el nuevo sistema con assert en lugar de printout
"""

def demo_simple():
    """Demostración simple del sistema experto"""
    print("🚀 DEMOSTRACIÓN DEL SISTEMA EXPERTO CLIPS")
    print("=" * 50)
    
    try:
        from sistema_experto import SistemaExperto
        
        # Crear sistema experto
        print("1️⃣ Creando sistema experto...")
        sistema = SistemaExperto()
        print("✅ Sistema creado correctamente")
        
        # Mostrar reglas disponibles
        reglas = sistema.listar_reglas_disponibles()
        print(f"\n2️⃣ Reglas disponibles: {len(reglas)}")
        for i, regla in enumerate(reglas, 1):
            print(f"   {i}. {regla}")
        
        # Insertar hechos financieros
        print("\n3️⃣ Insertando hechos financieros...")
        sistema.insertar_hechos(
            ingresos=3000,
            ahorro=150,      # 5% de ingresos (menos del 10%)
            gastos=2500,
            deudas=1500,     # 50% de ingresos (más del 40%)
            ocio=1000        # 40% de gastos (más del 30%)
        )
        
        # Mostrar hechos insertados
        hechos = sistema.listar_hechos_actuales()
        print(f"✅ Hechos insertados: {len(hechos)}")
        for hecho in hechos:
            print(f"   - {hecho}")
        
        # Ejecutar inferencia
        print("\n4️⃣ Ejecutando inferencia...")
        sistema.ejecutar_inferencia()
        print("✅ Inferencia ejecutada")
        
        # Mostrar hechos después de la inferencia
        hechos_finales = sistema.listar_hechos_actuales()
        hechos_mensaje = [h for h in hechos_finales if "(mensaje" in h]
        print(f"\n5️⃣ Hechos de mensaje generados: {len(hechos_mensaje)}")
        for hecho in hechos_mensaje:
            print(f"   - {hecho}")
        
        # Obtener resultado procesado
        print("\n6️⃣ Resultado final procesado:")
        resultado = sistema.obtener_resultado()
        print(resultado)
        
        # Mostrar estado completo
        print("\n7️⃣ Estado completo del sistema:")
        estado = sistema.obtener_estado_completo()
        print(f"   - Total de hechos: {estado['hechos_count']}")
        print(f"   - Total de reglas: {estado['reglas_count']}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de que el módulo clips esté instalado")
        return False
    except Exception as e:
        print(f"❌ Error durante la demostración: {e}")
        return False


def demo_reglas_personalizadas():
    """Demostración con reglas personalizadas"""
    print("\n" + "=" * 50)
    print("🎯 DEMOSTRACIÓN CON REGLAS PERSONALIZADAS")
    print("=" * 50)
    
    try:
        from sistema_experto import SistemaExperto
        
        # Reglas personalizadas
        reglas_especiales = """
        (defrule reglaSituacionCritica
            (ahorro-bajo)
            (deuda-alta)
            (ocio-excesivo)
            =>
            (assert (mensaje "🚨 SITUACIÓN CRÍTICA: Múltiples problemas financieros detectados.")))
        
        (defrule reglaPlanAccion
            (situacion-critica)
            =>
            (assert (mensaje "📋 PLAN DE ACCIÓN: 1) Reduce gastos 2) Paga deudas 3) Aumenta ahorro")))
        """
        
        # Crear sistema con reglas personalizadas
        print("1️⃣ Creando sistema con reglas personalizadas...")
        sistema = SistemaExperto()
        sistema.cargar_reglas(reglas_especiales)
        print("✅ Reglas personalizadas cargadas")
        
        # Insertar hechos críticos
        print("\n2️⃣ Insertando hechos críticos...")
        sistema.insertar_hechos(
            ingresos=2000,
            ahorro=50,       # 2.5% de ingresos
            gastos=1800,
            deudas=1200,     # 60% de ingresos
            ocio=800         # 44% de gastos
        )
        
        # Agregar hecho adicional para situación crítica
        sistema.sistema.assert_string("(situacion-critica)")
        
        # Ejecutar inferencia
        print("3️⃣ Ejecutando inferencia...")
        sistema.ejecutar_inferencia()
        
        # Mostrar resultado
        print("\n4️⃣ Resultado con reglas personalizadas:")
        resultado = sistema.obtener_resultado()
        print(resultado)
        
        return True
        
    except Exception as e:
        print(f"❌ Error en reglas personalizadas: {e}")
        return False


if __name__ == "__main__":
    print("🎬 INICIANDO DEMOSTRACIÓN COMPLETA")
    
    # Ejecutar demostraciones
    demo1_ok = demo_simple()
    demo2_ok = demo_reglas_personalizadas()
    
    print("\n" + "=" * 50)
    if demo1_ok and demo2_ok:
        print("🎉 ¡DEMOSTRACIÓN COMPLETADA EXITOSAMENTE!")
        print("\n💡 RESUMEN DE LO QUE APRENDISTE:")
        print("   ✅ Las reglas usan 'assert' para crear hechos de mensaje")
        print("   ✅ Los mensajes se procesan automáticamente desde los hechos")
        print("   ✅ El sistema es más modular y fácil de extender")
        print("   ✅ Puedes crear reglas personalizadas fácilmente")
        
        print("\n🚀 PRÓXIMOS PASOS:")
        print("   1. Ejecuta: python ejemplo_uso.py (para más ejemplos)")
        print("   2. Ejecuta: python prueba_refactorizada.py (para la GUI)")
        print("   3. Crea tus propias reglas usando assert")
        
    else:
        print("❌ Algunas demostraciones fallaron")
        print("   Revisa los errores anteriores")
    
    print("\n📚 Para más información, consulta: README_SISTEMA_EXPERTO.md")
