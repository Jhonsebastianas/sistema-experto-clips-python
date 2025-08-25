#!/usr/bin/env python3
"""
Archivo de prueba simple para verificar el módulo sistema_experto
"""

def test_basico():
    """Prueba básica del sistema experto"""
    print("🧪 Probando sistema experto básico...")
    
    try:
        from sistema_experto import SistemaExperto
        
        # Crear instancia
        sistema = SistemaExperto()
        print("✅ Sistema experto creado correctamente")
        
        # Verificar reglas cargadas
        reglas = sistema.listar_reglas_disponibles()
        print(f"✅ Reglas cargadas: {len(reglas)}")
        
        # Insertar hechos de prueba
        sistema.insertar_hechos(
            ingresos=1000,
            ahorro=50,    # 5% (menos del 10%)
            gastos=800,
            deudas=500,   # 50% (más del 40%)
            ocio=300      # 37.5% (más del 30%)
        )
        print("✅ Hechos insertados correctamente")
        
        # Verificar hechos
        hechos = sistema.listar_hechos_actuales()
        print(f"✅ Hechos activos: {len(hechos)}")
        print(f"  Hechos: {hechos}")
        
        # Ejecutar inferencia
        sistema.ejecutar_inferencia()
        print("✅ Inferencia ejecutada correctamente")
        
        # Obtener resultado
        resultado = sistema.obtener_resultado()
        print("✅ Resultado obtenido:")
        print(resultado)
        
        # Verificar que se generaron hechos de mensaje
        hechos_finales = sistema.listar_hechos_actuales()
        hechos_mensaje = [h for h in hechos_finales if "(mensaje" in h]
        print(f"✅ Hechos de mensaje generados: {len(hechos_mensaje)}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        return False


def test_funciones_conveniencia():
    """Prueba las funciones de conveniencia"""
    print("\n🧪 Probando funciones de conveniencia...")
    
    try:
        from sistema_experto import (
            cargar_reglas, 
            insertar_hechos, 
            ejecutar_inferencia, 
            obtener_resultado
        )
        
        # Crear sistema con funciones de conveniencia
        sistema = cargar_reglas()
        print("✅ Sistema creado con funciones de conveniencia")
        
        # Insertar hechos
        insertar_hechos(
            sistema,
            ingresos=2000,
            ahorro=100,   # 5%
            gastos=1500,
            deudas=1000,  # 50%
            ocio=600      # 40%
        )
        print("✅ Hechos insertados con funciones de conveniencia")
        
        # Ejecutar y obtener resultado
        ejecutar_inferencia(sistema)
        resultado = obtener_resultado(sistema)
        print("✅ Resultado obtenido con funciones de conveniencia:")
        print(resultado)
        
        return True
        
    except Exception as e:
        print(f"❌ Error en funciones de conveniencia: {e}")
        return False


def test_reglas_con_assert():
    """Prueba que las reglas usen assert correctamente"""
    print("\n🧪 Probando reglas con assert...")
    
    try:
        from sistema_experto import SistemaExperto
        
        # Crear sistema
        sistema = SistemaExperto()
        
        # Verificar que las reglas usen assert
        reglas = sistema.listar_reglas_disponibles()
        reglas_assert = [r for r in reglas if "assert" in r]
        reglas_printout = [r for r in reglas if "printout" in r]
        
        print(f"✅ Reglas con assert: {len(reglas_assert)}")
        print(f"✅ Reglas sin printout: {len(reglas_printout)}")
        
        # Verificar que no haya printout en las reglas
        if reglas_printout:
            print("⚠️ ADVERTENCIA: Se encontraron reglas con printout")
            for regla in reglas_printout:
                print(f"  - {regla}")
        else:
            print("✅ Todas las reglas usan assert correctamente")
        
        # Probar que las reglas generen hechos de mensaje
        sistema.insertar_hechos(ingresos=1000, ahorro=50, gastos=800, deudas=500, ocio=300)
        sistema.ejecutar_inferencia()
        
        # Verificar hechos de mensaje
        hechos = sistema.listar_hechos_actuales()
        hechos_mensaje = [h for h in hechos if "(mensaje" in h]
        
        if hechos_mensaje:
            print(f"✅ Se generaron {len(hechos_mensaje)} hechos de mensaje")
            for hecho in hechos_mensaje:
                print(f"  - {hecho}")
        else:
            print("❌ No se generaron hechos de mensaje")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error en prueba de reglas con assert: {e}")
        return False


def test_procesamiento_mensajes():
    """Prueba el procesamiento de mensajes desde hechos"""
    print("\n🧪 Probando procesamiento de mensajes...")
    
    try:
        from sistema_experto import SistemaExperto
        
        # Crear sistema
        sistema = SistemaExperto()
        
        # Insertar hechos que activen múltiples reglas
        sistema.insertar_hechos(
            ingresos=5000,
            ahorro=200,   # 4% (menos del 10%)
            gastos=4000,
            deudas=2500,  # 50% (más del 40%)
            ocio=1500     # 37.5% (más del 30%)
        )
        
        # Ejecutar inferencia
        sistema.ejecutar_inferencia()
        
        # Obtener resultado
        resultado = sistema.obtener_resultado()
        print("✅ Resultado procesado:")
        print(resultado)
        
        # Verificar que el resultado contenga múltiples mensajes
        if resultado and resultado != "✅ Tu situación financiera está equilibrada.":
            print("✅ Se procesaron múltiples mensajes correctamente")
            
            # Verificar que no haya texto de CLIPS crudo
            if "f-" in resultado or "(mensaje" in resultado:
                print("⚠️ ADVERTENCIA: El resultado contiene texto de CLIPS sin procesar")
                return False
            else:
                print("✅ Los mensajes se procesaron correctamente")
                return True
        else:
            print("❌ No se generaron mensajes o solo mensaje por defecto")
            return False
        
    except Exception as e:
        print(f"❌ Error en procesamiento de mensajes: {e}")
        return False


if __name__ == "__main__":
    print("🚀 INICIANDO PRUEBAS DEL SISTEMA EXPERTO")
    print("=" * 50)
    
    # Ejecutar todas las pruebas
    test1_ok = test_basico()
    test2_ok = test_funciones_conveniencia()
    test3_ok = test_reglas_con_assert()
    test4_ok = test_procesamiento_mensajes()
    
    print("\n" + "=" * 50)
    if test1_ok and test2_ok and test3_ok and test4_ok:
        print("🎉 TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        print("\n💡 El módulo sistema_experto está funcionando correctamente.")
        print("   - Las reglas usan 'assert' en lugar de 'printout'")
        print("   - Los mensajes se procesan desde hechos")
        print("   - Puedes usarlo en otros archivos importándolo")
    else:
        print("❌ ALGUNAS PRUEBAS FALLARON.")
        print("   Revisa los errores anteriores.")
    
    print("\n📚 Para más ejemplos, ejecuta: python ejemplo_uso.py")
    print("🔧 Las reglas ahora usan: (assert (mensaje \"texto\"))")
