# -*- coding: utf-8 -*-
"""API_6-Distancias.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OQDQtl7oYBTCkUOTirpo82VOgcwnMgJJ
"""

#Importando as bibliotecas
import pandas as pd #data manipulation
import matplotlib.pyplot as plt #plotting library

#Habilitando a abertura de dados que estão no Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Abrindo csv "Tabela Novo Dataframe"
Tabela_novo_dataframe = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_novo_dataframe.csv')

# Importando a biblioteca pandas
import pandas as pd

# Filtrando as colunas desejadas
colunas_desejadas = ['CO.Fabrica', 'CO.Cliente', 'Dist']
Distancia = Tabela_novo_dataframe.filter(colunas_desejadas)

# Salvando o DataFrame em um arquivo CSV
Distancia.to_csv('Distancia.csv', index=False)

# Baixando o arquivo pelo Colab
from google.colab import files
files.download('Distancia.csv')

# Abrindo csv "Tabela Distância"
Tabela_distancia = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_distancia.csv')

# Abrindo csv "Tabela Nova Distância"
Nova_distancia = pd.read_csv('/content/drive/My Drive/Dados_API/Nova_distancia.csv')

Nova_distancia.to_csv('Nova_distancia.csv', index=False)

# Exibir informações sobre os DataFrames
print("Informações sobre Tabela_distancia:")
print(Tabela_distancia.info())

print("\nInformações sobre Nova_distancia:")
print(Nova_distancia.info())

# Verificar tipos de dados das colunas
print(Tabela_distancia.dtypes)
print(Nova_distancia.dtypes)

# Converter tipos de dados, se necessário
Nova_distancia['CO.Cliente'] = Nova_distancia['CO.Cliente'].astype(int)
Nova_distancia['CO.Fabrica'] = Nova_distancia['CO.Fabrica'].astype(int)

# Verificar valores nulos ou não correspondentes
print(Tabela_distancia['CO.Cliente'].isnull().sum())
print(Nova_distancia['CO.Cliente'].isnull().sum())

# Mesclar os DataFrames novamente
resultado = pd.merge(Tabela_distancia, Nova_distancia, on=['CO.Cliente', 'CO.Fabrica'], how='inner')

# Selecionar apenas as colunas necessárias
resultado = resultado[['CO.Cliente', 'CO.Fabrica', 'Dist', 'Nova_Dist']]

# Exibir o resultado
print(resultado)

print(resultado.columns)

# Selecionando apenas as colunas necessárias
resultado = resultado[['CO.Cliente', 'CO.Fabrica', 'Dist', 'Nova_Dist']]

# Exibindo o resultado
print(resultado)

# Salvando o DataFrame como um arquivo CSV
alteracao_distancias = resultado.copy()  # atribuir o resultado a uma nova variável
alteracao_distancias.to_csv('alteracao_distancias.csv', index=False)

# Baixando o arquivo CSV para o seu sistema local
from google.colab import files
files.download('alteracao_distancias.csv')

# Abrindo csv "Alteração das distâncias"
alteracao_distancias = pd.read_csv('/content/drive/My Drive/Dados_API/alteracao_distancias.csv')

print(alteracao_distancias)

# Calculando a diferença entre as colunas "Dist" e "Nova_Dist"
alteracao_distancias['Diferenca'] = alteracao_distancias['Dist'] - alteracao_distancias['Nova_Dist']

# Exibindo o DataFrame com a nova coluna "Diferenca"
print(alteracao_distancias)

# Filtrando as linhas onde a diferença é maior que zero
diferenca_positiva = alteracao_distancias[alteracao_distancias['Diferenca'] > 0]

# Exibindo o DataFrame com diferença positiva
print(diferenca_positiva)

# Filtrando as linhas onde a diferença é maior que zero
diferenca_positiva = alteracao_distancias[alteracao_distancias['Diferenca'] > 0]

# Calculando a média da diferença positiva
media_diferenca_positiva = diferenca_positiva['Diferenca'].mean()

# Exibindo a média da diferença positiva
print("Média da diferença positiva:", media_diferenca_positiva)

# Encontrando o índice da linha com a menor diferença
indice_menor_diferenca = alteracao_distancias['Diferenca'].idxmin()
linha_menor_diferenca = alteracao_distancias.loc[indice_menor_diferenca]

# Encontrando o índice da linha com a maior diferença
indice_maior_diferenca = alteracao_distancias['Diferenca'].idxmax()
linha_maior_diferenca = alteracao_distancias.loc[indice_maior_diferenca]

# Exibindo as linhas com menor e maior diferença
print("Linha com menor diferença:")
print(linha_menor_diferenca)
print("\nLinha com maior diferença:")
print(linha_maior_diferenca)

import pandas as pd

# Abrindo csv "Tabela Novo Dataframe"
Tabela_novo_dataframe = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_novo_dataframe.csv')

# Abrindo csv "Alteração das distâncias"
alteracao_distancias = pd.read_csv('/content/drive/My Drive/Dados_API/alteracao_distancias.csv')

# Adicionando a coluna 'Nova_Dist' ao DataFrame 'Tabela_novo_dataframe'
Tabela_novo_dataframe['Nova_Dist'] = alteracao_distancias['Nova_Dist']

# Isso adicionará a coluna 'Nova_Dist' de 'alteração_distancias' como uma nova coluna em 'Tabela_novo_dataframe'

# Excluindo a coluna Dist original
Tabela_novo_dataframe = Tabela_novo_dataframe.drop(columns=['Dist'])

# Isso removerá a coluna 'Dist' de 'Tabela_novo_dataframe'

# Exibindo o DataFrame resultante
print(Tabela_novo_dataframe)

# O Mês de dezembro não esta completo e deve ser excluido

# Excluindo as linhas com o valor '12' na coluna 'Mes.Base'
Tabela_novo_dataframe = Tabela_novo_dataframe.loc[Tabela_novo_dataframe['Mes.Base'] != 12]

# Isso removerá todas as linhas do DataFrame onde o valor da coluna 'Mes.Base' for '12'

# Exibindo o DataFrame resultante
print(Tabela_novo_dataframe)

from google.colab import files

# Salvando o DataFrame alterado como um arquivo CSV
Tabela_novo_dataframe.to_csv('Tabela_nova.csv', index=False)

# Baixando o arquivo CSV
files.download('Tabela_nova.csv')

# Abrindo csv "Tabela Nova"
Tabela_nova = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_nova.csv')

print (Tabela_nova)