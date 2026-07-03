import numpy as np
from scipy.stats import norm, expon

# (a)
# Z ~ N(0, 1)
print("(a)")

# (i)
p1 = norm.cdf(0)
print("P(Z <= 0) =", p1)

# (ii)
p2 = 1 - norm.cdf(1.5)
print("P(Z > 1.5) =", p2)

# (iii)
p3 = norm.cdf(1.5) - norm.cdf(-1.5)
print("P(|Z| < 1.5) =", p3)


# (b)
# X ~ N(2, 3²)
mu = 2
sigma = 3

print("\n(b)")

# (i)
p1 = norm.cdf(mu, loc=mu, scale=sigma)
print("P(X <= μ) =", p1)

# (ii)
p2 = 1 - norm.cdf(mu + 1.5 * sigma, loc=mu, scale=sigma)
print("P(X - μ > 1.5σ) =", p2)

# (iii)
lower = mu - 1.5 * sigma
upper = mu + 1.5 * sigma

p3 = norm.cdf(upper, loc=mu, scale=sigma) - norm.cdf(lower, loc=mu, scale=sigma)
print("P(|X - μ| < 1.5σ) =", p3)


# (c)
# Y ~ Exp(λ)
lam = 2

print("\n(c)")

# Analytical result
cdf = 1 - np.exp(-lam * (1 / lam))
print("Analytical P(Y <= 1/λ) =", cdf)

# Numerical check using scipy
cdf_check = expon.cdf(1 / lam, scale=1 / lam)
print("SciPy check =", cdf_check)