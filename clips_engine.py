from clips import Environment

class ClipsEngine:
    def __init__(self):
        self.env = Environment()
        self.env.reset()  # Siempre iniciar con un reset

    def cargar_reglas(self, reglas_str: str):
        """Carga reglas en el motor CLIPS desde un string"""
        # Puedes cargar varias reglas separadas por saltos de línea
        for regla in reglas_str.split("\n"):
            regla = regla.strip()
            if regla:
                self.env.build(regla)

    def agregar_hecho(self, hecho: str):
        """Agrega un hecho"""
        self.env.assert_string(hecho)

    def ejecutar(self):
        """Ejecuta el motor de inferencia"""
        return self.env.run()

    def listar_hechos(self):
        """Devuelve lista de hechos (omitimos el fact inicial f-0)"""
        return [str(fact) for fact in self.env.facts() if not str(fact).startswith("f-0")]

    def listar_reglas(self):
        """Devuelve lista de reglas"""
        return [str(rule) for rule in self.env.rules()]
    
    def reiniciar(self):
        """Reinicia los hechos (pero mantiene las reglas)"""
        self.env.reset()