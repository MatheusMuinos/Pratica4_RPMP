# %% CELULA 1 - ETAPA 01 - INTERPOLACAO LINEAR

import numpy as np

n = 2
X = np.array([45000, 62000])  # Gastos
Y = np.array([56000, 78000])  # Receitas

G = 55000

R = Y[0] + ((G - X[0]) / (X[1] - X[0])) * (Y[1] - Y[0])

print(f"O valor da receita para um gasto de R$ {G:,.2f} é R$ {R:,.2f}")


# %% CELULA 2 - ETAPA 02 - INTERPOLACAO DE LAGRANGE

import numpy as np

X = np.array([283, 293, 303, 313])       # Temperaturas em K
Y = np.array([500, 1000, 3000, 5000])    # Pressões em Pa
n = len(X)

mT = 300
xp = mT
yp = 0

for k in range(n):
    p = 1

    for j in range(n):
        if k != j:
            p = p * (xp - X[j]) / (X[k] - X[j])

    yp = yp + p * Y[k]

print(f"O valor da pressão para uma temperatura de {mT} K é {yp:.2f} Pa")