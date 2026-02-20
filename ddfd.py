import numpy as np
import matplotlib.pyplot as plt
from heat_equation_solver import HeatEquationSolver
from visualizitation import plot_temperature_profile  # проверьте правильность имени файла и функции

def main():
    L = float(input("Введите полуинтервал по x (L): "))  # Отрезок [-L, L]
    T = float(input("Введите время моделирования (T): "))
    a = float(input("Введите коэффициент температуропроводности (a): "))
    Nx = int(input("Введите число точек по пространству (Nx): "))
    Nt = int(input("Введите число временных шагов (Nt): "))

    # Начальное условие: пример — "шапка"
    def initial_condition(x):
        return 1.0 if abs(x) < 1 else 0.0

    solver = HeatEquationSolver(L=L, T=T, a=a, Nx=Nx, Nt=Nt, initial_condition=initial_condition)

    if not solver.check_stability():
        print("Внимание! Условие устойчивости σ <= 0.5 нарушено. Уменьшите шаг по времени или увеличьте Nx.")
        return

    solver.solve()

    plot_temperature_profile(solver.x, solver.u, title=f'Temperature profile at t={T}')

if __name__ == "__main__":
    main()