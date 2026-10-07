# %% CELULA 1 - ETAPA 01 - SPLINE LINEAR

import matplotlib.pyplot as plt
import numpy as np

# item 4 a 6
def splineLinear(xi, xiant, fxi, fxiant, x):
    si = fxiant * (xi - x) / (xi - xiant) + fxi * (x - xiant) / (xi - xiant)
    return si

def SLM(xi, xiant, fxi, fxiant, t):
    yt = []
    for i in t:
        yt.append(splineLinear(xi, xiant, fxi, fxiant, i))
    return yt


# Itens 8 e 9
X_spline = np.array([1, 2, 5, 7], dtype=float)
Y_spline = np.array([1, 2, 3, 2.5], dtype=float)
t1 = np.linspace(1, 2, 10)
t2 = np.linspace(2, 5, 10)
t3 = np.linspace(5, 7, 10)

# Itens 10 e 11
s1 = SLM(X_spline[1], X_spline[0], Y_spline[1], Y_spline[0], t1)
s2 = SLM(X_spline[2], X_spline[1], Y_spline[2], Y_spline[1], t2)
s3 = SLM(X_spline[3], X_spline[2], Y_spline[3], Y_spline[2], t3)

print("ETAPA 01 - Splines lineares")
print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")

plt.figure(figsize=(10, 5))
plt.plot(t1, s1, "b-", label="[1, 2]")
plt.plot(t2, s2, "r-", label="[2, 5]")
plt.plot(t3, s3, "g-", label="[5, 7]")
plt.scatter(X_spline, Y_spline, color="black", label="Dados")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Splines lineares")
plt.legend()
plt.grid(True)
plt.show()


# %% CELULA 2 - ETAPA 02 - INTERPOLACAO DE LAGRANGE

import matplotlib.pyplot as plt
import numpy as np

def lagrange(X, Y, medida):
    yp = 0.0
    n = len(X)

    for i in range(n):
        termo = Y[i]
        for j in range(n):
            if i != j:
                termo *= (medida - X[j]) / (X[i] - X[j])
        yp += termo

    return yp

# Dados do movimento
X = np.array([1, 4, 7, 10, 13], dtype=float)
Y = np.array([1.8, 7.2, 12.6, 18.0, 23.4], dtype=float)

n = len(X)
mt = 8.75
yp = lagrange(X, Y, mt)

print("\nETAPA 02 - Interpolacao de Lagrange")
print(f"n = {n}")
print(f"Velocidade para t = {mt:.2f} s: {yp:.6f} m/s")


# %% CELULA 3 - ETAPA 03 - MMQ LINEAR

import matplotlib.pyplot as plt
import numpy as np

# Dados do movimento
X = np.array([1, 4, 7, 10, 13], dtype=float)
Y = np.array([1.8, 7.2, 12.6, 18.0, 23.4], dtype=float)

# Itens 4
plt.figure(figsize=(10, 5))
plt.scatter(X, Y, color="red", label="Medidas")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.title("Velocidade do carro")
plt.legend()
plt.grid(True)
plt.show()

# Itens 5 a 7
n = len(X)
XY = X * Y
X2 = X ** 2

# Item 8
soma_X = sum(X)
soma_Y = sum(Y)
soma_X_2 = soma_X ** 2
soma_X2 = sum(X2)
soma_XY = sum(XY)

# Item 9
denominador = n * soma_X2 - soma_X_2
c1 = (n * soma_XY - soma_X * soma_Y) / denominador
c2 = (soma_Y * soma_X2 - soma_X * soma_XY) / denominador

# Item 10
print("\nETAPA 03 - MMQ linear")
print(f"soma_X = {soma_X:.6f}")
print(f"soma_Y = {soma_Y:.6f}")
print(f"soma_X_2 = {soma_X_2:.6f}")
print(f"soma_X2 = {soma_X2:.6f}")
print(f"soma_XY = {soma_XY:.6f}")
print(f"c1 (aceleracao) = {c1:.6f} m/s2")
print(f"c2 (velocidade inicial) = {c2:.6f} m/s")

Y_ajustada = c1 * X + c2
plt.figure(figsize=(10, 5))
plt.scatter(X, Y, color="red", label="Medidas")
plt.plot(X, Y_ajustada, color="blue", label="Reta ajustada")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.title("MMQ linear da velocidade")
plt.legend()
plt.grid(True)
plt.show()


# %% CELULA 4 - ETAPA 04 - INTEGRACAO DE SIMPSON

import matplotlib.pyplot as plt
import numpy as np

def simpson(y2, h):
    """Calcula a integral pela regra de Simpson 1/3 composta."""
    n_intervalos = len(y2) - 1

    if n_intervalos % 2 != 0:
        raise ValueError("A regra de Simpson 1/3 exige um numero par de intervalos.")

    soma = 0.0
    for i, valor in enumerate(y2):
        if i == 0 or i == n_intervalos:
            soma += valor
        elif i % 2 == 0:
            soma += 2 * valor
        else:
            soma += 4 * valor

    return soma * h / 3

# Dados do movimento
X = np.array([1, 4, 7, 10, 13], dtype=float)
Y = np.array([1.8, 7.2, 12.6, 18.0, 23.4], dtype=float)


# Itens 3 a 5
a = X[0]
b = X[-1]
n = len(X) - 1
m = n + 1
h = (b - a) / n

# Item 6
resultado = simpson(Y, h)

print("\nETAPA 04 - Integracao pela regra de Simpson")
print(f"a = {a:.1f}, b = {b:.1f}, n = {n}, m = {m}, h = {h:.6f}")
print(f"Distancia percorrida = {resultado:.6f} m")
