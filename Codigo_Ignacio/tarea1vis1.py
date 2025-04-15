import pandas as pd
import ast
import plotly.express as px
import numpy as np


df = pd.read_csv("movie_dataset.csv")

def extract_countries(entrada):
    try:
        countries = ast.literal_eval(entrada)
        return [country['name'] for country in countries if 'name' in country]
    except:
        return []

df['country_list'] = df['production_countries'].dropna().apply(extract_countries)

df_exploded = df.explode('country_list')

df_exploded = df_exploded[['country_list', 'revenue']].dropna()
df_exploded = df_exploded[df_exploded['revenue'] > 0]

summary = df_exploded.groupby('country_list').agg(
    Cantidad_de_peliculas=('country_list', 'count'),
    Promedio_ingresos=('revenue', 'mean')
).reset_index()

summary.rename(columns={'country_list': 'Country'}, inplace=True)


summary['log_movie_count'] = np.log1p(summary['Cantidad_de_peliculas'])  

real_counts = [1,3,9,27,81,243,729,2178 ]
log_values = np.log1p(real_counts)

fig = px.choropleth(
    summary,
    locations="Country",
    locationmode="country names",
    color="log_movie_count", 
    hover_name="Country",
    hover_data={"Promedio_ingresos": ":$,.0f", "Cantidad_de_peliculas": True, "log_movie_count": False},
    color_continuous_scale="earth",
)


fig.update_coloraxes(
    colorbar=dict(
        tickvals=log_values,
        ticktext=[str(x) for x in real_counts],
        title="Cantidad de Películas"
    )
)


fig.update_layout(
    geo=dict(
        showland=True,
        landcolor="#ffffe5",
        showcoastlines=True,
        coastlinecolor="black",
        showlakes=True,
        lakecolor="#e0f7fa",
        showocean=True,
        oceancolor="#006994",
        bgcolor="#ffffff",
        projection_type="orthographic"
    ),
    width=1000,
    height=800,
    title="Cantidad de Películas y Promedio de Recaudación por País"
)

fig.show()
