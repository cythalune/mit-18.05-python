import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Distribution parameters
mu = 280
sigma = 8.5

# (a)

x = np.linspace(240, 320, 500)

pdf = norm.pdf(x, loc=mu, scale=sigma)
cdf = norm.cdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(8, 4))
plt.plot(x, pdf)
plt.title("Normal Distribution PDF")
plt.xlabel("Days of Gestation")
plt.ylabel("Density")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(x, cdf)
plt.title("Normal Distribution CDF")
plt.xlabel("Days of Gestation")
plt.ylabel("Probability")
plt.grid(True)
plt.show()


# (b)
# Due date: May 25 (280 days)
# Final exam: May 18 (7 days earlier)
exam_day = 280 - 7

prob_before_exam = norm.cdf(exam_day, loc=mu, scale=sigma)

print("(b)")
print("P(Birth on or before exam) =", prob_before_exam)


# (c)
# May 19 through May 31
# Relative to due date:
# May 19 = 274
# May 31 = 286
start = 274
end = 286

prob_after_exam = (
    norm.cdf(end, loc=mu, scale=sigma)
    - norm.cdf(start, loc=mu, scale=sigma)
)

print("\n(c)")
print("P(Birth between May 19 and May 31) =", prob_after_exam)


# (d)
# Need the exam date so that
# P(Birth after exam) = 0.95
#
# Therefore
# P(Birth on or before exam) = 0.05
exam_day = norm.ppf(0.05, loc=mu, scale=sigma)

days_before_due = mu - exam_day

print("\n(d)")
print("Exam should be about", round(days_before_due), "days before the due date.")
print("Day of gestation:", exam_day)