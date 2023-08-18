import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")

# Creating dataframe

df = pd.read_excel(r"C:\Users\jeano\Documents\Jean\Coding\study\DIO\Análise de Dados com Pandas\AdventureWorks.xlsx")

# Visualizando 5 primeiras linhas
print(df.head())

# Quantidade de linhas e colunas
print(df.shape)

# Visualizando receita total
print(df["Valor Venda"].sum())

# Criando coluna de custo
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

# Criando coluna de lucro. 
df["Lucro"] = df["Valor Venda"] - df["Custo"]

# Criando coluna Tempo de Envio.
df["Tempo de Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# Plot Total de produtos vendidos.
total_prod = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.bar(title = "Total de produtos vendidos")
plt.xlabel('Total')
plt.ylabel('Produtos')
#plt.show()

# Plotando o Lucro por ano

df.groupby(df['Data Venda'].dt.year)['lucro'].sum().plot.bar(title = 'Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Lucro')
plt.show()


# Vendas do ano de 2009

df_2009 = df[df['Data Venda'].dt.year==2009]

# Lucro por mês
df_2009.groupby(df_2009['Data Venda'].dt.month)['lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()

# Lucro por marca
df_2009.groupby('Marca')['lucro'].sum().plot.bar(title = 'Lucro x Marca')
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = 30)
plt.show()

# Lucro por Classe

df_2009.groupby('Classe')['lucro'].sum().plot.bar(title = 'Lucro x Classe')
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = 'horizontal')
plt.show()


