import pandas as pd
import statsmodels.api as sm

years = list(range(1999, 2024))

primary_balance = [
    0.925, 1.060, -0.524, -1.457, -1.211, -0.900, -0.929, 0.628, 2.554, 2.070,
    -0.831, -2.289, 1.156, 1.781, 1.555, 1.960, 1.996, 2.066, 2.170, 2.607,
    1.918, -3.916, -2.703, -1.348, -1.850
]

output_gap = [
   -0.038, 1.328, 1.608, 0.381, -1.349, -1.280, -1.775, 0.447, 2.394, 2.488,
   -3.834, -0.973, 1.358, 0.261, -0.809, -0.331, -0.324, 0.095, 1.040, 0.883,
    0.438, -3.085, -0.762, 1.315, -0.217
]

inflation = [
    0.647, 1.413, 1.900, 1.326, 1.074, 1.780, 1.928, 1.775, 2.271, 2.754,
    0.246, 1.119, 2.482, 2.159, 1.607, 0.769, 0.680, 0.367, 1.702, 1.935,
    1.354, 0.371, 3.212, 8.666, 6.030
]

debt_lag = [
    59.438, 60.349, 59.239, 58.062, 59.823, 63.344, 64.965, 67.120, 66.397, 63.687,
    65.170, 72.362, 81.034, 78.484, 79.835, 77.457, 74.538, 71.184, 68.301, 63.988,
    60.758, 58.682, 68.037, 67.991, 64.442
]

crisis_dummy = [1 if year in (2009, 2010, 2020, 2021) else 0 for year in years]

post2011 = [1 if year >= 2011 else 0 for year in years]

df = pd.DataFrame({
    'Year': years,
    'PrimaryBalance': primary_balance,
    'OutputGap': output_gap,
    'Inflation': inflation,
    'Debt_lag': debt_lag,
    'CrisisDummy': crisis_dummy,
    'Post2011': post2011
})

df['OG_x_Post2011'] = df['OutputGap'] * df['Post2011']

Y = df['PrimaryBalance']
X_full = df[['OutputGap', 'OG_x_Post2011', 'Post2011', 'Debt_lag', 'Inflation', 'CrisisDummy']]
X_full = sm.add_constant(X_full)

model_full = sm.OLS(Y, X_full).fit()

print("=" * 100)
print("РЕЗУЛЬТАТЫ ОЦЕНКИ БАЗОВОЙ МОДЕЛИ (OLS)")
print("PrimaryBalance_t = β₀ + β₁·OutputGap_t + β₂·(OutputGap_t×Post2011_t) +")
print("β₃·Post2011_t + β₄·Debt_{t-1} + β₅·Inflation_t + β₆·CrisisDummy_t + ε_t")
print("=" * 100)
print(model_full.summary())

with open('regression_results_full.txt', 'w', encoding='utf-8') as f:
    f.write(model_full.summary().as_text())

X_simple = df[['OutputGap', 'OG_x_Post2011', 'Post2011', 'Inflation']]
X_simple = sm.add_constant(X_simple)

model_simple = sm.OLS(Y, X_simple).fit()
model_simple_robust = sm.OLS(Y, X_simple).fit(cov_type='HC3')

print("\n" + "=" * 100)
print("Обычный OLS")
print("=" * 100)
print(model_simple.summary())

print("\n" + "=" * 100)
print("Робастые стандартные ошибки HC3)")
print("=" * 100)
print(model_simple_robust.summary())

with open('regression_results_simple.txt', 'w', encoding='utf-8') as f:
    f.write("=== Обычный OLS ===\n")
    f.write(model_simple.summary().as_text())
    f.write("\n\n=== Робастые стандартные ошибки HC3 ===\n")
    f.write(model_simple_robust.summary().as_text())