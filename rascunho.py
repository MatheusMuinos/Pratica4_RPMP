# ============================================
# ROTEIRO DE PRÁTICA - PYTHON III
# Estatística das Jogadoras de Vôlei
# ============================================


# -----------------------------
# ETAPA 01 - PANDAS
# -----------------------------

# 4. Importar a biblioteca pandas
import pandas as pd


# 6. Importar o arquivo Excel
# O arquivo deve estar na mesma pasta do Jupyter Notebook
df = pd.read_excel("jogadoras_2022.xlsx")


# 7. Mostrar as cinco primeiras jogadoras
print("Cinco primeiras jogadoras:")
print(df.head())


# 8. Mostrar apenas a coluna Idade
print("\nColuna Idade:")
print(df["Idade"])


# 9. Mostrar as colunas Jogadoras e Idade
print("\nJogadoras e Idade:")
print(df[["Jogadoras", "Idade"]])


# -----------------------------
# MÉDIA DAS IDADES
# -----------------------------

c


# -----------------------------
# ETAPA 02 - GRÁFICO
# -----------------------------

# 1. Importar numpy
import numpy as np


# 2. Criar as matrizes X e Y
X = np.array(df["Jogadoras"])
Y = np.array(df["Pontos"])


# 3. Importar matplotlib
import matplotlib.pyplot as plt


# 4. Criar gráfico de barras horizontal
plt.barh(X, Y, color="red")


# 5. Nomes dos eixos
plt.xlabel("Pontos")
plt.ylabel("Jogadoras")


# 6. Título do gráfico
plt.title(
    "Pontuação da seleção brasileira de vôlei "
    "no campeonato mundial de 2022"
)


# 7. Mostrar gráfico
plt.show()