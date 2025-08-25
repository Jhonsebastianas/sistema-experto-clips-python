# Sistema Experto CLIPS para Finanzas Personales

Este proyecto implementa un sistema experto usando CLIPS (C Language Integrated Production System) para proporcionar recomendaciones financieras personales basadas en reglas de negocio.

## 🚀 Características

- **Motor de inferencia CLIPS**: Sistema experto basado en reglas
- **Reglas financieras predefinidas**: Evaluación automática de salud financiera
- **Sistema de hechos**: Las reglas crean hechos de mensaje que se procesan automáticamente
- **API reutilizable**: Módulo centralizado para uso en otros proyectos
- **Interfaz gráfica**: GUI moderna con Tkinter
- **Funciones de conveniencia**: API simple para uso rápido

## 📁 Estructura del Proyecto

```
sistema-experto-clips-python/
├── sistema_experto.py          # 🆕 Módulo principal del sistema experto
├── ejemplo_uso.py              # 🆕 Ejemplos de uso del módulo
├── prueba_refactorizada.py     # 🆕 GUI refactorizada usando el nuevo módulo
├── test_sistema_experto.py     # 🆕 Pruebas del módulo
├── clips_engine.py             # Motor CLIPS básico (legacy)
├── gui.py                      # GUI básica (legacy)
├── main.py                     # Archivo principal (legacy)
├── prueba.py                   # Implementación original
└── README_SISTEMA_EXPERTO.md   # Este archivo
```

## 🛠️ Instalación

1. **Instalar dependencias**:
   ```bash
   pip install clips
   ```

2. **Verificar instalación**:
   ```bash
   python test_sistema_experto.py
   ```

## 📚 Uso del Módulo Sistema Experto

### Uso Básico

```python
from sistema_experto import SistemaExperto

# Crear instancia
sistema = SistemaExperto()

# Insertar hechos financieros
sistema.insertar_hechos(
    ingresos=5000,
    ahorro=300,      # Solo 6% de ingresos
    gastos=3000,
    deudas=2500,     # 50% de ingresos
    ocio=1200        # 40% de gastos
)

# Ejecutar inferencia
sistema.ejecutar_inferencia()

# Obtener recomendaciones
resultado = sistema.obtener_resultado()
print(resultado)
```

### Funciones de Conveniencia

```python
from sistema_experto import cargar_reglas, insertar_hechos, ejecutar_inferencia, obtener_resultado

# Crear y configurar sistema
sistema = cargar_reglas()

# Insertar hechos
insertar_hechos(sistema, ingresos=4000, ahorro=200, gastos=3500, deudas=2000, ocio=800)

# Ejecutar y obtener resultado
ejecutar_inferencia(sistema)
resultado = obtener_resultado(sistema)
```

### Cargar Reglas Personalizadas

```python
# Reglas adicionales usando assert
reglas_adicionales = """
(defrule reglaPersonalizada
    (condicion-especial)
    =>
    (assert (mensaje "Mensaje personalizado")))
"""

# Cargar en el sistema
sistema = cargar_reglas(reglas_adicionales)
```

## 🔍 Reglas del Sistema

El sistema incluye las siguientes reglas financieras predefinidas que usan `assert` para crear hechos:

1. **Regla de Ahorro**: Alerta si ahorras menos del 10% de ingresos
2. **Regla de Deuda**: Alerta si las deudas superan el 40% de ingresos
3. **Regla de Emergencia**: Alerta si no tienes 3 meses de gastos ahorrados
4. **Regla de Ocio**: Alerta si gastas más del 30% en ocio
5. **Regla de Inversión**: Recomienda inversiones si ahorras ≥15% y deudas <20%

### Formato de las Reglas

```clips
(defrule reglaEjemplo
    (condicion)
    =>
    (assert (mensaje "Tu mensaje aquí")))
```

**Nota**: Las reglas ahora usan `(assert (mensaje "texto"))` en lugar de `(printout t "texto" crlf)`. Esto permite un mejor control y procesamiento de los mensajes.

## 📊 API del Módulo

### Clase SistemaExperto

#### Métodos Principales

- `__init__()`: Inicializa el sistema experto
- `insertar_hechos(**kwargs)`: Inserta hechos financieros
- `ejecutar_inferencia()`: Ejecuta el motor de inferencia
- `obtener_resultado()`: Retorna las recomendaciones procesadas

#### Métodos de Información

- `listar_hechos_actuales()`: Lista hechos activos
- `listar_reglas_disponibles()`: Lista reglas del sistema
- `obtener_estado_completo()`: Estado completo del sistema
- `reiniciar_sistema()`: Limpia hechos, mantiene reglas

### Funciones de Conveniencia

