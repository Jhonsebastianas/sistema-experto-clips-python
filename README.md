# Sistema Experto CLIPS para Finanzas Personales

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CLIPS](https://img.shields.io/badge/CLIPS-1.0+-green.svg)](https://sourceforge.net/projects/clipsrules/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un sistema experto inteligente que utiliza CLIPS (C Language Integrated Production System) para proporcionar recomendaciones financieras personales basadas en reglas de negocio.

## 🚀 Características

- **Motor de inferencia CLIPS**: Sistema experto basado en reglas
- **Reglas financieras predefinidas**: Evaluación automática de salud financiera
- **Sistema de hechos**: Las reglas crean hechos que se procesan automáticamente
- **API reutilizable**: Módulo centralizado para uso en otros proyectos
- **Interfaz gráfica moderna**: GUI con Tkinter
- **Funciones de conveniencia**: API simple para uso rápido

## 📁 Estructura del Proyecto

```
sistema-experto-clips-python/
├── src/                          # Código fuente principal
│   ├── __init__.py
│   ├── sistema_experto.py        # Módulo principal del sistema experto
│   └── gui/                      # Interfaz gráfica
│       ├── __init__.py
│       └── main_window.py        # Ventana principal
├── examples/                      # Ejemplos de uso
│   ├── __init__.py
│   ├── demo_basico.py            # Demostración simple
│   └── ejemplo_uso.py            # Ejemplos completos
├── tests/                         # Pruebas
│   ├── __init__.py
│   └── test_sistema_experto.py   # Pruebas del módulo
├── docs/                          # Documentación
│   └── README.md                 # README detallado
├── requirements.txt               # Dependencias
├── setup.py                      # Configuración del paquete
└── main.py                       # Punto de entrada principal
```

## 🛠️ Instalación

### Requisitos Previos

- Python 3.8 o superior
- Módulo CLIPS para Python

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
   ```

## 🚀 Uso Rápido

### Ejecutar la Interfaz Gráfica

```bash
python main.py
```

### Uso Programático

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

## 🆘 Soporte

- **Issues**: Abre un issue en GitHub
- **Documentación**: Consulta [docs/README.md](docs/README.md)
- **Pruebas**: Ejecuta los archivos de prueba para verificar la instalación

## 🔄 Cambios Recientes

### Versión 2.0.0 - Refactorización Completa

- ✅ **Nueva estructura de proyecto** con buenas prácticas
- ✅ **Sistema de hechos** con `assert` en lugar de `printout`
- ✅ **API modular** y fácil de extender
- ✅ **Documentación completa** y ejemplos
- ✅ **Pruebas automatizadas**

---

**¡Disfruta usando tu sistema experto CLIPS! 🎉**

---

*Desarrollado con ❤️ para la comunidad de IA y finanzas personales*
