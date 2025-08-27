# Sistema Difuso Financiero - Documentación Técnica

## 📋 Descripción General

El Sistema Difuso Financiero es un módulo que implementa lógica difusa (fuzzy logic) para proporcionar recomendaciones de inversión basadas en dos variables de entrada: **ahorro mensual** y **riesgo de inversión**. El sistema utiliza scikit-fuzzy para implementar inferencia difusa con dos métodos: **Mamdani** y **TSK**.

## 🎯 Objetivo

Proporcionar recomendaciones inteligentes sobre qué porcentaje del ingreso mensual debería destinarse a inversión, considerando el perfil de ahorro del usuario y su tolerancia al riesgo.

## 🏗️ Arquitectura del Sistema

### Componentes Principales

1. **Variables Lingüísticas de Entrada**
   - Ahorro mensual (USD)
   - Riesgo de inversión (escala 0-10)

2. **Variable Lingüística de Salida**
   - Nivel de inversión recomendada (%)

3. **Motor de Inferencia Difusa**
   - Sistema Mamdani
   - Sistema TSK

4. **Defuzzificación**
   - Centroide para Mamdani
   - Media de pesos para TSK

## 📊 Variables Lingüísticas

### Ahorro Mensual (0-1000 USD)

| Etiqueta | Rango | Función | Descripción |
|----------|-------|---------|-------------|
| **Bajo** | [0, 400] | Triangular (0, 0, 400) | Ahorro insuficiente para inversión agresiva |
| **Medio** | [200, 800] | Triangular (200, 500, 800) | Ahorro moderado, permite estrategias balanceadas |
| **Alto** | [600, 1000] | Triangular (600, 1000, 1000) | Ahorro sustancial, permite estrategias agresivas |

### Riesgo de Inversión (0-10)

| Etiqueta | Rango | Función | Descripción |
|----------|-------|---------|-------------|
| **Bajo** | [0, 10] | Gaussiano (μ=0, σ=1.5) | Perfil conservador, aversión al riesgo |
| **Moderado** | [0, 10] | Gaussiano (μ=5, σ=1.5) | Perfil balanceado, tolerancia media al riesgo |
| **Alto** | [0, 10] | Gaussiano (μ=10, σ=1.5) | Perfil agresivo, alta tolerancia al riesgo |

### Nivel de Inversión (0-50%)

| Etiqueta | Rango | Función | Descripción |
|----------|-------|---------|-------------|
| **Conservadora** | [0, 20] | Triangular (0, 10, 20) | Estrategia de bajo riesgo, preservación de capital |
| **Moderada** | [15, 35] | Triangular (15, 25, 35) | Estrategia balanceada, crecimiento moderado |
| **Agresiva** | [30, 50] | Triangular (30, 40, 50) | Estrategia de alto riesgo, máximo crecimiento potencial |

## 🧠 Reglas de Inferencia

### Regla 1: Estrategia Conservadora
```
SI ahorro es bajo O riesgo es alto
ENTONCES inversión es conservadora
```
**Lógica**: OR (máximo) entre condiciones
**Aplicación**: Cuando el usuario tiene poco ahorro o alta aversión al riesgo

### Regla 2: Estrategia Moderada
```
SI ahorro es medio Y riesgo es moderado
ENTONCES inversión es moderada
```
**Lógica**: AND (mínimo) entre condiciones
**Aplicación**: Cuando el usuario tiene ahorro moderado y tolerancia media al riesgo

### Regla 3: Estrategia Agresiva
```
SI ahorro es alto Y riesgo es bajo
ENTONCES inversión es agresiva
```
**Lógica**: AND (mínimo) entre condiciones
**Aplicación**: Cuando el usuario tiene ahorro sustancial y baja aversión al riesgo

## ⚙️ Métodos de Inferencia

### Método Mamdani

#### Características
- **Entrada**: Conjuntos difusos
- **Salida**: Conjuntos difusos
- **Agregación**: Unión (máximo)
- **Defuzzificación**: Centroide

