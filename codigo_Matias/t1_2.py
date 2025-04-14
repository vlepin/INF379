import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('movie_dataset.csv')

# Limpiar datos
df = df[df['revenue'] > 0]
df = df.dropna(subset=['original_language'])  # Eliminar valores nulos en 'original_language'

# Tomar los 5 idiomas más frecuentes
top_languages = df['original_language'].value_counts().nlargest(5).index
df_top = df[df['original_language'].isin(top_languages)]

# Gráfico de caja (boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_top, x='original_language', y='revenue', palette='Set2')
plt.title('Comparación de Ingresos según Idioma Original')
plt.xlabel('Idioma Original')
plt.ylabel('Ingresos de Taquilla (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
