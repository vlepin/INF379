import pandas as pd
import plotly.express as px
import ast

df = pd.read_csv('movie_dataset.csv')

df = df[['release_date', 'production_companies', 'revenue', 'original_title']]
df = df.dropna(subset=['release_date', 'production_companies', 'revenue'])

def extract_first_company(name_str):
    try:
        companies = ast.literal_eval(name_str)
        if isinstance(companies, list) and len(companies) > 0 and 'name' in companies[0]:
            return companies[0]['name']
    except:
        return None
    return None

df['production_companies_clean'] = df['production_companies'].apply(extract_first_company)
df = df.dropna(subset=['production_companies_clean'])

df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df = df.dropna(subset=['release_date'])
df['year'] = df['release_date'].dt.year

top_productions = df['production_companies_clean'].value_counts().head(10).index
df = df[df['production_companies_clean'].isin(top_productions)]

agg_df = df.groupby(['production_companies_clean', 'year'], as_index=False).agg({
    'revenue': 'sum',
    'original_title': lambda x: ', '.join(x.head(3))
})


fig = px.scatter(
    agg_df,
    x="year",
    y="production_companies_clean",
    size="revenue",
    color="production_companies_clean",
    hover_name="original_title",
    size_max=60,
    labels={
        "year": "Año de lanzamiento",
        "production_companies_clean": "Productora",
        "revenue": "Ingresos ($)",
        "original_title": "Películas destacadas"
    },
    title="Ingresos de películas por productora a lo largo del tiempo"
)


fig.update_layout(
    xaxis=dict(
        tickmode='linear',
        dtick=5
    ),
    yaxis={'categoryorder': 'total ascending'},
    template="plotly_white",
    legend_title="Productora"
)

fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>Año: %{x}<br>Productora: %{y}<br>Ingresos: $%{marker.size:,.0f}"
)

fig.show()
