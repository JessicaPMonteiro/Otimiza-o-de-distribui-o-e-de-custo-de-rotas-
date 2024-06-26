# -*- coding: utf-8 -*-
"""API_6-Sprint1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12mSkHHTqD0cSi4lwhsH5Tcr8-E3l6sem
"""

#Importando as bibliotecas
import pandas as pd #data manipulation
import matplotlib.pyplot as plt #plotting library

#Habilitando a abertura de dados que estão no Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Abrindo csv "Tabela nova Frete"
Tabela_nova_frete = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_nova_frete.csv')

# Calculando a média da coluna 'Produtividade'
media_produtividade = Tabela_nova_frete['Produtividade'].mean()

# Calculando a mediana da coluna 'Produtividade'
mediana_produtividade = Tabela_nova_frete['Produtividade'].median()

print("Média da Produtividade:", media_produtividade)
print("Mediana da Produtividade:", mediana_produtividade)

import pandas as pd
import matplotlib.pyplot as plt

# Carregando o CSV em um DataFrame
df = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_nova_frete.csv')

# Listas para armazenar os meses e as médias de produtividade
meses = []
medias_produtividade = []

# Iterar sobre os meses de 1 a 12
for mes in range(1, 13):
    # Filtrando as linhas onde o valor na coluna 'Mes.Base' é igual ao mês atual
    df_filtrado = df[df['Mes.Base'] == mes]

    # Calculando a média da coluna 'Produtividade' para o mês atual
    media_produtividade = df_filtrado['Produtividade'].mean()

    # Armazenando o mês e a média de produtividade nas listas
    meses.append(mes)
    medias_produtividade.append(media_produtividade)

# Criando o gráfico de linhas
plt.plot(meses, medias_produtividade, marker='o')

# Adicionando rótulos aos eixos
plt.xlabel('Mês')
plt.ylabel('Produtividade Média')

# Adicionando título ao gráfico
plt.title('Produtividade Média por Mês Geral')

# Exibindo o gráfico
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Carregando o CSV em um DataFrame
df = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_nova_frete.csv')

# Lista de CO.Fabrica e seus respectivos nomes
fabricas = {
    3423909: 'Itu',
    3403208: 'Araraquara',
    3424402: 'Jacareí'
}

# Dicionário para armazenar os dados de produtividade média por fábrica
dados_fabricas = {}

# Iterando sobre cada CO.Fabrica
for fabrica, nome in fabricas.items():
    # Filtrando as linhas onde o valor na coluna 'CO.Fabrica' é igual ao da fábrica atual
    df_fabrica = df[df['CO.Fabrica'] == fabrica]

    # Listas para armazenar os meses e as médias de produtividade
    meses = []
    medias_produtividade = []

    # Iterando sobre os meses de 1 a 12
    for mes in range(1, 13):
        # Filtrando as linhas onde o valor na coluna 'Mes.Base' é igual ao mês atual
        df_mes = df_fabrica[df_fabrica['Mes.Base'] == mes]

        # Calculando a média da coluna 'Produtividade' para o mês atual
        media_produtividade = df_mes['Produtividade'].mean()

        # Armazenando o mês e a média de produtividade nas listas
        meses.append(mes)
        medias_produtividade.append(media_produtividade)

    # Armazenando os dados da fábrica no dicionário
    dados_fabricas[nome] = {'meses': meses, 'produtividade': medias_produtividade}

# Criando o gráfico de linhas para cada fábrica
for nome, dados in dados_fabricas.items():
    plt.plot(dados['meses'], dados['produtividade'], marker='o', label=f'{nome}')

# Adicionando rótulos aos eixos
plt.xlabel('Mês')
plt.ylabel('Produtividade Média')

# Adicionando título ao gráfico
plt.title('Produtividade Média por Mês')

# Adicionando legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Carregando o CSV em um DataFrame
df = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_nova_frete.csv')

# Lista de CO.Fabrica e seus respectivos nomes
fabricas = {
    3423909: 'Itu',
    3403208: 'Araraquara',
    3424402: 'Jacareí'
}

# Lista de veículos desejados
veiculos = ['P12', 'P24']

# Dicionário para armazenar os dados de produtividade média por fábrica e veículo
dados_fabricas_veiculos = {}

