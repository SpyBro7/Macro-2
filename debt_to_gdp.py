import pandas as pd
import matplotlib.pyplot as plt

years = list(range(1999, 2024))
debt_to_gdp = [
    60.349, 59.239, 58.062, 59.823, 63.344, 64.965, 67.120, 66.397, 63.687, 65.170,
    72.362, 81.034, 78.484, 79.835, 77.457, 74.538, 71.184, 68.301, 63.988, 60.758,
    58.682, 68.037, 67.991, 64.442, 62.382
]

df_debt = pd.DataFrame({'Year': years, 'Debt_to_GDP': debt_to_gdp})

plt.figure(figsize=(14, 7))

plt.plot(df_debt['Year'], df_debt['Debt_to_GDP'],
         marker='o', linewidth=2.5, markersize=6,
         color='purple', label='Госдолг (% ВВП)')

plt.axvline(x=2011, color='red', linestyle='--', linewidth=1.5, alpha=0.8,
            label='Введение Schuldenbremse (2011)')

plt.axhline(y=60, color='green', linestyle='-.', linewidth=1.5, alpha=0.7,
            label='Критерий Маастрихта (60% ВВП)')

plt.axvspan(2008, 2010, alpha=0.2, color='red', label='Финансовый кризис (2008-2010)')
plt.axvspan(2020, 2022, alpha=0.2, color='orange', label='Пандемия COVID-19 (2020-2022)')

max_debt = df_debt.loc[df_debt['Debt_to_GDP'].idxmax()]
plt.annotate(f'Пик: {max_debt["Debt_to_GDP"]:.1f}%',
             xy=(max_debt['Year'], max_debt['Debt_to_GDP']),
             xytext=(max_debt['Year'] - 2, max_debt['Debt_to_GDP'] + 3),
             arrowprops=dict(arrowstyle='->', color='black', alpha=0.6),
             fontsize=10, fontweight='bold')

min_debt = df_debt.loc[df_debt['Debt_to_GDP'].idxmin()]
plt.annotate(f'Минимум: {min_debt["Debt_to_GDP"]:.1f}%',
             xy=(min_debt['Year'], min_debt['Debt_to_GDP']),
             xytext=(min_debt['Year'], min_debt['Debt_to_GDP'] - 4),
             arrowprops=dict(arrowstyle='->', color='black', alpha=0.6),
             fontsize=10, fontweight='bold')

plt.title('Динамика государственного долга',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Государственный долг, % ВВП', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.3)
plt.xticks(range(1999, 2024, 2), rotation=45)
plt.xlim(1998, 2024)
plt.ylim(55, 85)

plt.legend(loc='upper left', fontsize=10, framealpha=0.9)
plt.tight_layout()

plt.savefig('germany_government_debt_1999_2023.png', dpi=300, bbox_inches='tight')
plt.show()