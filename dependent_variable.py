import pandas as pd
import matplotlib.pyplot as plt

years = list(range(1999, 2024))
values = [
    0.925, 1.060, -0.524, -1.457, -1.211, -0.900, -0.929, 0.628, 2.554, 2.070,
    -0.831, -2.289, 1.156, 1.781, 1.555, 1.960, 1.996, 2.066, 2.170, 2.607,
    1.918, -3.916, -2.703, -1.348, -1.850
]

df = pd.DataFrame({'Year': years, 'Primary_Balance': values})

plt.figure(figsize=(14, 7))

plt.plot(df['Year'], df['Primary_Balance'],
         marker='o', linewidth=2.5, markersize=6,
         color='#1f77b4', label='Первичный баланс (% ВВП)')

plt.title('Динамика первичного баланса бюджета Германии до и после введения Schuldenbremse\n(1999–2023 гг.)',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Первичный баланс, % ВВП', fontsize=12)

plt.axvline(x=2011, color='red', linestyle='--', linewidth=2, alpha=0.8,
            label='Введение правила Schuldenbremse (2011)')

plt.axvspan(1999, 2010, alpha=0.1, color='gray', label='До введения правила')

plt.axvspan(2011, 2023, alpha=0.1, color='lightgreen', label='После введения правила')


plt.axhline(y=0, color='black', linewidth=0.8, linestyle='-', alpha=0.5)


plt.fill_between(df['Year'], df['Primary_Balance'], 0,
                 where=(df['Primary_Balance'] < 0),
                 color='red', alpha=0.1, label='Дефицит бюджета')
plt.fill_between(df['Year'], df['Primary_Balance'], 0,
                 where=(df['Primary_Balance'] > 0),
                 color='green', alpha=0.1, label='Профицит бюджета')


plt.grid(True, linestyle='--', alpha=0.3)
plt.xticks(range(1999, 2024, 2), rotation=45)
plt.xlim(1998, 2024)


plt.legend(loc='upper left', fontsize=10, framealpha=0.9)

plt.tight_layout()
plt.savefig('primary_balance_germany_schuldenbremse.png', dpi=300, bbox_inches='tight')
plt.show()