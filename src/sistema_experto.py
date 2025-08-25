import clips
import sys
import io
from typing import Dict, Any, Optional

class SistemaExperto:
    """
    Módulo centralizado para el sistema experto CLIPS de finanzas personales.
    Encapsula toda la lógica de reglas, hechos y inferencia.
    """
    
    def __init__(self):
        """Inicializa el sistema experto CLIPS"""
        self.sistema = clips.Environment()
        self.sistema.clear()
        self.resultado_capturado = ""
        self.router_captura = None
        self._configurar_router()
        self._cargar_reglas_financieras()
    
    def _configurar_router(self):
        """Configura un router personalizado para capturar la salida de printout"""
        class CapturaRouter(clips.Router):
            def __init__(self, sistema_experto):
                super().__init__("captura", ["stdout", "stderr"])
                self.sistema_experto = sistema_experto
            
            def query(self, logical_name):
                return True
            
            def print(self, logical_name, text):
                self.sistema_experto.resultado_capturado += text
        
        self.router_captura = CapturaRouter(self)
    
    def _cargar_reglas_financieras(self):
        """Carga las reglas predefinidas del sistema financiero usando assert en lugar de printout"""
        reglas = [
            """
            (defrule reglaAhorro
                (ahorro-bajo)
                =>
                (assert (mensajeAhorro)))
            """,
            """
            (defrule reglaDeuda
                (deuda-alta)
                =>
                (assert (mensajeDeuda)))
            """,
            """
            (defrule reglaEmergencia
                (sin-emergencia)
                =>
                (assert (mensajeEmergencia)))
            """,
            """
            (defrule reglaOcio
                (ocio-excesivo)
                =>
                (assert (mensajeOcio)))
            """,
            """
            (defrule reglaInversion
                (puede-invertir)
                =>
                (assert (mensajeInversion)))
            """
        ]
        
        for regla in reglas:
            self.sistema.build(regla)
    
    def cargar_reglas(self, reglas_str: str) -> bool:
        """
        Carga reglas adicionales desde un string
        
        Args:
            reglas_str: String con las reglas CLIPS a cargar
            
        Returns:
            bool: True si se cargaron correctamente, False en caso contrario
        """
        try:
            # Dividir por líneas y cargar cada regla
            for regla in reglas_str.split("\n"):
                regla = regla.strip()
                if regla and regla.startswith("(defrule"):
                    self.sistema.build(regla)
            return True
        except Exception as e:
            print(f"Error al cargar reglas: {e}")
            return False
    
    def insertar_hechos(self, **kwargs) -> None:
        """
        Inserta hechos dinámicamente basándose en los parámetros proporcionados
        
        Args:
            **kwargs: Parámetros con los valores financieros
                     (ingresos, ahorro, gastos, deudas, ocio)
        """
        # Limpiar hechos anteriores
        self.sistema.reset()
        self.resultado_capturado = ""
        
        # Extraer valores
        ingresos = kwargs.get('ingresos', 0)
        ahorro = kwargs.get('ahorro', 0)
        gastos = kwargs.get('gastos', 0)
        deudas = kwargs.get('deudas', 0)
        ocio = kwargs.get('ocio', 0)
        
        # Insertar hechos según condiciones
        if ahorro < ingresos * 0.10:
            self.sistema.assert_string("(ahorro-bajo)")
        
        if deudas > ingresos * 0.40:
            self.sistema.assert_string("(deuda-alta)")
        
        if ahorro < gastos * 3:
            self.sistema.assert_string("(sin-emergencia)")
        
        if ocio > gastos * 0.30:
            self.sistema.assert_string("(ocio-excesivo)")
        
        if ahorro >= ingresos * 0.15 and deudas < ingresos * 0.20:
            self.sistema.assert_string("(puede-invertir)")
    
    def ejecutar_inferencia(self) -> None:
        """Ejecuta el motor de inferencia CLIPS"""
        try:
            # Ejecutar el motor de inferencia
            self.sistema.run()
            
            # Procesar los hechos de mensaje generados
            self._procesar_mensajes()
            
        except Exception as e:
            self.resultado_capturado = f"Error en la inferencia: {e}"
    
    def _procesar_mensajes(self):
        """Procesa los hechos de mensaje generados por las reglas"""
        mensajes = []
        
        # Mapeo de hechos simbólicos a textos para UI
        mapa_mensajes = {
            'mensajeAhorro': "- Estas ahorrando menos del 10% de tus ingresos.\n",
            'mensajeDeuda': "- Tus deudas superan el 40% de tus ingresos. Reduce o renegocia.\n",
            'mensajeEmergencia': "- No tienes un fondo de emergencia de al menos 3 meses de gastos.\n",
            'mensajeOcio': "- Gastas mas del 30% de tus gastos en ocio. Intenta controlarlo.\n",
            'mensajeInversion': "- Estas en buena posición para considerar inversiones.\n"
        }
        
        # Buscar todos los hechos y traducir a mensajes
        for fact in self.sistema.facts():
            fact_str = str(fact)
            # 1) Compatibilidad: (mensaje "texto")
            if fact_str.startswith("f-") and "(mensaje" in fact_str and '"' in fact_str:
                try:
                    start = fact_str.find('"') + 1
                    end = fact_str.rfind('"')
                    if start > 0 and end > start:
                        mensajes.append(fact_str[start:end])
                        continue
                except:
                    pass
            
            # 2) Nuevos hechos simbólicos sin parámetros
            # Formatos posibles del string del hecho, ejemplos:
            #   f-3     (mensajeAhorro)
            #   f-4     (mensajeDeuda)
            #   f-5     (mensajeEmergencia)
            #   f-6     (mensajeOcio)
            #   f-7     (mensajeInversion)
            for clave, texto in mapa_mensajes.items():
                patron = f"({clave})"
                if patron in fact_str:
                    mensajes.append(texto)
                    break
        
        # Unir todos los mensajes
        if mensajes:
            self.resultado_capturado = "\n".join(mensajes)
        else:
            self.resultado_capturado = ""
    
    def obtener_resultado(self) -> str:
        """
        Retorna los mensajes generados por las reglas
        
        Returns:
            str: Mensajes de las reglas activadas
        """
        if not self.resultado_capturado.strip():
            return "✅ Tu situación financiera está equilibrada."
        return self.resultado_capturado
    
    def listar_hechos_actuales(self) -> list:
        """
        Lista los hechos actuales en el sistema
        
        Returns:
            list: Lista de hechos activos
        """
        return [str(fact) for fact in self.sistema.facts() if not str(fact).startswith("f-0")]
    
    def listar_reglas_disponibles(self) -> list:
        """
        Lista las reglas disponibles en el sistema
        
        Returns:
            list: Lista de reglas definidas
        """
        return [str(rule) for rule in self.sistema.rules()]
    
    def reiniciar_sistema(self) -> None:
        """Reinicia el sistema (mantiene reglas, limpia hechos)"""
        self.sistema.reset()
        self.resultado_capturado = ""
    
    def obtener_estado_completo(self) -> Dict[str, Any]:
        """
        Obtiene el estado completo del sistema
        
        Returns:
            Dict con hechos, reglas y resultado actual
        """
        return {
            'hechos': self.listar_hechos_actuales(),
            'reglas': self.listar_reglas_disponibles(),
            'resultado': self.resultado_capturado,
            'reglas_count': len(self.sistema.rules()),
            'hechos_count': len(self.sistema.facts())
        }


# Funciones de conveniencia para uso directo
def cargar_reglas(reglas_str: str = "") -> SistemaExperto:
    """
    Función de conveniencia para crear y configurar el sistema experto
    
    Args:
        reglas_str: Reglas adicionales opcionales
        
    Returns:
        SistemaExperto: Instancia configurada del sistema
    """
    sistema = SistemaExperto()
    if reglas_str:
        sistema.cargar_reglas(reglas_str)
    return sistema


def insertar_hechos(sistema: SistemaExperto, **kwargs) -> None:
    """
    Función de conveniencia para insertar hechos
    
    Args:
        sistema: Instancia del sistema experto
        **kwargs: Parámetros financieros
    """
    sistema.insertar_hechos(**kwargs)


def ejecutar_inferencia(sistema: SistemaExperto) -> None:
    """
    Función de conveniencia para ejecutar inferencia
    
    Args:
        sistema: Instancia del sistema experto
    """
    sistema.ejecutar_inferencia()


def obtener_resultado(sistema: SistemaExperto) -> str:
    """
    Función de conveniencia para obtener resultado
    
    Args:
        sistema: Instancia del sistema experto
        
    Returns:
        str: Resultado de la inferencia
    """
    return sistema.obtener_resultado()
