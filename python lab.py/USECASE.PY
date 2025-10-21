import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

mean = 0
std_dev = 1
x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, mean, std_dev)

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, color='blue', label='Normal Distribution (μ=0, σ=1)')
plt.title("Probability Density Function - Normal Distribution")
plt.xlabel("Random Variable (x)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

n = 10
p = 0.5
x_binom = np.arange(0, n + 1)
pmf = binom.pmf(x_binom, n, p)

plt.figure(figsize=(8, 5))
plt.stem(x_binom, pmf, basefmt=" ", use_line_collection=True)
plt.title("Probability Mass Function - Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid(True)
plt.show()
