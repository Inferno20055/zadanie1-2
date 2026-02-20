class HeatEquationSolver:
    def __init__(self, L, T, a, Nx, Nt, initial_condition):
        self.L = L
        self.T = T
        self.a = a
        self.Nx = Nx
        self.Nt = Nt
        self.initial_condition = initial_condition

        self.h = 2 * L / (Nx - 1)
        self.tau = T / Nt
        self.sigma = a * self.tau / self.h ** 2

        self.x = [(-L + i * self.h) for i in range(Nx)]
        self.u = [initial_condition(xi) for xi in self.x]
        self.u_new = [0.0] * Nx

        self.u[0] = 0.0
        self.u[-1] = 0.0

    def check_stability(self):
        return self.sigma <= 0.5

    def solve(self):
        for _ in range(self.Nt):
            for i in range(1, self.Nx - 1):
                self.u_new[i] = (self.sigma * self.u[i - 1] +
                                 (1 - 2 * self.sigma) * self.u[i] +
                                 self.sigma * self.u[i + 1])

            self.u_new[0] = 0.0
            self.u_new[-1] = 0.0

            self.u, self.u_new = self.u_new, self.u