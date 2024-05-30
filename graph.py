import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('https://raw.githubusercontent.com/deciocferreira/VisualizacaoInformacao/main/cursos-prouni.csv')

# Verificar as primeiras linhas do dataset para garantir que foi lido corretamente
print(df.head())

# Contar a frequência de cada curso
curso_frequencia = df['curso_busca'].value_counts()

# Selecionar os 4 cursos mais ofertados
top_cursos = curso_frequencia.head(4)

# Criar o gráfico de setores
plt.figure(figsize=(8, 8))
plt.pie(top_cursos, labels=top_cursos.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(top_cursos))))
plt.title('Top 4 Cursos Mais Ofertados no Prouni')
plt.axis('equal')  # Garantir que o gráfico seja um círculo
plt.show()
