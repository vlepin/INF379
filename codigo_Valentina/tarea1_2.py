import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('movie_dataset.csv')

# Extraer el año
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['year'] = df['release_date'].dt.year

df_recent = df[(df['year'] >= 1990)]

# Agrupar por año
revenue_recent = df_recent.groupby('year')['revenue'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.heatmap(revenue_recent.pivot_table(index="year", values="revenue"),
            cmap="YlOrRd", annot=True, fmt=".0f", linewidths=1)
plt.title("Ingresos de taquilla por año")
plt.xlabel("Ingresos")
plt.ylabel("Año")
plt.tight_layout()
plt.show()
plt.savefig("grafico.png")
print("Gráfico guardado como 'grafico.png'")