#### Proceso
1. **Fuzzificación**: Convertir entradas numéricas a grados de pertenencia
2. **Evaluación de Reglas**: Aplicar operadores lógicos (AND/OR)
3. **Implicación**: Recortar conjuntos de salida según el grado de activación
4. **Agregación**: Combinar todas las salidas recortadas
5. **Defuzzificación**: Calcular centroide del conjunto agregado

#### Ventajas
- Resultados más suaves y continuos
- Interpretación intuitiva de la salida
- Manejo natural de incertidumbre

#### Desventajas
- Computacionalmente más costoso
- Resultados pueden ser menos precisos

### Método TSK (Takagi-Sugeno-Kang)

#### Características
- **Entrada**: Conjuntos difusos
- **Salida**: Singletones (valores fijos)
- **Agregación**: Media ponderada
- **Defuzzificación**: Media de pesos

#### Proceso
1. **Fuzzificación**: Convertir entradas numéricas a grados de pertenencia
2. **Evaluación de Reglas**: Aplicar operadores lógicos (AND/OR)
3. **Implicación**: Usar singletones predefinidos
4. **Agregación**: Media ponderada de los singletones
5. **Defuzzificación**: Resultado directo de la agregación

#### Singletones Utilizados
- **Conservadora**: 10% (valor máximo del conjunto conservador)
- **Moderada**: 25% (valor máximo del conjunto moderado)
- **Agresiva**: 40% (valor máximo del conjunto agresivo)

#### Ventajas
- Computacionalmente eficiente
- Resultados más precisos y directos
- Fácil interpretación numérica

#### Desventajas
- Resultados menos suaves
- Menos intuitivo para interpretación lingüística

## 🔧 Implementación Técnica

### Dependencias
```python
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
```

### Estructura de Clases

```python
class SistemaDifusoFinanciero:
    def __init__(self):
        self._configurar_variables()
        self._configurar_reglas()
        self._crear_sistemas_control()
    
    def _configurar_variables(self):
        # Configuración de variables lingüísticas
        
    def _configurar_reglas(self):
        # Definición de reglas de inferencia
        
    def _crear_sistemas_control(self):
        # Creación de sistemas Mamdani y TSK
```

### Métodos Principales

#### `evaluar_mamdani(ahorro, riesgo)`
- Evalúa el sistema usando el método Mamdani
- Retorna diccionario con resultado numérico y etiqueta

#### `evaluar_tsk(ahorro, riesgo)`
- Evalúa el sistema usando el método TSK
- Retorna diccionario con resultado numérico y etiqueta

#### `evaluar_ambos_metodos(ahorro, riesgo)`
- Evalúa ambos métodos simultáneamente
- Permite comparación y análisis de consistencia

#### `visualizar_conjuntos_difusos()`
- Genera gráficos de los conjuntos difusos
- Utiliza matplotlib para visualización

## 📈 Casos de Uso

### Caso 1: Perfil Conservador
- **Entrada**: Ahorro = 200 USD, Riesgo = 8
- **Esperado**: Inversión conservadora (0-20%)
- **Justificación**: Bajo ahorro + alto riesgo = estrategia defensiva

### Caso 2: Perfil Moderado
- **Entrada**: Ahorro = 500 USD, Riesgo = 5
- **Esperado**: Inversión moderada (15-35%)
- **Justificación**: Ahorro medio + riesgo moderado = estrategia balanceada

### Caso 3: Perfil Agresivo
- **Entrada**: Ahorro = 800 USD, Riesgo = 2
- **Esperado**: Inversión agresiva (30-50%)
- **Justificación**: Alto ahorro + bajo riesgo = estrategia de crecimiento

## 🧪 Pruebas y Validación

### Pruebas Unitarias
- Creación correcta del sistema
- Validación de rangos de entrada
- Evaluación de métodos Mamdani y TSK
- Consistencia entre métodos
- Determinación correcta de etiquetas

### Casos de Prueba
- Valores límite (0, 1000 USD; 0, 10 riesgo)
- Valores fuera de rango (validación de errores)
- Casos extremos (máximo ahorro + mínimo riesgo)
- Casos intermedios (valores en zonas de transición)