# Iterando sobre cada CO.Fabrica
for fabrica, nome_fabrica in fabricas.items():
    # Filtrando as linhas onde o valor na coluna 'CO.Fabrica' é igual ao da fábrica atual
    df_fabrica = df[df['CO.Fabrica'] == fabrica]

    # Dicionário para armazenar os dados de produtividade média por veículo
    dados_veiculos = {}

    # Iterando sobre cada veículo
    for veiculo in veiculos:
        # Filtrando as linhas onde o valor na coluna 'Veiculo' é igual ao veículo atual
        df_veiculo = df_fabrica[df_fabrica['Veiculo'] == veiculo]

        # Listas para armazenar os meses e as médias de produtividade
        meses = []
        medias_produtividade = []

        # Iterando sobre os meses de 1 a 12
        for mes in range(1, 13):
            # Filtrando as linhas onde o valor na coluna 'Mes.Base' é igual ao mês atual
            df_mes = df_veiculo[df_veiculo['Mes.Base'] == mes]

            # Calculando a média da coluna 'Produtividade' para o mês atual
            media_produtividade = df_mes['Produtividade'].mean()

            # Armazenando o mês e a média de produtividade nas listas
            meses.append(mes)
            medias_produtividade.append(media_produtividade)

        # Armazenando os dados do veículo no dicionário
        dados_veiculos[veiculo] = {'meses': meses, 'produtividade': medias_produtividade}

    # Armazenando os dados da fábrica e veículo no dicionário
    dados_fabricas_veiculos[nome_fabrica] = dados_veiculos

# Criando o gráfico de linhas para cada fábrica e veículo
for nome_fabrica, dados_veiculos in dados_fabricas_veiculos.items():
    for veiculo, dados in dados_veiculos.items():
        plt.plot(dados['meses'], dados['produtividade'], marker='o', label=f'{nome_fabrica} - {veiculo}')

# Adicionando rótulos aos eixos
plt.xlabel('Mês')
plt.ylabel('Produtividade Média')

# Adicionando título ao gráfico
plt.title('Produtividade Média por Mês (por Veículo)')

# Adicionando legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()

import pandas as pd

# Carregando o DataFrame
Tabela_unica = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_nova_frete.csv')

# Lista de veículos desejados
veiculos = ['P12', 'P24']

# Dicionário para armazenar a produtividade média por veículo
produtividade_por_veiculo = {}

# Iterando sobre cada veículo
for veiculo in veiculos:
    # Filtrando as linhas onde o valor na coluna 'Veiculo' é igual ao veículo atual
    df_veiculo = Tabela_unica[Tabela_unica['Veiculo'] == veiculo]

    # Calculando a média da coluna 'Produtividade' para o veículo atual
    media_produtividade_veiculo = df_veiculo['Produtividade'].mean()

    # Armazenando a média da produtividade do veículo no dicionário
    produtividade_por_veiculo[veiculo] = media_produtividade_veiculo

# Exibindo os resultados
for veiculo, media_produtividade in produtividade_por_veiculo.items():
    print(f'Veículo: {veiculo}, Produtividade Média: {media_produtividade:.2f}')

# Abrindo csv "Frete_CIF"
Frete_CIF = pd.read_csv('/content/drive/My Drive/Dados_API/Frete_CIF.csv')

# Valor do Frete por mês

# Criando uma lista vazia para armazenar os custos mensais com frete
custo_mensal_frete = []

# Loop de 1 a 12 para calcular o custo mensal com frete
for mes in range(1, 13):
    # Filtrando o DataFrame para o mês atual
    df_mes = Frete_CIF[Frete_CIF['Mes.Base'] == mes]

    # Calculando o custo total do frete para o mês atual
    custo_mes_atual = df_mes['Vlr.Frete'].sum()

    # Adicionando o custo total do frete para o mês atual à lista
    custo_mensal_frete.append(custo_mes_atual)

# Imprimindo o custo mensal com frete
print("Custo mensal com frete:")
for mes, custo in enumerate(custo_mensal_frete, start=1):
    print(f"Mês {mes}: R${custo:.2f}")

import matplotlib.pyplot as plt

# Criando uma lista para os meses de 1 a 12
meses = list(range(1, 13))

# Criando o gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(meses, custo_mensal_frete, marker='o', linestyle='-')
plt.title('Custo Mensal com Frete')
plt.xlabel('Mês')
plt.ylabel('Custo (R$)')
plt.grid(True)
plt.xticks(meses)  # Define os ticks do eixo x como os meses de 1 a 12
plt.tight_layout()

# Exibindo o gráfico
plt.show()

import matplotlib.pyplot as plt

# Dicionário que mapeia os códigos das fábricas para os nomes das fábricas
fabrica_nomes = {
    3423909: 'Itu',
    3424402: 'Araraquara',
    3403208: 'Jacareí'
}

# Lista única de fábricas
fabricas = Frete_CIF['CO.Fabrica'].unique()

# Criando um gráfico para cada fábrica
plt.figure(figsize=(12, 8))

