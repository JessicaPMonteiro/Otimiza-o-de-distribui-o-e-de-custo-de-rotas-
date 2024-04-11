# -*- coding: utf-8 -*-
"""API_6-Otimizacao.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XI7I5YJdaQdZ5nC7PdSpa3DesebpCD9l
"""

#Importando as bibliotecas
import pandas as pd #data manipulation
import matplotlib.pyplot as plt #plotting library
import numpy as np

#Habilitando a abertura de dados que estão no Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Abrindo csv "Tabela Unica Completa"
Tabela_unica_completa = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_unica_completa.csv')

# Visualizando as primeiras linhas do DataFrame
print(Tabela_unica_completa.head())

# Checagem do arquivo
Tabela_unica_completa.info()

# Analises
## Filtros

# Extrair valores únicos da coluna 'CO.Fabrica'
Fabricas = Tabela_unica_completa['CO.Fabrica'].unique()

# Imprimir os valores únicos
print(Fabricas)

# Analise segmentada de uma fábrica

# Definindo os valores de fábrica e incoterm
CO_Fabrica = 3423909
incoterm = "CIF"

# Filtrando o DataFrame para a fábrica e incoterm específicos
df_filtrado = Tabela_unica_completa[(Tabela_unica_completa['CO.Fabrica'] == CO_Fabrica) & (Tabela_unica_completa['Incoterm'] == incoterm)]

# Extraindo clientes únicos
Clientes = df_filtrado['CO.Cliente'].unique()

# Imprimindo os clientes únicos
print(Clientes)

# Exportar a lista de clientes
with open('Clientes.txt', 'w') as file:
    for client in Clientes:
        file.write(str(client) + '\n')

from google.colab import files

# Baixar o arquivo 'Clientes.txt'
files.download('Clientes.txt')

# Frete médio por fabrica e cliente

df_filtrado['frete/unidade'] = df_filtrado['Vlr.Frete'] / df_filtrado['Qtd.Transp']
frete_media = df_filtrado.groupby(['CO.Fabrica','CO.Cliente'])['frete/unidade'].mean().reset_index()
frete_media.info()
print(frete_media)

from google.colab import files

# Gerar um CSV com a Tabela 'Frete médio por fabrica e cliente"
frete_media.to_csv('Frete.csv', index=False)

# Baixar o arquivo 'Frete.csv'
files.download('Frete.csv')