- `cargar_reglas(reglas_str="")`: Crea y configura sistema
- `insertar_hechos(sistema, **kwargs)`: Inserta hechos
- `ejecutar_inferencia(sistema)`: Ejecuta inferencia
- `obtener_resultado(sistema)`: Obtiene resultado

## 🎯 Ejemplos de Uso

### Ejemplo 1: Análisis Financiero Simple

```python
from sistema_experto import SistemaExperto

sistema = SistemaExperto()
sistema.insertar_hechos(ingresos=3000, ahorro=150, gastos=2500, deudas=1800, ocio=900)
sistema.ejecutar_inferencia()
print(sistema.obtener_resultado())
```

### Ejemplo 2: Múltiples Escenarios

```python
from sistema_experto import SistemaExperto

sistema = SistemaExperto()

escenarios = [
    {'ingresos': 4000, 'ahorro': 800, 'gastos': 3000, 'deudas': 1000, 'ocio': 600},
    {'ingresos': 2000, 'ahorro': 100, 'gastos': 1800, 'deudas': 1500, 'ocio': 700}
]

for i, escenario in enumerate(escenarios, 1):
    print(f"\n--- Escenario {i} ---")
    sistema.insertar_hechos(**escenario)
    sistema.ejecutar_inferencia()
    print(sistema.obtener_resultado())
    sistema.reiniciar_sistema()
```

### Ejemplo 3: Reglas Personalizadas

```python
from sistema_experto import SistemaExperto

# Reglas personalizadas
reglas_personalizadas = """
(defrule reglaRiesgoAlto
    (ahorro-bajo)
    (deuda-alta)
    =>
    (assert (mensaje "🚨 RIESGO ALTO: Tu situación financiera es crítica.")))

(defrule reglaRecomendacionEspecifica
    (riesgo-alto)
    =>
    (assert (mensaje "💡 Prioriza pagar deudas y aumentar ahorro inmediatamente.")))
"""

sistema = SistemaExperto()
sistema.cargar_reglas(reglas_personalizadas)

# Insertar hechos y ejecutar
sistema.insertar_hechos(ingresos=2000, ahorro=50, gastos=1800, deudas=1500, ocio=500)
sistema.ejecutar_inferencia()
print(sistema.obtener_resultado())
```

## 🧪 Pruebas

### Ejecutar Pruebas Básicas

```bash
python test_sistema_experto.py
```

### Ejecutar Ejemplos Completos

```bash
python ejemplo_uso.py
```

### Ejecutar GUI Refactorizada

```bash
python prueba_refactorizada.py
```

## 🔧 Personalización

### Agregar Nuevas Reglas

```python
# Definir regla personalizada
nueva_regla = """
(defrule reglaNueva
    (condicion-nueva)
    =>
    (assert (mensaje "Nueva recomendación")))
"""

# Cargar en sistema existente
sistema.cargar_reglas(nueva_regla)
```

### Modificar Lógica de Hechos

```python
class SistemaExpertoPersonalizado(SistemaExperto):
    def insertar_hechos(self, **kwargs):
        # Lógica personalizada para insertar hechos
        super().insertar_hechos(**kwargs)
        
        # Agregar hechos adicionales
        if kwargs.get('edad', 0) > 50:
            self.sistema.assert_string("(edad-avanzada)")
```

## 🚨 Solución de Problemas

### Error: "No module named 'clips'"

```bash
pip install clips
```

### Error: "CLIPS environment not available"

Verificar que CLIPS esté instalado correctamente en el sistema.

### Los mensajes no se procesan correctamente

El sistema ahora procesa hechos de tipo `(mensaje "texto")`. Verificar que las reglas usen `assert` en lugar de `printout`.

## 📈 Próximas Mejoras

- [ ] Soporte para reglas desde archivos externos
- [ ] Persistencia de hechos y reglas
- [ ] API REST para uso web
- [ ] Más reglas financieras avanzadas
- [ ] Sistema de logging y auditoría
- [ ] Tests unitarios completos
- [ ] Soporte para hechos con múltiples campos
- [ ] Sistema de prioridades para mensajes

## 🤝 Contribuciones

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Para preguntas o problemas:
- Abre un issue en GitHub
- Revisa la documentación
- Ejecuta los archivos de prueba

---

**¡Disfruta usando tu sistema experto CLIPS! 🎉**

## 🔄 Cambios Recientes

### Versión 2.0 - Sistema de Hechos con Assert

- **Cambio principal**: Las reglas ahora usan `(assert (mensaje "texto"))` en lugar de `(printout t "texto" crlf)`
- **Beneficios**:
  - Mejor control sobre los mensajes
  - Procesamiento automático de hechos
  - Sistema más modular y mantenible
  - Facilita la extensión con nuevas reglas
- **Compatibilidad**: El API público se mantiene igual, solo cambia la implementación interna
