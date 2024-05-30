import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('https://raw.githubusercontent.com/deciocferreira/VisualizacaoInformacao/main/cursos-prouni.csv')

# Ordenar o DataFrame pelos valores das mensalidades em ordem decrescente
df_sorted = df.sort_values(by='mensalidade', ascending=False)

# Selecionar os 7 cursos mais caros
top_cursos_caros = df_sorted.head(7)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(top_cursos_caros['curso_busca'], top_cursos_caros['mensalidade'], color='skyblue')
plt.xlabel('Cursos')
plt.ylabel('Mensalidade')
plt.title('Top 7 Cursos Mais Caros Ofertados no Prouni')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.tight_layout()  # Ajustar layout para melhor visualização
plt.show()