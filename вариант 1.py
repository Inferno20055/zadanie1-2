import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
#задание 1 а и б
x = np.linspace(0, 10, 500)

y1 = 5 - x
y2_upper = 3 * x + 3
y2_lower = 3 * x - 3

y_b1 = 4 - x
y_b2_lower = (6 - 6 * x) / 2
y_b2_upper = (5 - x) / 5

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y1, label='x1 + x2 ≤ 5')
plt.fill_between(x, 0, y1, where=(y1 >= 0), color='skyblue', alpha=0.5)
plt.plot(x, y2_upper, label='3x1 - x2 ≤ 3', color='orange')
plt.fill_between(x, 0, y2_upper, where=(y2_upper >= 0), color='orange', alpha=0.3)
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Графика для варианта (а)')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x, y_b1, label='x1 + x2 ≤ 4')
plt.fill_between(x, 0, y_b1, where=(y_b1 >= 0), color='lightgreen', alpha=0.5)
plt.plot(x, y_b2_lower, label='6x1 + 2x2 ≥ 6', color='red')
plt.fill_between(x, y_b2_lower, y_b2_upper, where=(y_b2_lower <= y_b2_upper), color='pink', alpha=0.5)
plt.plot(x, y_b2_upper, label='x1 + 5x2 ≥ 5', color='blue')
plt.fill_between(x, y_b2_upper, 0, where=(y_b2_upper >= 0), color='purple', alpha=0.3)
plt.xlim(0, 7)
plt.ylim(0, 7)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Графика для варианта (б)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
#задание 2
c = [-4, -10]

A = [
    [0.01, 0.02],
    [0.01, 0.03],
    [0.02, 0.03]
]
b = [60, 70, 100]


x_bounds = [(0, None), (0, None)]

res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

if res.success:
    x1, x2 = res.x
    max_profit = -res.fun
    print(f"Оптимальное количество носков: {x1:.2f}")
    print(f"Оптимальное количество чулок: {x2:.2f}")
    print(f"Максимальная прибыль: {max_profit:.2f} рублей")
else:
    print("Решение не найдено.")