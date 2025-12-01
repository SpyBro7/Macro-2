import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

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
X = df[['OutputGap', 'OG_x_Post2011', 'Post2011', 'Debt_lag', 'Inflation', 'CrisisDummy']]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()

print(model.summary())

new_data = pd.DataFrame({
    'Year': [2024],
    'OutputGap': [0.0],
    'Post2011': [1],
    'Debt_lag': [62.382],
    'Inflation': [2.0],
    'CrisisDummy': [0]
})
new_data['OG_x_Post2011'] = new_data['OutputGap'] * new_data['Post2011']

X_new = new_data[['OutputGap', 'OG_x_Post2011', 'Post2011', 'Debt_lag', 'Inflation', 'CrisisDummy']]
X_new = sm.add_constant(X_new, has_constant='add')

forecast_2024 = model.predict(X_new)[0]
print(f"Прогноз первичного баланса на 2024 год: {forecast_2024:.3f} % ВВП")

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['PrimaryBalance'], marker='o', label='Фактический первичный баланс')
plt.plot([2024], [forecast_2024], marker='X', markersize=10, label='Прогноз 2024', linestyle='--')

plt.axhline(0, linestyle=':')
plt.xlabel('Год')
plt.ylabel('Первичный баланс, % ВВП')
plt.title('Первичный баланс Германии: факт и прогноз по модели')
plt.legend()
plt.tight_layout()
plt.show()