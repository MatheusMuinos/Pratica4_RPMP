# %% CELULA 1 - ETAPA 01 - REGRA DE SIMPSON

import numpy as np
from sympy import Symbol, diff


def simpson(xn, h):
	n = len(xn) - 1

	if n % 2 != 0:
		raise ValueError("A regra de Simpson 1/3 exige um numero par de intervalos.")

	i = 0
	area_total = 0.0

	while i <= n:
		y2 = xn[i]

		if i == 0 or i == n:
			area_total += y2
		elif i % 2 == 0:
			area_total += 2 * y2
		else:
			area_total += 4 * y2

		i += 1

	return area_total * h / 3


# Itens 4b a 4d
a = 3.0
b = 3.6
n = 6
m = n + 1
h = (b - a) / n

# Itens 4e a 4j
xn = []
f = a
xn.append(f)

for j in range(n):
	f = f + h
	xn.append(f)

# Itens 5 e 6
valores_1 = [1 / x for x in xn]
resultado = simpson(valores_1, h)

print("ETAPA 01 - Regra de Simpson")
print(f"a = {a}, b = {b}, n = {n}, m = {m}, h = {h:.6f}")
print(f"xn = {xn}")
print(f"Resultado da integral = {resultado:.9f}")
print(f"Solucao analitica = {np.log(b / a):.9f}")


# %% CELULA 2 - ETAPA 02 - ERRO DE TRUNCAMENTO

import numpy as np
from sympy import Symbol, diff

# Itens 2 e 3: intervalo, quantidade de intervalos e passo.
a = 3.0
b = 3.6
n = 6
h = (b - a) / n
xint = np.array([a, b])

# Itens 3 a 7
xs = Symbol("x")
fun = 1 / xs
derivada_quarta = diff(fun, xs, 4)
max_valor = None

for valor_x in xint:
	num = abs(float(derivada_quarta.subs(xs, valor_x)))

	if max_valor is None or num > max_valor:
		max_valor = num

# Item 8
erro_truncamento = (h**5 / 180) * n * max_valor

# Item 9: resultado do erro.
print("\nETAPA 02 - Erro de truncamento")
print(f"f''''(x) = {derivada_quarta}")
print(f"|f''''(xi)| max = {max_valor:.9f}")
print(f"Erro de truncamento = {erro_truncamento:.9f}")


# %% CELULA 3 - ETAPA 03 - TRABALHO DO GAS

import numpy as np

def simpson(xn, h):
    """Calcula a integral pela regra de Simpson 1/3 composta."""
    n = len(xn) - 1

    if n % 2 != 0:
        raise ValueError("A regra de Simpson 1/3 exige um numero par de intervalos.")

    area_total = 0.0
    for i, y2 in enumerate(xn):
        if i == 0 or i == n:
            area_total += y2
        elif i % 2 == 0:
            area_total += 2 * y2
        else:
            area_total += 4 * y2

    return area_total * h / 3

# Itens 3 e 4
X = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
Y = np.array([80, 72, 64, 53, 44, 31, 22], dtype=float)

# Itens 6 a 8: limites, numero de intervalos e passo.
a_gas = X[0]
b_gas = X[-1]
n_gas = len(X) - 1
m_gas = n_gas + 1
h_gas = (b_gas - a_gas) / n_gas

# Item 9
resultado_gas = simpson(Y, h_gas)

# Item 10
print("\nETAPA 03 - Trabalho do gas")
print(f"a = {a_gas}, b = {b_gas}, n = {n_gas}, m = {m_gas}, h = {h_gas:.6f}")
print(f"Pressao = {Y.tolist()}")
print(f"Trabalho realizado pelo gas = {resultado_gas:.6f} J")