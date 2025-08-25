"""
Sistema Experto CLIPS para Finanzas Personales
==============================================

Este paquete contiene la implementación principal del sistema experto
basado en CLIPS para análisis financiero personal.
"""

__version__ = "2.0.0"
__author__ = "Sistema Experto CLIPS Team"
__description__ = "Sistema experto para finanzas personales usando CLIPS"

from .sistema_experto import SistemaExperto, cargar_reglas, insertar_hechos, ejecutar_inferencia, obtener_resultado

__all__ = [
    'SistemaExperto',
    'cargar_reglas', 
    'insertar_hechos', 
    'ejecutar_inferencia', 
    'obtener_resultado'
]
