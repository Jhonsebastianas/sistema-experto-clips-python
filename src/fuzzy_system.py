"""
Sistema Difuso Financiero
==========================

Este módulo implementa un sistema de inferencia difusa para recomendaciones
de inversión basado en el ahorro mensual y el perfil de riesgo del usuario.

Utiliza scikit-fuzzy para implementar:
- Variables lingüísticas con conjuntos difusos
- Reglas de inferencia difusa
- Métodos de inferencia Mamdani y TSK
- Defuzzificación para obtener resultados numéricos

Autor: Sistema Experto Financiero
Fecha: 2024
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from typing import Dict, Tuple, Any
import matplotlib.pyplot as plt


class SistemaDifusoFinanciero:
    """
    Sistema de inferencia difusa para recomendaciones de inversión financiera.
    
    Este sistema toma como entrada:
    - Ahorro mensual (0-1000 USD)
    - Riesgo de inversión (0-10)
    
    Y produce como salida:
    - Nivel de inversión recomendada (0-50%)
    
    Implementa tanto el método de inferencia Mamdani como TSK.
    """
    
    def __init__(self):
        """Inicializa el sistema difuso financiero"""
        self._configurar_variables()
        self._configurar_reglas()
        self._crear_sistemas_control()
        
    def _configurar_variables(self):
        """
        Configura las variables lingüísticas del sistema difuso.
        
        Variables de entrada:
        - ahorro_mensual: Rango [0, 1000] USD
        - riesgo_inversion: Rango [0, 10]
        
        Variable de salida:
        - nivel_inversion: Rango [0, 50] %
        """
        
        # Variable de entrada: Ahorro mensual (0-1000 USD)
        # Conjuntos difusos triangulares según especificación
        self.ahorro_mensual = ctrl.Antecedent(np.arange(0, 1001, 1), 'ahorro_mensual')
        
        # Definir conjuntos difusos triangulares
        # Bajo: (0, 0, 400) - Triángulo que va de 0 a 400
        self.ahorro_mensual['bajo'] = fuzz.trimf(self.ahorro_mensual.universe, [0, 0, 400])
        
        # Medio: (200, 500, 800) - Triángulo centrado en 500
        self.ahorro_mensual['medio'] = fuzz.trimf(self.ahorro_mensual.universe, [200, 500, 800])
        
        # Alto: (600, 1000, 1000) - Triángulo que va de 600 a 1000
        self.ahorro_mensual['alto'] = fuzz.trimf(self.ahorro_mensual.universe, [600, 1000, 1000])
        
        # Variable de entrada: Riesgo de inversión (0-10)
        # Conjuntos difusos gaussianos según especificación
        self.riesgo_inversion = ctrl.Antecedent(np.arange(0, 11, 0.1), 'riesgo_inversion')
        
        # Definir conjuntos difusos trapezoidales (cuadrados)
        # Bajo: empieza en 0, máximo hasta 3
        self.riesgo_inversion['bajo'] = fuzz.trapmf(self.riesgo_inversion.universe, [0, 0, 2, 3])

        # Moderado: centrado en 5, ancho entre 2 y 8
        self.riesgo_inversion['moderado'] = fuzz.trapmf(self.riesgo_inversion.universe, [2, 4, 6, 8])

        # Alto: empieza desde 7 y llega a 10
        self.riesgo_inversion['alto'] = fuzz.trapmf(self.riesgo_inversion.universe, [7, 8, 10, 10])

        
        # Variable de salida: Nivel de inversión (0-50%)
        # Conjuntos difusos triangulares según especificación
        self.nivel_inversion = ctrl.Consequent(np.arange(0, 51, 0.1), 'nivel_inversion')
        
        # Definir conjuntos difusos triangulares
        # Conservadora: (0, 10, 20) - Triángulo centrado en 10%
        self.nivel_inversion['conservadora'] = fuzz.trimf(self.nivel_inversion.universe, [0, 10, 20])
        
        # Moderada: (15, 25, 35) - Triángulo centrado en 25%
        self.nivel_inversion['moderada'] = fuzz.trimf(self.nivel_inversion.universe, [15, 25, 35])
        
        # Agresiva: (30, 40, 50) - Triángulo centrado en 40%
        self.nivel_inversion['agresiva'] = fuzz.trimf(self.nivel_inversion.universe, [30, 40, 50])
    
    def _configurar_reglas(self):
        """
        Configura las reglas de inferencia difusa del sistema.
        
        Reglas implementadas:
        - R1: Si ahorro es bajo ∨ riesgo es alto → inversión es conservadora
        - R2: Si ahorro es medio ∧ riesgo es moderado → inversión es moderada  
        - R3: Si ahorro es alto ∧ riesgo es bajo → inversión es agresiva
        - R4: Si ahorro es medio ∧ riesgo es bajo → inversión es moderada
        - R5: Si ahorro es alto ∧ riesgo es moderado → inversión es agresiva
        """
        
        # Regla 1: Ahorro bajo O riesgo alto → Inversión conservadora
        # Usamos OR (máximo) para la unión de condiciones
        self.regla1 = ctrl.Rule(
            (self.ahorro_mensual['bajo'] | self.riesgo_inversion['alto']),
            self.nivel_inversion['conservadora']
        )
        
        # Regla 2: Ahorro medio Y riesgo moderado → Inversión moderada
        # Usamos AND (mínimo) para la intersección de condiciones
        self.regla2 = ctrl.Rule(
            (self.ahorro_mensual['medio'] & self.riesgo_inversion['moderado']),
            self.nivel_inversion['moderada']
        )
        
        # Regla 3: Ahorro alto Y riesgo bajo → Inversión agresiva
        # Usamos AND (mínimo) para la intersección de condiciones
        self.regla3 = ctrl.Rule(
            (self.ahorro_mensual['alto'] & self.riesgo_inversion['bajo']),
            self.nivel_inversion['agresiva']
        )

        # Regla 4: Ahorro medio Y riesgo bajo → Inversión moderada
        self.regla4 = ctrl.Rule(
            (self.ahorro_mensual['medio'] & self.riesgo_inversion['bajo']),
            self.nivel_inversion['moderada']
        )

        # Regla 5: Ahorro alto Y riesgo moderado → Inversión agresiva
        self.regla5 = ctrl.Rule(
            (self.ahorro_mensual['alto'] & self.riesgo_inversion['moderado']),
            self.nivel_inversion['agresiva']
        )
    
    def _crear_sistemas_control(self):
        """
        Crea los sistemas de control para los métodos Mamdani y TSK.
        
        - Sistema Mamdani: Usa conjuntos difusos para la salida
        - Sistema TSK: Usa singletones (valores numéricos fijos)
        """
        
        # Sistema Mamdani: Conjuntos difusos de salida
        self.sistema_mamdani = ctrl.ControlSystem([
            self.regla1, self.regla2, self.regla3, self.regla4, self.regla5
        ])
        
        # Simulador para Mamdani
        self.simulador_mamdani = ctrl.ControlSystemSimulation(self.sistema_mamdani)
        
        # Sistema TSK: Singletones como salida
        # Definir singletones en el valor máximo de cada conjunto de salida
        self.nivel_inversion_tsk = ctrl.Consequent(np.arange(0, 51, 0.1), 'nivel_inversion_tsk')
        
        # Singletones: valores fijos en los picos de los conjuntos difusos
        self.nivel_inversion_tsk['conservadora'] = fuzz.trimf(self.nivel_inversion_tsk.universe, [10, 10, 10])
        self.nivel_inversion_tsk['moderada'] = fuzz.trimf(self.nivel_inversion_tsk.universe, [25, 25, 25])
        self.nivel_inversion_tsk['agresiva'] = fuzz.trimf(self.nivel_inversion_tsk.universe, [40, 40, 40])
        
        # Reglas TSK con singletones
        self.regla1_tsk = ctrl.Rule(
            (self.ahorro_mensual['bajo'] | self.riesgo_inversion['alto']),
            self.nivel_inversion_tsk['conservadora']
        )
        
        self.regla2_tsk = ctrl.Rule(
            (self.ahorro_mensual['medio'] & self.riesgo_inversion['moderado']),
            self.nivel_inversion_tsk['moderada']
        )
        
        self.regla3_tsk = ctrl.Rule(
            (self.ahorro_mensual['alto'] & self.riesgo_inversion['bajo']),
            self.nivel_inversion_tsk['agresiva']
        )

        # Reglas TSK con singletones
        self.regla4_tsk = ctrl.Rule(
            (self.ahorro_mensual['medio'] & self.riesgo_inversion['bajo']),
            self.nivel_inversion_tsk['moderada']
        )

        self.regla5_tsk = ctrl.Rule(
            (self.ahorro_mensual['alto'] & self.riesgo_inversion['moderado']),
            self.nivel_inversion_tsk['agresiva']
        )
        
        # Sistema TSK
        self.sistema_tsk = ctrl.ControlSystem([
            self.regla1_tsk, self.regla2_tsk, self.regla3_tsk, self.regla4_tsk, self.regla5_tsk
        ])
        
        # Simulador para TSK
        self.simulador_tsk = ctrl.ControlSystemSimulation(self.sistema_tsk)
    
    def evaluar_mamdani(self, ahorro: float, riesgo: float) -> Dict[str, Any]:
        """
        Evalúa el sistema usando el método de inferencia Mamdani.
        
        Args:
            ahorro: Ahorro mensual en USD (0-1000)
            riesgo: Nivel de riesgo de inversión (0-10)
            
        Returns:
            Dict con el resultado numérico y la etiqueta lingüística
        """
        try:
            # Validar rangos de entrada
            if not (0 <= ahorro <= 1000):
                raise ValueError("Ahorro debe estar entre 0 y 1000 USD")
            if not (0 <= riesgo <= 10):
                raise ValueError("Riesgo debe estar entre 0 y 10")
            
            # Configurar entradas
            self.simulador_mamdani.input['ahorro_mensual'] = ahorro
            self.simulador_mamdani.input['riesgo_inversion'] = riesgo
            
            # Ejecutar inferencia
            self.simulador_mamdani.compute()
            
            # Obtener resultado
            resultado_numerico = self.simulador_mamdani.output['nivel_inversion']
            
            # Determinar etiqueta lingüística
            etiqueta = self._determinar_etiqueta(resultado_numerico)
            
            return {
                'metodo': 'Difuso',
                'ahorro_entrada': ahorro,
                'riesgo_entrada': riesgo,
                'nivel_inversion': round(resultado_numerico, 2),
                'etiqueta': etiqueta,
                'unidad': '%'
            }
            
        except Exception as e:
            return {
                'error': f"Error en evaluación Mamdani: {str(e)}",
                'metodo': 'Mamdani'
            }
    
    def evaluar_tsk(self, ahorro: float, riesgo: float) -> Dict[str, Any]:
        """
        Evalúa el sistema usando el método de inferencia TSK.
        
        Args:
            ahorro: Ahorro mensual en USD (0-1000)
            riesgo: Nivel de riesgo de inversión (0-10)
            
        Returns:
            Dict con el resultado numérico y la etiqueta lingüística
        """
        try:
            # Validar rangos de entrada
            if not (0 <= ahorro <= 1000):
                raise ValueError("Ahorro debe estar entre 0 y 1000 USD")
            if not (0 <= riesgo <= 10):
                raise ValueError("Riesgo debe estar entre 0 y 10")
            
            # Configurar entradas
            self.simulador_tsk.input['ahorro_mensual'] = ahorro
            self.simulador_tsk.input['riesgo_inversion'] = riesgo
            
            # Ejecutar inferencia
            self.simulador_tsk.compute()
            
            # Obtener resultado
            resultado_numerico = self.simulador_tsk.output['nivel_inversion_tsk']
            
            # Determinar etiqueta lingüística
            etiqueta = self._determinar_etiqueta(resultado_numerico)
            
            return {
                'metodo': 'TSK',
                'ahorro_entrada': ahorro,
                'riesgo_entrada': riesgo,
                'nivel_inversion': round(resultado_numerico, 2),
                'etiqueta': etiqueta,
                'unidad': '%'
            }
            
        except Exception as e:
            return {
                'error': f"Error en evaluación TSK: {str(e)}",
                'metodo': 'TSK'
            }
    
    def _determinar_etiqueta(self, valor: float) -> str:
        """
        Determina la etiqueta lingüística basada en el valor numérico.
        
        Args:
            valor: Valor numérico del nivel de inversión (0-50)
            
        Returns:
            String con la etiqueta lingüística
        """
        if valor <= 20:
            return "Conservadora"
        elif valor <= 35:
            return "Moderada"
        else:
            return "Agresiva"
    
    def evaluar_ambos_metodos(self, ahorro: float, riesgo: float) -> Dict[str, Any]:
        """
        Evalúa el sistema usando ambos métodos (Mamdani y TSK).
        
        Args:
            ahorro: Ahorro mensual en USD (0-1000)
            riesgo: Nivel de riesgo de inversión (0-10)
            
        Returns:
            Dict con los resultados de ambos métodos
        """
        resultado_mamdani = self.evaluar_mamdani(ahorro, riesgo)
        resultado_tsk = self.evaluar_tsk(ahorro, riesgo)
        
        return {
            'entradas': {
                'ahorro_mensual': ahorro,
                'riesgo_inversion': riesgo
            },
            'resultados': {
                'mamdani': resultado_mamdani,
                'tsk': resultado_tsk
            },
            'comparacion': {
                'diferencia': abs(resultado_mamdani.get('nivel_inversion', 0) - 
                                resultado_tsk.get('nivel_inversion', 0))
            }
        }
    
    def visualizar_conjuntos_difusos(self, guardar_imagen: bool = False) -> None:
        """
        Visualiza los conjuntos difusos del sistema.
        
        Args:
            guardar_imagen: Si es True, guarda la imagen en lugar de mostrarla
        """
        try:
            # Crear figura con subplots
            
            # Ahorro mensual
            self.ahorro_mensual.view()
            
            # Riesgo de inversión
            self.riesgo_inversion.view()
            
            # Nivel de inversión
            #self.nivel_inversion.view(ax=axes[2])
            self.nivel_inversion.view(sim=self.simulador_mamdani)
            
            plt.tight_layout()
            
            if guardar_imagen:
                plt.savefig('conjuntos_difusos_financieros.png', dpi=300, bbox_inches='tight')
                print("Imagen guardada como 'conjuntos_difusos_financieros.png'")
            else:
                plt.show()
                
        except Exception as e:
            print(f"Error al visualizar conjuntos difusos: {e}")
    
    def obtener_info_sistema(self) -> Dict[str, Any]:
        """
        Retorna información general del sistema difuso.
        
        Returns:
            Dict con información del sistema
        """
        return {
            'nombre': 'Sistema Difuso Financiero',
            'descripcion': 'Sistema de inferencia difusa para recomendaciones de inversión',
            'variables_entrada': {
                'ahorro_mensual': {
                    'rango': [0, 1000],
                    'unidad': 'USD',
                    'conjuntos': ['bajo', 'medio', 'alto'],
                    'tipo': 'Triangulares'
                },
                'riesgo_inversion': {
                    'rango': [0, 10],
                    'unidad': 'Escala',
                    'conjuntos': ['bajo', 'moderado', 'alto'],
                    'tipo': 'Gaussianos'
                }
            },
            'variable_salida': {
                'nivel_inversion': {
                    'rango': [0, 50],
                    'unidad': '%',
                    'conjuntos': ['conservadora', 'moderada', 'agresiva'],
                    'tipo': 'Triangulares'
                }
            },
            'reglas': [
                'Si ahorro es bajo ∨ riesgo es alto → inversión es conservadora',
                'Si ahorro es medio ∧ riesgo es moderado → inversión es moderada',
                'Si ahorro es alto ∧ riesgo es bajo → inversión es agresiva'
            ],
            'metodos_inferencia': ['Mamdani', 'TSK'],
            'defuzzificacion': 'Centroide (Mamdani), Media de pesos (TSK)'
        }


# Función de ejemplo para demostración
def ejemplo_uso():
    """
    Función de ejemplo que demuestra el uso del sistema difuso financiero.
    """
    print("🎯 SISTEMA DIFUSO FINANCIERO - EJEMPLO DE USO")
    print("=" * 60)
    
    # Crear instancia del sistema
    sistema = SistemaDifusoFinanciero()
    
    # Mostrar información del sistema
    info = sistema.obtener_info_sistema()
    print(f"\n📊 {info['nombre']}")
    print(f"📝 {info['descripcion']}")
    
    # Ejemplo de evaluación
    print("\n🧪 EVALUACIÓN DE EJEMPLO:")
    print("Entradas: Ahorro = 700 USD, Riesgo = 3")
    
    resultado = sistema.evaluar_ambos_metodos(700, 3)
    
    print(f"\n📈 Resultado Mamdani: {resultado['resultados']['mamdani']['nivel_inversion']}% "
          f"({resultado['resultados']['mamdani']['etiqueta']})")
    print(f"📈 Resultado TSK: {resultado['resultados']['tsk']['nivel_inversion']}% "
          f"({resultado['resultados']['tsk']['etiqueta']})")
    print(f"🔍 Diferencia entre métodos: {resultado['comparacion']['diferencia']:.2f}%")
    
    return sistema


if __name__ == "__main__":
    # Ejecutar ejemplo si se ejecuta directamente
    sistema_ejemplo = ejemplo_uso()
