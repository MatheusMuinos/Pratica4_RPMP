# %% CELULA 1 - ETAPA 01 - LEITURA E ANALISE DOS DADOS
# Pedro Wenzel, Isabela Reol, Antonio Pedro, Maria Clara Marques, Matheus Muinos

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Coloque o arquivo Excel na mesma pasta deste arquivo Python.
arquivo = 'PC - Programação 03.xlsx'

df = pd.read_excel(arquivo)

print("\nCinco primeiras jogadoras:")
print(df.head(5))

print("\nColuna Idade:")
print(df["Idade"])

print("\nColuna Jogadoras e Idade:")
print(df[["Jogadoras", "Idade"]])

soma_id = 0
n = len(df)

for i in df["Idade"]:
    soma_id = soma_id + i

media_id = soma_id / n

print("\nMédia de idade:")
print(media_id)

soma_al = 0

for i in df["Altura"]:
    soma_al = soma_al + i

media_al = soma_al / n

print("\nMédia de altura:")
print(media_al)


# %% CELULA 2 - ETAPA 02 - GRAFICO DE PONTUACAO
# Pedro Wenzel, Isabela Reol, Antonio Pedro, Maria Clara Marques, Matheus Muinos

import numpy as np
import matplotlib.pyplot as plt
X = (['Ana Carolina', 'Rosa Maria', 'Roberta', 'Lorenne', 'Nyeme', 'Caral Gattaz', 'Macris', 'Lorena', 'Gabi', 'Tainara', 'Pri Dariot', 'Natinha', 'Julia Kudiess', 'Kisy'])
Y = ([120, 34, 3, 28, 0, 108, 18, 9, 205, 91, 107, 0, 5, 60])

plt.barh(X,Y, color='red')
plt.ylabel('Jogadores')
plt.xlabel('Pontos')
plt.title('Pontuação da seleção brasileira de vôlei no campeonato mundial de 2022.')
plt.show()