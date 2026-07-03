import numpy as np


def longest_run(sequence):
    max_run = 1
    current_run = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 1

    return max(max_run, current_run)

#(a)
trial = np.random.randint(0, 2, size=50)

print(f"Part (a)\nSequence:\n {trial}")


# (b)
print("\nPart (b)\nLongest run:", longest_run(trial))


#(c)
n_trials = 10000
n_flips = 50

longest_runs = []

for _ in range(n_trials):
    trial = np.random.randint(0, 2, size=n_flips)
    longest_runs.append(longest_run(trial))

average_longest_run = np.mean(longest_runs)

print("\nPart (c)")
print("Average longest run over 10000 trials:", average_longest_run)


#(d)
count = 0

for _ in range(n_trials):
    trial = np.random.randint(0, 2, size=n_flips)

    if longest_run(trial) >= 8:
        count += 1

probability = count / n_trials

print("\nPart (d)")
print("Estimated probability of a run of at least 8:", probability)