#!/usr/bin/env python3
"""
Pruebas para el Sistema Difuso Financiero
=========================================

Este archivo contiene pruebas unitarias para verificar el correcto
funcionamiento del sistema difuso financiero.

Autor: Sistema Experto Financiero
Fecha: 2024
"""

import sys
import os
import unittest

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from fuzzy_system import SistemaDifusoFinanciero
    FUZZY_AVAILABLE = True
except ImportError:
    FUZZY_AVAILABLE = False
    print("⚠️  scikit-fuzzy no disponible. Las pruebas del sistema difuso se omitirán.")


@unittest.skipUnless(FUZZY_AVAILABLE, "scikit-fuzzy no disponible")
class TestSistemaDifusoFinanciero(unittest.TestCase):
    """Pruebas para la clase SistemaDifusoFinanciero"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.sistema = SistemaDifusoFinanciero()
    
    def test_creacion_sistema(self):
        """Prueba que el sistema se cree correctamente"""
        self.assertIsNotNone(self.sistema)
        self.assertTrue(hasattr(self.sistema, 'ahorro_mensual'))
        self.assertTrue(hasattr(self.sistema, 'riesgo_inversion'))
        self.assertTrue(hasattr(self.sistema, 'nivel_inversion'))
    
    def test_variables_entrada(self):
        """Prueba que las variables de entrada estén configuradas correctamente"""
        # Verificar ahorro mensual
        self.assertEqual(self.sistema.ahorro_mensual.universe.min(), 0)
        self.assertEqual(self.sistema.ahorro_mensual.universe.max(), 1000)
        
        # Verificar riesgo de inversión
        self.assertEqual(self.sistema.riesgo_inversion.universe.min(), 0)
        self.assertEqual(self.sistema.riesgo_inversion.universe.max(), 10)
        
        # Verificar nivel de inversión
        self.assertEqual(self.sistema.nivel_inversion.universe.min(), 0)
        self.assertEqual(self.sistema.nivel_inversion.universe.max(), 50)
    
    def test_conjuntos_difusos(self):
        """Prueba que los conjuntos difusos estén definidos"""
        # Verificar conjuntos de ahorro mensual
        self.assertIn('bajo', self.sistema.ahorro_mensual.terms)
        self.assertIn('medio', self.sistema.ahorro_mensual.terms)
        self.assertIn('alto', self.sistema.ahorro_mensual.terms)
        
        # Verificar conjuntos de riesgo
        self.assertIn('bajo', self.sistema.riesgo_inversion.terms)
        self.assertIn('moderado', self.sistema.riesgo_inversion.terms)
        self.assertIn('alto', self.sistema.riesgo_inversion.terms)
        
        # Verificar conjuntos de nivel de inversión
        self.assertIn('conservadora', self.sistema.nivel_inversion.terms)
        self.assertIn('moderada', self.sistema.nivel_inversion.terms)
        self.assertIn('agresiva', self.sistema.nivel_inversion.terms)
    
    def test_evaluacion_mamdani_valores_validos(self):
        """Prueba la evaluación Mamdani con valores válidos"""
        # Caso conservador: ahorro bajo, riesgo alto
        resultado = self.sistema.evaluar_mamdani(200, 8)
        
        self.assertNotIn('error', resultado)
        self.assertEqual(resultado['metodo'], 'Mamdani')
        self.assertEqual(resultado['ahorro_entrada'], 200)
        self.assertEqual(resultado['riesgo_entrada'], 8)
        self.assertIn('nivel_inversion', resultado)
        self.assertIn('etiqueta', resultado)
        self.assertGreaterEqual(resultado['nivel_inversion'], 0)
        self.assertLessEqual(resultado['nivel_inversion'], 50)
    
    def test_evaluacion_tsk_valores_validos(self):
        """Prueba la evaluación TSK con valores válidos"""
        # Caso moderado: ahorro medio, riesgo moderado
        resultado = self.sistema.evaluar_tsk(500, 5)
        
        self.assertNotIn('error', resultado)
        self.assertEqual(resultado['metodo'], 'TSK')
        self.assertEqual(resultado['ahorro_entrada'], 500)
        self.assertEqual(resultado['riesgo_entrada'], 5)
        self.assertIn('nivel_inversion', resultado)
        self.assertIn('etiqueta', resultado)
        self.assertGreaterEqual(resultado['nivel_inversion'], 0)
        self.assertLessEqual(resultado['nivel_inversion'], 50)
    
    def test_evaluacion_ambos_metodos(self):
        """Prueba la evaluación con ambos métodos"""
        resultado = self.sistema.evaluar_ambos_metodos(700, 3)
        
        self.assertIn('entradas', resultado)
        self.assertIn('resultados', resultado)
        self.assertIn('comparacion', resultado)
        
        self.assertEqual(resultado['entradas']['ahorro_mensual'], 700)
        self.assertEqual(resultado['entradas']['riesgo_inversion'], 3)
        
        self.assertIn('mamdani', resultado['resultados'])
        self.assertIn('tsk', resultado['resultados'])
        
        self.assertIn('diferencia', resultado['comparacion'])
        self.assertGreaterEqual(resultado['comparacion']['diferencia'], 0)
    
    def test_validacion_rangos_ahorro(self):
        """Prueba la validación de rangos para ahorro mensual"""
        # Valor fuera de rango (negativo)
        resultado = self.sistema.evaluar_mamdani(-100, 5)
        self.assertIn('error', resultado)
        
        # Valor fuera de rango (muy alto)
        resultado = self.sistema.evaluar_mamdani(1500, 5)
        self.assertIn('error', resultado)
        
        # Valores válidos en los límites
        resultado = self.sistema.evaluar_mamdani(0, 5)
        self.assertNotIn('error', resultado)
        
        resultado = self.sistema.evaluar_mamdani(1000, 5)
        self.assertNotIn('error', resultado)
    
    def test_validacion_rangos_riesgo(self):
        """Prueba la validación de rangos para riesgo de inversión"""
        # Valor fuera de rango (negativo)
        resultado = self.sistema.evaluar_mamdani(500, -1)
        self.assertIn('error', resultado)
        
        # Valor fuera de rango (muy alto)
        resultado = self.sistema.evaluar_mamdani(500, 15)
        self.assertIn('error', resultado)
        
        # Valores válidos en los límites
        resultado = self.sistema.evaluar_mamdani(500, 0)
        self.assertNotIn('error', resultado)
        
        resultado = self.sistema.evaluar_mamdani(500, 10)
        self.assertNotIn('error', resultado)
    
    def test_determinacion_etiquetas(self):
        """Prueba la determinación correcta de etiquetas lingüísticas"""
        # Casos de prueba para diferentes rangos
        casos_prueba = [
            (5, "Conservadora"),    # 0-20%
            (15, "Conservadora"),   # 0-20%
            (25, "Moderada"),       # 15-35%
            (35, "Moderada"),       # 15-35%
            (40, "Agresiva"),       # 30-50%
            (45, "Agresiva")        # 30-50%
        ]
        
        for valor, etiqueta_esperada in casos_prueba:
            etiqueta_obtenida = self.sistema._determinar_etiqueta(valor)
            self.assertEqual(etiqueta_obtenida, etiqueta_esperada, 
                           f"Valor {valor} debería ser {etiqueta_esperada}")
    
    def test_consistencia_entre_metodos(self):
        """Prueba que ambos métodos produzcan resultados consistentes"""
        # Casos de prueba
        casos_prueba = [
            (100, 9),   # Bajo ahorro, alto riesgo
            (500, 5),   # Ahorro medio, riesgo moderado
            (800, 2),   # Ahorro alto, riesgo bajo
        ]
        
        for ahorro, riesgo in casos_prueba:
            resultado = self.sistema.evaluar_ambos_metodos(ahorro, riesgo)
            
            # Verificar que ambos métodos produzcan resultados
            self.assertNotIn('error', resultado['resultados']['mamdani'])
            self.assertNotIn('error', resultado['resultados']['tsk'])
            
            # Verificar que las etiquetas sean consistentes
            etiqueta_mamdani = resultado['resultados']['mamdani']['etiqueta']
            etiqueta_tsk = resultado['resultados']['tsk']['etiqueta']
            
            # Las etiquetas deberían ser iguales para casos claros
            self.assertEqual(etiqueta_mamdani, etiqueta_tsk)
    
    def test_info_sistema(self):
        """Prueba que la información del sistema sea correcta"""
        info = self.sistema.obtener_info_sistema()
        
        self.assertEqual(info['nombre'], 'Sistema Difuso Financiero')
        self.assertIn('variables_entrada', info)
        self.assertIn('variable_salida', info)
        self.assertIn('reglas', info)
        self.assertIn('metodos_inferencia', info)
        
        # Verificar variables de entrada
        self.assertIn('ahorro_mensual', info['variables_entrada'])
        self.assertIn('riesgo_inversion', info['variables_entrada'])
        
        # Verificar variable de salida
        self.assertIn('nivel_inversion', info['variable_salida'])
        
        # Verificar reglas
        self.assertEqual(len(info['reglas']), 3)
        
        # Verificar métodos
        self.assertIn('Mamdani', info['metodos_inferencia'])
        self.assertIn('TSK', info['metodos_inferencia'])


class TestSistemaDifusoSinDependencias(unittest.TestCase):
    """Pruebas que se ejecutan incluso sin scikit-fuzzy"""
    
    def test_importacion_sin_dependencias(self):
        """Prueba que el sistema maneje correctamente la falta de dependencias"""
        if not FUZZY_AVAILABLE:
            with self.assertRaises(ImportError):
                from fuzzy_system import SistemaDifusoFinanciero


def ejecutar_pruebas():
    """Ejecuta todas las pruebas"""
    print("🧪 EJECUTANDO PRUEBAS DEL SISTEMA DIFUSO FINANCIERO")
    print("=" * 60)
    
    if not FUZZY_AVAILABLE:
        print("⚠️  scikit-fuzzy no disponible")
        print("💡 Instala las dependencias: pip install -r requirements.txt")
        print("📚 Solo se ejecutarán pruebas básicas de importación")
    
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSistemaDifusoFinanciero)
    
    # Agregar pruebas sin dependencias
    suite.addTests(loader.loadTestsFromTestCase(TestSistemaDifusoSinDependencias))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen
    print("\n📊 RESUMEN DE PRUEBAS")
    print("=" * 30)
    print(f"Pruebas ejecutadas: {result.testsRun}")
    print(f"Fallos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ Todas las pruebas pasaron exitosamente")
        return 0
    else:
        print("❌ Algunas pruebas fallaron")
        return 1


if __name__ == "__main__":
    exit_code = ejecutar_pruebas()
    sys.exit(exit_code)
