import numpy as np

def triple_birthday(n):
    birthdays = np.random.randint(1, 366, size=n)

    counts = np.bincount(birthdays)

    return np.any(counts >= 3)


def estimate_probability(n, trials=10000):
    successes = 0

    for _ in range(trials):
        if triple_birthday(n):
            successes += 1

    return successes / trials


n = 2

while True:
    probability = estimate_probability(n)

    print(f"n = {n}, P(C) ≈ {probability:.4f}")

    if probability > 0.5:
        print(f"\nEstimated smallest n = {n}")
        break

    n += 1