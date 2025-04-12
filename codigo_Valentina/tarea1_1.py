import pandas as pd
import plotly.express as px

# Carga el dataset
df = pd.read_csv('movie_dataset.csv')
df = df[['revenue', 'genres']].dropna()

# Extrae el primer género
df['main_genre'] = df['genres'].apply(lambda x: x.split(' ')[0] if ' ' in x else x)

# Filtramos por los 5 géneros más populares
top_genres = df['main_genre'].value_counts().nlargest(5).index
df_top = df[df['main_genre'].isin(top_genres)]

# Muestra aleatoria de 800 películas por género
df_sampled = df_top.groupby('main_genre').apply(lambda x: x.sample(n=min(800, len(x)), random_state=42)).reset_index(drop=True)

genre_order = df_sampled.groupby('main_genre')['revenue'].mean().sort_values(ascending=False).index

fig = px.violin(df_sampled, y="revenue", x="main_genre", box=True, points="all", color="main_genre",
                category_orders={"main_genre": genre_order},  # Aquí va el orden
                title="Distribución de ingresos",
                labels={"main_genre": "Género", "revenue": "Ingresos"})
fig.show()
