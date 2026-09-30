import numpy as np
import matplotlib.pyplot as plt
import math


# =========================
# ETAPA 01 - CONSTANTE DA MOLA
# =========================

# Etapa 01 - item 4
X = np.array([0.6, 1.2, 1.8, 2.4, 3.0, 3.6])
Y = np.array([5.90, 23.90, 53.50, 95.00, 148.50, 213.80])

# Etapa 01 - item 7
plt.figure(figsize=(10, 5))
plt.scatter(X, Y, color="red")
plt.xlabel("Deformacao (m)")
plt.ylabel("Energia potencial (J)")
plt.title("Estudo do comportamento da mola do elevador")
plt.grid(True)
plt.show()

# Etapa 01 - item 8
plt.figure(figsize=(10, 5))
plt.scatter(X, Y, color="red")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Deformacao (m)")
plt.ylabel("Energia potencial (J)")
plt.title("Linearizacao log-log da mola")
plt.grid(True, which="both")
plt.show()

# Etapa 01 - item 9
n_mola = len(X)

# Etapa 01 - item 10
ln_X = np.log(X)
ln_Y = np.log(Y)

# Etapa 01 - item 11
ln_XY = ln_X * ln_Y

# Etapa 01 - item 12
ln_X2 = ln_X ** 2

# Etapa 01 - item 13
soma_X = sum(ln_X)
soma_Y = sum(ln_Y)
soma_X_2 = soma_X ** 2
soma_X2 = sum(ln_X2)
soma_XY = sum(ln_XY)

# Etapa 01 - item 14
denominador_mola = n_mola * soma_X2 - soma_X_2
a1_mola = (n_mola * soma_XY - soma_X * soma_Y) / denominador_mola
a2_mola = (soma_Y - a1_mola * soma_X) / n_mola

# Etapa 01 - item 15
print("ETAPA 01 - Constante elastica da mola")
print(f"soma_X = {soma_X:.6f}")
print(f"soma_Y = {soma_Y:.6f}")
print(f"soma_X_2 = {soma_X_2:.6f}")
print(f"soma_X2 = {soma_X2:.6f}")
print(f"soma_XY = {soma_XY:.6f}")

# Etapa 01 - item 16
print(f"a1 (potencia) = {a1_mola:.6f}")
print(f"a2 (intercepto) = {a2_mola:.6f}")

# Etapa 01 - item 17
print(f"Potencia da deformacao (a1) = {a1_mola:.6f}")

# Etapa 01 - item 18
k = 2 * math.exp(a2_mola)

# Etapa 01 - item 19
print(f"Constante elastica k = {k:.6f} N/m\n")


# =========================
# ETAPA 02 - CORRENTE ALTERNADA
# =========================

# Etapa 02 - item 3
T = np.array([0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7])
I = np.array([-15.69, -27.69, 37.42, -1.67, -36.11, 30.00, 12.57, -39.86, 18.70])

# Etapa 02 - item 4, letras a-g
f = 60
w = 2 * math.pi * f
xa = np.cos(w * T * math.pi / 180)

# Etapa 02 - item 5
plt.figure(figsize=(10, 5))
plt.scatter(xa, I, color="red")
plt.xlabel("cos(wt)")
plt.ylabel("Corrente (A)")
plt.title("Estudo da corrente alternada do circuito")
plt.grid(True)
plt.show()

# Etapa 02 - item 6
n = len(T)

# Etapa 02 - item 7
xaI = xa * I

# Etapa 02 - item 8
xa2 = xa ** 2

# Etapa 02 - item 9, letras a-d
soma_xa = sum(xa)
soma_I = sum(I)
soma_xa_2 = soma_xa ** 2
soma_xa2 = sum(xa2)
soma_xaI = sum(xaI)

# Etapa 02 - item 10
denominador = n * soma_xa2 - soma_xa_2
a2 = (n * soma_xaI - soma_xa * soma_I) / denominador
a1 = (soma_I - a2 * soma_xa) / n

# Etapa 02 - item 11
print("Resultados dos somatorios:")
print(f"soma_xa = {soma_xa:.6f}")
print(f"soma_I = {soma_I:.6f}")
print(f"soma_xa_2 = {soma_xa_2:.6f}")
print(f"soma_xa2 = {soma_xa2:.6f}")
print(f"soma_xaI = {soma_xaI:.6f}")

# Etapa 02 - item 12
print("\nConstantes do ajuste:")
print(f"a1 (intercepto) = {a1:.6f} A")
print(f"a2 (amplitude maxima) = {a2:.6f} A")

# Etapa 02 - item 13
print(f"Amplitude maxima da corrente: {abs(a2):.6f} A")

# grafico complementar
I_ajustada = a1 + a2 * xa
ordem = np.argsort(xa)

plt.figure(figsize=(10, 5))
plt.scatter(xa, I, color="red", label="Medidas")
plt.plot(xa[ordem], I_ajustada[ordem], color="blue", label="Reta ajustada")
plt.xlabel("cos(wt)")
plt.ylabel("Corrente (A)")
plt.title("MMQ da corrente alternada")
plt.legend()
plt.grid(True)
plt.show()
