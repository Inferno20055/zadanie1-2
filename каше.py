import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from  heat_equation_solver import HeatEquationSolver
from visualizitation import visualisation
def u0(x):
    return np.exp(-x ** 2)
def apply_boundary_conditions(u):
    u[0] = 0
    u[-1] = 0
L = 10.0
T = 2.0
a = 1.0

Nx = 200
Nt = 1000
dx = 2 * L / (Nx - 1)
dt = T / Nt

if dt > dx ** 2 / (2 * a):
    print("Внимание! Схема может быть неустойчивой, уменьшите dt или увеличьте Nx")


x = np.linspace(-L, L, Nx)

u = u0(x)

u_new = np.zeros_like(u)

apply_boundary_conditions(u)

for n in range(Nt):

    for i in range(1, Nx - 1):
        u_new[i] = u[i] + a * dt / dx ** 2 * (u[i + 1] - 2 * u[i] + u[i - 1])

    apply_boundary_conditions(u_new)

    u[:] = u_new[:]

plt.plot(x, u, label=f't={T}')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Распределение температуры в конце расчёта')
plt.legend()
plt.grid()
plt.show()


