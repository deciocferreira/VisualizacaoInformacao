import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('cursos-prouni.csv')
fig = go.Figure(data=go.Choropleth(
locations=df['Brasil'], # Nome do país
z = df['pop'].astype(int), # Dados para o Choropleth
locationmode = 'country names', # Tipo de identificção geográfica
colorscale = 'Reds', #escala contínua em tons de vermelho
colorbar_title = "Notas",
))
fig.update_layout(
title_text = 'Notas de corte Prouni- 2018',
geo_scope='Brazil', # Limita escopo para o Brasil
)
fig.show()
