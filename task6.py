# %% CELULA 1 - AJUSTE LINEAR DO MOVIMENTO

import numpy as np
import matplotlib.pyplot as plt

# X: tempo em segundos; Y: distância em metros
X = np.array([15.25, 16.38, 16.97, 18.12, 19.01])
Y = np.array([120, 130, 140, 150, 160], dtype=float)

# Gráfico dos dados
plt.figure(figsize=(10, 5))
plt.scatter(X, Y, color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Distância (m)")
plt.title("Atleta com velocidade constante")
plt.show()

# Somas necessárias para o método dos mínimos quadrados
n = len(X)
XY = X * Y
X2 = X ** 2

soma_X = sum(X)
soma_Y = sum(Y)
soma_X_2 = soma_X ** 2
soma_X2 = sum(X2)
soma_XY = sum(XY)

# Reta ajustada: distância = c1 * tempo + c2
denominador = n * soma_X2 - soma_X_2
c1 = (n * soma_XY - soma_X * soma_Y) / denominador
c2 = (soma_Y * soma_X2 - soma_X * soma_XY) / denominador

print(f"Soma X: {soma_X:.4f}")
print(f"Soma Y: {soma_Y:.4f}")
print(f"(Soma X)²: {soma_X_2:.4f}")
print(f"Soma X²: {soma_X2:.4f}")
print(f"Soma XY: {soma_XY:.4f}")
print(f"Velocidade (c1): {c1:.6f} m/s")
print(f"Posição inicial da reta (c2): {c2:.6f} m")

# Valores da reta ajustada
Ya = []
for i in range(n):
    Ya.append(c1 * X[i] + c2)

plt.figure(figsize=(10, 5))
plt.scatter(X, Y, color="red", label="Medidas")
plt.plot(X, Ya, color="blue", label="Reta ajustada")
plt.xlabel("Tempo (s)")
plt.ylabel("Distância (m)")
plt.title("Ajuste linear do corredor")
plt.legend()
plt.show()