# clips_engine.py
from clips import Environment

class ClipsEngine:
    def __init__(self):
        self.env = Environment()

    def cargar_reglas(self, reglas_str: str):
        """Carga reglas en el motor CLIPS desde un string"""
        self.env.build(reglas_str)

    def agregar_hecho(self, hecho: str):
        """Agrega un hecho"""
        self.env.assert_string(hecho)

    def ejecutar(self):
        """Ejecuta el motor de inferencia"""
        return self.env.run()

    def listar_hechos(self):
        """Devuelve lista de hechos"""
        return [str(fact) for fact in self.env.facts()]

    def listar_reglas(self):
        """Devuelve lista de reglas"""
        return [str(rule) for rule in self.env.rules()]
