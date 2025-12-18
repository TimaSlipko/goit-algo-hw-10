import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

def monte_carlo_integration(func, a, b, n_samples=100000):
    x_random = np.random.uniform(a, b, n_samples)
    y_random = func(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

n_samples = 100000
monte_carlo_result = monte_carlo_integration(f, a, b, n_samples)

quad_result, quad_error = spi.quad(f, a, b)

analytical_result = (b**3 - a**3) / 3

print(f"Monte Carlo ({n_samples} samples): {monte_carlo_result}")
print(f"quad: {quad_result}")
print(f"Analytical calculation: {analytical_result}")
print(f"Monte Carlo error: {abs(monte_carlo_result - analytical_result)}")
print(f"quad error: {quad_error}")
