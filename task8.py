# ETAPA 01

import numpy as np
from sympy import Symbol, diff

#item 3
x = [3, 6]

# item 4
h = x[1] - x[0]

#item 5
y = []

#item 6 a 8
for i in range(len(x)):
    fx = 3 * x[i] + 2
    y.append(fx)

# item 9 
integral_trapeizo = (h / 2) * (y[0] + y[1])

#item 10
print("ETAPA 01 - Polinomio de grau 1")
print(f"h = {h}")
print(f"y = {y}")
#item 11
print(f"Integral pela regra do trapezio = {integral_trapeizo:.6f}")



# ETAPA 02

import numpy as np

# item 3 a 6
a = 3.0
b = 3.6
n = 6
h = (b - a) / n


# itens 7 e 8
x_atual = a
funcao = 1 / x_atual
area_total = 0.0
i = 0

while i < n:
	x_atual = x_atual + h
	y_atual = 1 / x_atual
	area_trapezio = ((funcao + y_atual) / 2) * h
	area_total = area_total + area_trapezio
	funcao = y_atual
	i += 1

# itens 10 e 11
print("ETAPA 02 - Formula composta")
print(f"a = {a}, b = {b}, n = {n}, h = {h}")
print(f"area_total = {area_total:.9f}")
print(f"Solucao exata de referencia = {np.log(b / a):.9f}\n")


# ETAPA 03

import numpy as np
from sympy import Symbol, diff

# item 2
xint = np.array([a,b])

# item 3
xs = Symbol("x")
f = 1 / xs
derivada = diff(f, xs, 2)

derivada_segunda = diff(f, xs, 2) #funcao da segunda derivada

max_valor = None

# item 4
for valor_x in xint:
	# item 5 e 6
	num = abs(float(derivada_segunda.subs(xs, valor_x)))

	# item 7
	if max_valor is None or num > max_valor:
		max_valor = num

# item 8
erro_truncamento = abs((n * h**3) / 12) * max_valor

# item 9
print("ETAPA 03 - Erro de truncamento")
print(f"f''(x) = {derivada_segunda}")
print(f"|f''(c)| max = {max_valor:.9f}")
print(f"Erro de truncamento = {erro_truncamento:.9f}")