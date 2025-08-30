# Sistema Financiero Inteligente - CLIPS + Lógica Difusa

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CLIPS](https://img.shields.io/badge/CLIPS-1.0+-green.svg)](https://sourceforge.net/projects/clipsrules/)
[![scikit-fuzzy](https://img.shields.io/badge/scikit--fuzzy-0.4.2+-orange.svg)](https://scikit-fuzzy.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un sistema financiero inteligente que integra **dos enfoques de inteligencia artificial**:
- **Sistema Experto CLIPS**: Basado en reglas lógicas para finanzas personales
- **Sistema Difuso**: Basado en lógica difusa para recomendaciones de inversión

## 🚀 Características

### 🧠 Sistema Experto CLIPS
- **Motor de inferencia CLIPS**: Sistema experto basado en reglas
- **Reglas financieras predefinidas**: Evaluación automática de salud financiera
- **Sistema de hechos**: Las reglas crean hechos que se procesan automáticamente
- **API reutilizable**: Módulo centralizado para uso en otros proyectos

### 🌊 Sistema Difuso
- **Variables lingüísticas**: Ahorro mensual y riesgo de inversión
- **Conjuntos difusos**: Triangulares y gaussianos según especificación
- **Reglas de inferencia**: 3 reglas principales para estrategias de inversión
- **Métodos de inferencia**: Mamdani y TSK (Takagi-Sugeno-Kang)
- **Defuzzificación**: Centroide para Mamdani, media de pesos para TSK

### 🖥️ Interfaz Integrada
- **Interfaz gráfica moderna**: GUI con Tkinter y pestañas
- **Pestaña 1**: Sistema Experto CLIPS para finanzas personales
- **Pestaña 2**: Sistema Difuso para recomendaciones de inversión
- **Pestaña 3**: Información completa del sistema
- **Visualización**: Gráficos de conjuntos difusos

## 📁 Estructura del Proyecto

```
sistema-experto-clips-python/
├── src/                          # Código fuente principal
│   ├── __init__.py
│   ├── sistema_experto.py        # Módulo del sistema experto CLIPS
│   ├── fuzzy_system.py           # Módulo del sistema difuso
│   └── gui/                      # Interfaz gráfica integrada
│       ├── __init__.py
│       └── main_window.py        # Ventana principal con pestañas
├── examples/                      # Ejemplos de uso
│   ├── __init__.py
│   ├── demo_basico.py            # Demostración del sistema experto
│   ├── ejemplo_uso.py            # Ejemplos del sistema experto
│   └── ejemplo_sistema_difuso.py # Ejemplos del sistema difuso
├── tests/                         # Pruebas
│   ├── __init__.py
│   └── test_sistema_experto.py   # Pruebas del módulo
├── docs/                          # Documentación
│   └── README.md                 # README detallado
├── requirements.txt               # Dependencias (CLIPS + scikit-fuzzy)
├── setup.py                      # Configuración del paquete
└── main.py                       # Punto de entrada principal
```

## 🛠️ Instalación

### Requisitos Previos

- Python 3.8 o superior
- Módulo CLIPS para Python
- scikit-fuzzy para lógica difusa
- numpy para cálculos numéricos
- matplotlib para visualización

### Instalación Rápida

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd sistema-experto-clips-python
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verificar instalación**:
   ```bash
   python tests/test_sistema_experto.py
   python examples/ejemplo_sistema_difuso.py
   ```

## 🚀 Uso Rápido

### Ejecutar la Interfaz Gráfica Integrada

```bash
python main.py
```

La interfaz se abrirá con tres pestañas:
- **🧠 Sistema Experto CLIPS**: Para finanzas personales
- **🌊 Sistema Difuso**: Para recomendaciones de inversión
- **ℹ️ Información**: Documentación del sistema

### Uso del Sistema Experto CLIPS

```python
from src.sistema_experto import SistemaExperto

# Crear sistema experto
sistema = SistemaExperto()

# Insertar datos financieros
sistema.insertar_hechos(
    ingresos=5000,
    ahorro=300,
    gastos=3000,
    deudas=2500,
    ocio=1200
)

# Ejecutar inferencia
sistema.ejecutar_inferencia()

# Obtener recomendaciones
resultado = sistema.obtener_resultado()
print(resultado)
```

### Uso del Sistema Difuso

```python
from src.fuzzy_system import SistemaDifusoFinanciero

# Crear sistema difuso
sistema_difuso = SistemaDifusoFinanciero()

# Evaluar con método Mamdani
resultado_mamdani = sistema_difuso.evaluar_mamdani(ahorro=700, riesgo=3)

# Evaluar con método TSK
resultado_tsk = sistema_difuso.evaluar_tsk(ahorro=700, riesgo=3)

# Evaluar ambos métodos
resultado_completo = sistema_difuso.evaluar_ambos_metodos(ahorro=700, riesgo=3)

print(f"Nivel de inversión recomendado: {resultado_mamdani['nivel_inversion']}%")
print(f"Estrategia: {resultado_mamdani['etiqueta']}")
```

## 🌊 Sistema Difuso - Detalles Técnicos

### Variables de Entrada

#### Ahorro Mensual (0-1000 USD)
- **Bajo**: (0, 0, 400) - Conjunto triangular
- **Medio**: (200, 500, 800) - Conjunto triangular
- **Alto**: (600, 1000, 1000) - Conjunto triangular

#### Riesgo de Inversión (0-10)
- **Bajo**: μ=0, σ=1.5 - Conjunto gaussiano
- **Moderado**: μ=5, σ=1.5 - Conjunto gaussiano
- **Alto**: μ=10, σ=1.5 - Conjunto gaussiano

### Variable de Salida

#### Nivel de Inversión (0-50%)
- **Conservadora**: (0, 10, 20) - Conjunto triangular
- **Moderada**: (15, 25, 35) - Conjunto triangular
- **Agresiva**: (30, 40, 50) - Conjunto triangular

### Reglas de Inferencia

1. **R1**: Si ahorro es bajo ∨ riesgo es alto → inversión es conservadora
2. **R2**: Si ahorro es medio ∧ riesgo es moderado → inversión es moderada
3. **R3**: Si ahorro es alto ∧ riesgo es bajo → inversión es agresiva
2. **R4**: Si ahorro es medio ∧ riesgo es bajo → inversión es moderada
3. **R5**: R5: Si ahorro es alto ∧ riesgo es moderado → inversión es agresiva

### Métodos de Inferencia

#### Mamdani (sistema difuso)
- Usa conjuntos difusos para la salida
- Defuzzificación por centroide
- Resultado más suave y continuo

#### TSK (Takagi-Sugeno-Kang)
- Usa singletones (valores fijos)
- Agregación por media de pesos
- Resultado más directo y computacionalmente eficiente

## 📚 Ejemplos

### Ejecutar Demostración Básica

```bash
python examples/demo_basico.py
```

### Ejecutar Ejemplos Completos

```bash
python examples/ejemplo_uso.py
```

## 🧪 Pruebas

### Ejecutar Todas las Pruebas

```bash
python tests/test_sistema_experto.py
```

### Ejecutar Pruebas Específicas

```bash
# Desde la raíz del proyecto
python -m pytest tests/
```

## 🔧 Desarrollo

### Instalar en Modo Desarrollo

```bash
pip install -e .[dev]
```

### Estructura de Desarrollo

- **`src/`**: Código fuente principal
- **`examples/`**: Ejemplos y demostraciones
- **`tests/`**: Pruebas unitarias y de integración
- **`docs/`**: Documentación detallada

## 📖 Documentación

Para información detallada sobre el uso, API y personalización, consulta:

- **Documentación completa**: [docs/README.md](docs/README.md)
- **Ejemplos de uso**: [examples/](examples/)
- **Pruebas**: [tests/](tests/)

## 🤝 Contribuciones

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

**¡Disfruta usando tu sistema experto CLIPS! 🎉**

---

*Desarrollado con ❤️ para la comunidad de IA y finanzas personales*
