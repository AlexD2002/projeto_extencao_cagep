import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do estilo do Seaborn
sns.set(style="whitegrid")

# 1. Leitura dos dados
# Supondo que você tenha um arquivo CSV com dados socioeconômicos
data = pd.read_csv('dados_socioeconomicos.csv')

# 2. Visualização inicial dos dados
print(data.head())

# 3. Limpeza de dados (caso necessário)
# Exemplo: Remover linhas com valores nulos
data.dropna(inplace=True)

# 4. Análise de dados
# Exemplo: Agrupar dados por faixa etária e calcular a média de renda
faixa_etaria = data.groupby('faixa_etaria')['renda'].mean().reset_index()

# 5. Visualização da renda média por faixa etária
plt.figure(figsize=(10, 6))
sns.barplot(x='faixa_etaria', y='renda', data=faixa_etaria, palette='viridis')
plt.title('Renda Média por Faixa Etária na Favela Cagepe')
plt.xlabel('Faixa Etária')
plt.ylabel('Renda Média')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('renda_media_faixa_etaria.png')  # Salvar gráfico
plt.show()

# 6. Visualização de dados socioeconômicos
# Exemplo: Distribuição de renda
plt.figure(figsize=(10, 6))
sns.histplot(data['renda'], bins=30, kde=True, color='blue')
plt.title('Distribuição de Renda na Favela Cagepe')
plt.xlabel('Renda')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('distribuicao_renda.png')  # Salvar gráfico
plt.show()

# 7. Salvar os dados processados, se necessário
data.to_csv('dados_processados.csv', index=False)