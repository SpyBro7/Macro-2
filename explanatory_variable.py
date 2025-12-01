import pandas as pd
import matplotlib.pyplot as plt

years_full = list(range(1991, 2024))

output_gap_values = [
    2.537, 2.606, -0.602, -0.267, -0.646, -1.228, -0.918, -0.486, -0.038, 1.328,
    1.608, 0.381, -1.349, -1.280, -1.775, 0.447, 2.394, 2.488, -3.834, -0.973,
    1.358, 0.261, -0.809, -0.331, -0.324, 0.095, 1.040, 0.883, 0.438, -3.085,
    -0.762, 1.315, -0.217
]

df_full = pd.DataFrame({
    'Year': years_full,
    'Output_Gap': output_gap_values
})

df = df_full[df_full['Year'] >= 1999].copy()
df.reset_index(drop=True, inplace=True)

df['Post2011'] = (df['Year'] >= 2011).astype(int)

df['OG_x_Post2011'] = df['Output_Gap'] * df['Post2011']

plt.figure(figsize=(14, 7))

plt.plot(df['Year'], df['Output_Gap'],
         marker='s', linewidth=2.5, markersize=6,
         color='darkorange', label='Разрыв выпуска (Output Gap)')

plt.title('Динамика экономического цикла в Германии: разрыв выпуска (Output Gap)',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Output Gap, % от потенц. ВВП', fontsize=12)

plt.axhline(y=0, color='black', linewidth=0.8, linestyle='-', alpha=0.5)
plt.axvline(x=2011, color='red', linestyle='--', linewidth=2, alpha=0.8,
            label='Введение Schuldenbremse (2011)')

plt.fill_between(df['Year'], df['Output_Gap'], 0,
                 where=(df['Output_Gap'] >= 0),
                 color='gold', alpha=0.2, label='Выше потенциала)')
plt.fill_between(df['Year'], df['Output_Gap'], 0,
                 where=(df['Output_Gap'] < 0),
                 color='lightblue', alpha=0.3, label='Ниже потенциала)')

plt.grid(True, linestyle='--', alpha=0.3)
plt.xticks(range(1999, 2024, 2), rotation=45)
plt.xlim(1998, 2024)

plt.legend(loc='lower left', fontsize=10, framealpha=0.9)
plt.tight_layout()

plt.savefig('output_gap_germany_1999_2023.png', dpi=300, bbox_inches='tight')
plt.show()

