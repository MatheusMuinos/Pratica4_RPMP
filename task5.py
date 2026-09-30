# Etapa 1

import numpy as np

X = np.array([-4, 8], dtype=float)
Y = np.array([5, -11], dtype=float)
xint = 2

# Polinômio de Newton para dois pontos
f_int = Y[0] + (xint - X[0]) * (Y[1] - Y[0]) / (X[1] - X[0])

print(f"O valor interpolado para x = 2 é: {f_int:g}")

# Etapa 2

import numpy as np

X = np.array([2010, 2012, 2014, 2016, 2018], dtype=float)
Y = np.array([14302571, 14441531, 14565807, 14689684, 14812617],
             dtype=float)

def dif_divididas(x, y):
    n = len(y)
    dif = np.zeros((n, n))
    dif[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            dif[i, j] = (
                (dif[i + 1, j - 1] - dif[i, j - 1])
                / (x[i + j] - x[i])
            )

    return dif

def polinomio_newton(coef, x, xp):
    p = coef[-1]

    for k in range(len(x) - 2, -1, -1):
        p = coef[k] + (xp - x[k]) * p

    return p

# Subtrair 2010 dos anos facilita os cálculos sem alterar o resultado.
x = X - 2010

matriz_dif = dif_divididas(x, Y)
dif_d = matriz_dif[0, :]  # Coeficientes: primeira linha da matriz

A = 2013
Pop = polinomio_newton(dif_d, x, A - 2010)
print(f"A estimativa da população em 2013 é de: {Pop:,.0f}")

ANO = [2011, 2013, 2015, 2017]

for i in range(len(ANO)):
    y_new = polinomio_newton(dif_d, x, ANO[i] - 2010)
    print(f"O valor da população em {ANO[i]} é {y_new:,.0f}")