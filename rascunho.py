import numpy as np
from sympy import Symbol, diff


# =========================
# ETAPA 01 - POLINOMIO DE GRAU 1
# =========================

# Item 3: intervalos x0 e x1.
x = [3, 6]

# Item 4: tamanho do intervalo.
h = x[1] - x[0]

# Item 5: lista que armazenara os valores da funcao.
y = []

# Itens 6 a 8: calculo de f(x) = 3x + 2 nos dois pontos.
for i in range(2):
	fx = 3 * x[i] + 2
	y.append(fx)

# Item 9: regra do trapezio para um unico intervalo.
integral_etapa_1 = (h / 2) * (y[0] + y[1])

# Item 10: resultado calculado pelo algoritmo.
print("ETAPA 01 - Polinomio de grau 1")
print(f"h = {h}")
print(f"y = {y}")
print(f"Integral pela regra do trapezio = {integral_etapa_1:.6f}")

# Item 11: para um polinomio de grau 1, o resultado e exato.
print(f"Solucao da integral = {integral_etapa_1:.6f}\n")


# =========================
# ETAPA 02 - FORMULA COMPOSTA
# =========================

# Itens 3 a 6: limites, numero de subdivisoes e passo h.
a = 3.0
b = 3.6
n = 6
h = (b - a) / n

# Itens 7 e 8: regra do trapezio composta para f(x) = 1/x.
x_atual = a
funcao = 1 / x_atual
area_total = 0.0
i = 0

while i < n:
	x_atual += h
	y_atual = 1 / x_atual
	area_trapezio = ((funcao + y_atual) / 2) * h
	area_total += area_trapezio
	funcao = y_atual
	i += 1

print("ETAPA 02 - Formula composta")
print(f"a = {a}, b = {b}, n = {n}, h = {h}")
print(f"area_total = {area_total:.9f}")
print(f"Solucao exata de referencia = {np.log(b / a):.9f}\n")


# =========================
# ETAPA 03 - ERRO DE TRUNCAMENTO
# =========================

# Item 2: extremos usados para procurar o maior valor de |f''(x)|.
xint = np.array([a, b])

# Itens 3 a 5: segunda derivada de f(x) = 1/x.
xs = Symbol("x")
fun = 1 / xs
derivada_segunda = diff(fun, xs, 2)
max_valor = None

# Item 6: avalia a derivada nos extremos em valor absoluto.
for valor_x in xint:
	num = abs(float(derivada_segunda.subs(xs, valor_x)))

	# Item 7: guarda o maior valor encontrado.
	if max_valor is None or num > max_valor:
		max_valor = num

# Item 8: ET = |n * h^3 / 12| * |f''(c)|max.
erro_truncamento = abs((n * h**3) / 12) * max_valor

# Item 9: resultado do erro de truncamento.
print("ETAPA 03 - Erro de truncamento")
print(f"f''(x) = {derivada_segunda}")
print(f"|f''(c)| max = {max_valor:.9f}")
print(f"Erro de truncamento = {erro_truncamento:.9f}")