### Validación de Resultados
- Los resultados están en el rango [0, 50]%
- Las etiquetas son consistentes con los valores numéricos
- Ambos métodos producen resultados similares para casos claros
- Las diferencias entre métodos son razonables

## 🔍 Análisis de Resultados

### Interpretación de Salidas

#### Nivel de Inversión
- **0-20%**: Estrategia conservadora, preservación de capital
- **15-35%**: Estrategia moderada, crecimiento balanceado
- **30-50%**: Estrategia agresiva, máximo crecimiento potencial

#### Etiquetas Lingüísticas
- **Conservadora**: Para usuarios con bajo ahorro o alta aversión al riesgo
- **Moderada**: Para usuarios con ahorro y tolerancia al riesgo balanceados
- **Agresiva**: Para usuarios con alto ahorro y baja aversión al riesgo

### Comparación de Métodos

#### Diferencias Esperadas
- **Mamdani**: Resultados más suaves, transiciones graduales
- **TSK**: Resultados más directos, valores más precisos
- **Rango de diferencias**: Típicamente 0-5% entre métodos

#### Interpretación de Diferencias
- **Diferencias pequeñas (<2%)**: Alta consistencia del sistema
- **Diferencias moderadas (2-5%)**: Variación normal entre métodos
- **Diferencias grandes (>5%)**: Posible problema en la configuración

## 🚀 Uso Avanzado

### Personalización de Conjuntos Difusos
```python
# Modificar rangos de conjuntos triangulares
self.ahorro_mensual['bajo'] = fuzz.trimf(
    self.ahorro_mensual.universe, [0, 0, 300]
)

# Modificar parámetros gaussianos
self.riesgo_inversion['bajo'] = fuzz.gaussmf(
    self.riesgo_inversion.universe, 0, 2.0
)
```

### Agregación de Nuevas Reglas
```python
# Nueva regla personalizada
regla4 = ctrl.Rule(
    (self.ahorro_mensual['medio'] & self.riesgo_inversion['bajo']),
    self.nivel_inversion['moderada']
)

# Agregar al sistema
self.sistema_mamdani = ctrl.ControlSystem([
    self.regla1, self.regla2, self.regla3, regla4
])
```

### Visualización Personalizada
```python
# Guardar visualización como imagen
self.sistema_difuso.visualizar_conjuntos_difusos(guardar_imagen=True)

# Personalizar gráficos
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')
```

## 📚 Referencias

### Documentación Oficial
- [scikit-fuzzy Documentation](https://scikit-fuzzy.readthedocs.io/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/)

### Teoría de Lógica Difusa
- Zadeh, L.A. (1965). "Fuzzy sets". Information and Control, 8(3), 338-353.
- Mamdani, E.H. (1974). "Application of fuzzy algorithms for control of simple dynamic plant". Proceedings of the Institution of Electrical Engineers, 121(12), 1585-1588.
- Takagi, T., & Sugeno, M. (1985). "Fuzzy identification of systems and its applications to modeling and control". IEEE Transactions on Systems, Man, and Cybernetics, 15(1), 116-132.

### Aplicaciones Financieras
- Chen, S.M., & Chen, J.H. (2009). "Fuzzy risk analysis based on similarity measures of generalized fuzzy numbers". IEEE Transactions on Fuzzy Systems, 17(4), 745-757.
- Kahraman, C., & Kaya, İ. (2010). "Investment analysis using linguistic variables". Fuzzy Sets and Systems, 161(5), 741-763.

## 🤝 Contribuciones

### Áreas de Mejora
1. **Optimización de Conjuntos Difusos**: Ajuste fino de parámetros
2. **Nuevas Reglas**: Expansión del conjunto de reglas
3. **Métodos de Defuzzificación**: Implementación de métodos alternativos
4. **Validación Empírica**: Comparación con datos reales del mercado

### Código de Conducta
- Mantener documentación actualizada
- Seguir estándares de código Python (PEP 8)
- Incluir pruebas para nuevas funcionalidades
- Documentar cambios y mejoras

---

**Nota**: Esta documentación está diseñada para ser comprensible por estudiantes y desarrolladores que se inician en lógica difusa. Para consultas técnicas específicas, consulte la documentación oficial de scikit-fuzzy.
