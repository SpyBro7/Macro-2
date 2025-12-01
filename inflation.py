import pandas as pd
import matplotlib.pyplot as plt

years = list(range(1999, 2024))
inflation_values = [
    0.647, 1.413, 1.900, 1.326, 1.074, 1.780, 1.928, 1.775, 2.271, 2.754,
    0.246, 1.119, 2.482, 2.159, 1.607, 0.769, 0.680, 0.367, 1.702, 1.935,
    1.354, 0.371, 3.212, 8.666, 6.030
]

df = pd.DataFrame({'Year': years, 'Inflation': inflation_values})

plt.figure(figsize=(14, 6))

plt.plot(df['Year'], df['Inflation'],
         marker='o', linewidth=2.5, markersize=6,
         color='darkorange', label='Инфляция (ИПЦ, % г/г)')

plt.title('Динамика инфляции',
          fontsize=15, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Изменение ИПЦ, % (г/г)', fontsize=12)

plt.axhline(y=2.0, color='red', linestyle=':', linewidth=1.5, alpha=0.7,
            label='Целевой уровень инфляции ЕЦБ (~2%)')

plt.axvline(x=2011, color='blue', linestyle='--', linewidth=1.5, alpha=0.7,
            label='Введение Schuldenbremse (2011)')

high_inflation_years = df[df['Year'] >= 2022]
plt.fill_between(high_inflation_years['Year'], high_inflation_years['Inflation'], 2,
                 where=(high_inflation_years['Inflation'] > 2),
                 color='red', alpha=0.2, label='Высокая инфляция (2022-2023)')

plt.grid(True, linestyle='--', alpha=0.3)
plt.xticks(range(1999, 2024, 2), rotation=45)
plt.xlim(1998, 2024)
plt.ylim(-0.5, 10)

max_inflation = df.loc[df['Inflation'].idxmax()]
plt.annotate(f'Пик: {max_inflation["Inflation"]}%',
             xy=(max_inflation['Year'], max_inflation['Inflation']),
             xytext=(max_inflation['Year']-1, max_inflation['Inflation']+0.7),
             arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
             fontsize=10, color='red', fontweight='bold')

plt.legend(loc='upper left', fontsize=10, framealpha=0.9)

plt.tight_layout()
plt.savefig('inflation_germany_1999_2023.png', dpi=300, bbox_inches='tight')
plt.show()