for fabrica in fabricas:
    # Criando uma lista para armazenar os custos mensais de frete para esta fábrica
    custo_mensal_frete_fabrica = []

    # Loop de 1 a 12 para calcular o custo mensal com frete para esta fábrica
    for mes in range(1, 13):
        # Filtrando o DataFrame para a fábrica e o mês atual
        df_mes_fabrica = Frete_CIF[(Frete_CIF['CO.Fabrica'] == fabrica) & (Frete_CIF['Mes.Base'] == mes)]

        # Calculando o custo total do frete para esta fábrica e mês atual
        custo_mes_atual_fabrica = df_mes_fabrica['Vlr.Frete'].sum()

        # Adicionando o custo total do frete para esta fábrica e mês atual à lista
        custo_mensal_frete_fabrica.append(custo_mes_atual_fabrica)

    # Plotando o gráfico de linhas para esta fábrica com o nome substituído na legenda
    plt.plot(meses, custo_mensal_frete_fabrica, marker='o', label=fabrica_nomes.get(fabrica, fabrica))

# Configurações do gráfico
plt.title('Custo Mensal com Frete por Fábrica')
plt.xlabel('Mês')
plt.ylabel('Custo (R$)')
plt.grid(True)
plt.xticks(meses)
plt.legend()
plt.tight_layout()

# Exibindo o gráfico
plt.show()

# Agrupando os dados pelo nome da cidade e calculando a soma dos custos de frete para cada cidade
custo_por_cidade = Frete_CIF.groupby('MUN')['Vlr.Frete'].sum().reset_index()

# Ordenando os custos de frete em ordem decrescente
custo_por_cidade = custo_por_cidade.sort_values(by='Vlr.Frete', ascending=False)

# Exibindo as cidades com os maiores custos de frete
print("Cidades com os maiores custos de frete:")
print(custo_por_cidade.head(10))

import matplotlib.pyplot as plt

# Ordenando os custos de frete em ordem crescente
custo_por_cidade = custo_por_cidade.sort_values(by='Vlr.Frete', ascending=True)

# Configurações do gráfico
plt.figure(figsize=(10, 8))

# Plotando o gráfico de barras horizontais
plt.barh(custo_por_cidade['MUN'], custo_por_cidade['Vlr.Frete'], color='skyblue')
plt.xlabel('Custo de Frete (R$)')
plt.ylabel('Cidade')
plt.title('Cidades com Maiores Custos de Frete')

# Exibindo o gráfico
plt.show()

# Visualizar as inconsistências corrigidas

## Utilizar a Tabela 'Tabela_unica_inc'

# Abrindo csv "Tabela Unica Inc"
Tabela_unica_inc = pd.read_csv('/content/drive/My Drive/Dados_API/Tabela_unica_inc.csv')

# Inconsistência relacionada ao incoterm utilizado

# Filtrando as linhas onde a coluna 'Incoterm' contém 'FOB' e a coluna 'Vlr.Frete' contém o valor maior que 0
resultado = Tabela_unica_inc[(Tabela_unica_inc['Incoterm'].str.contains('FOB')) & (Tabela_unica_inc['Vlr.Frete'] > 0)]

# Exibindo apenas as colunas consultadas no resultado
print(resultado)

# Identificando qual rota apresentou mais esse erro

# Importando a biblioteca Pandas, se já não estiver importada
import pandas as pd

# Calculando a contagem de cada combinação entre 'CO.Fabrica' e 'MUN' no resultado
contagem_rotas = resultado.groupby(['CO.Fabrica', 'MUN']).size().reset_index(name='Contagem')

# Ordenando o DataFrame pelo número de ocorrências em ordem crescente
contagem_rotas_sorted = contagem_rotas.sort_values(by='Contagem')

# Exibindo o resultado
print(contagem_rotas_sorted)

# Gerando um gráfico para visualizar as rotas com maiores erros

# Dicionário que mapeia os códigos de fábrica para os nomes das fábricas
nomes_fabricas = {
    '3423909': 'Itu',
    '3403208': 'Araraquara',
    '3424402': 'Jacareí'
}

# Definindo o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Criando o gráfico de barras
plt.bar(contagem_rotas.index, contagem_rotas['Contagem'])

# Substituindo os códigos de fábrica pelos nomes das fábricas
contagem_rotas['CO.Fabrica'] = contagem_rotas['CO.Fabrica'].astype(str).map(nomes_fabricas)

# Definindo os rótulos do eixo x
plt.xticks(contagem_rotas.index, [fabrica + ' - ' + municipio for fabrica, municipio in zip(contagem_rotas['CO.Fabrica'], contagem_rotas['MUN'])], rotation=90)

# Definindo os rótulos dos eixos e o título
plt.xlabel('Rotas')
plt.ylabel('Número de erros')
plt.title('Contagem de Erros no Incoterm por Rotas')

# Exibindo o gráfico
plt.tight_layout()
plt.show()