import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('movie_dataset.csv')

# Limpiar datos
df = df[df['budget'] > 0]
df = df[df['revenue'] > 0]

# Gráfico de hexágonos
plt.figure(figsize=(10, 6))
plt.hexbin(df['budget'], df['revenue'], gridsize=50, cmap='YlGnBu')
plt.title('Presupuesto vs Ingresos de Taquilla')
plt.xlabel('Presupuesto (USD)')
plt.ylabel('Ingresos de Taquilla (USD)')

# Establecer límites de los ejes
plt.xlim(0, 1e8)  # Eje X de 0 a 100 millones
plt.ylim(0, 1.5e8)  # Eje Y de 0 a 500 millones

# Agregar barra de colores para la densidad
plt.colorbar(label='Densidad')

# Ajustar la visualización
plt.tight_layout()
plt.show()
