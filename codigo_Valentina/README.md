# Análisis de Ingresos de Taquilla

Esta sección contiene dos scripts en Python diseñados para visualizar y analizar los ingresos generados por películas a partir de un dataset. Las visualizaciones permiten entender la distribución de ingresos según el género y su evolución a lo largo de los años.

---

## Requisitos de instalación

Instala las dependencias necesarias con:

```bash
pip install pandas matplotlib seaborn plotly
```

## Datos utilizados

- [Movie Dataset kaggle](https://www.kaggle.com/datasets/utkarshx27/movies-dataset?resource=downloadmovie)

---

### 1. `tarea1_1.py` - Gráfico de violín

Este script genera un gráfico de violín que muestra la distribución de ingresos de películas agrupadas por género.

**Características:**
- Filtra los 5 géneros con más películas.
- Muestra una muestra aleatoria de hasta 800 películas por género.
- Ordena los géneros por el ingreso promedio de mayor a menor.
- Visualiza la distribución, los valores atípicos y los ingresos promedio por género.

**Requisitos:**
- `pandas`
- `plotly`

## Ejecución
```bash
python tarea1_1.py
```

### 2. `tarea1_2.py`

Este script genera un heatmap que muestra la evolución de los ingresos totales de taquilla por año, desde 1990 en adelante.

**Características:**
- Convierte la fecha de estreno a año.
- Agrupa los ingresos por año.
- Visualiza los ingresos totales en forma de mapa de calor.

**Requisitos:**
- `pandas`
- `seaborn`
- `matplotlib`

## Ejecución
```bash
python tarea1_2.py
```



