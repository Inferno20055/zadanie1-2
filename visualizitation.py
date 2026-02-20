import matplotlib.pyplot as plt

def plot_temperature_profile(x, u, title="Temperature Profile"):
    plt.plot(x, u)
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.title(title)
    plt.grid(True)
    plt.show()