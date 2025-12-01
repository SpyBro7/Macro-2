import pandas as pd
import matplotlib.pyplot as plt

years = list(range(1999, 2024))
crisis_dummy = [0]*len(years)

crisis_years = [2009, 2010, 2020, 2021]
for year in crisis_years:
    if year in years:
        idx = years.index(year)
        crisis_dummy[idx] = 1

df_crisis = pd.DataFrame({
    'Year': years,
    'Crisis_Dummy': crisis_dummy
})

plt.figure(figsize=(14, 4))

plt.step(df_crisis['Year'], df_crisis['Crisis_Dummy'],
         where='post', linewidth=2.5, color='crimson')

plt.title('Кризисная дамми-переменная',
          fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Год', fontsize=12)
plt.ylabel('Crisis_Dummy (0/1)', fontsize=12)

plt.axvline(x=2011, color='red', linestyle='--', alpha=0.7, linewidth=1.5,
            label='Введение Schuldenbremse (2011)')

for i, row in df_crisis.iterrows():
    if row['Crisis_Dummy'] == 1:
        plt.axvspan(row['Year']-0.5, row['Year']+0.5,
                   alpha=0.2, color='red', zorder=0)

plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)

plt.yticks([0, 1], ['0 (Норма)', '1 (Кризис)'])
plt.ylim(-0.1, 1.5)

plt.xticks(range(1999, 2024, 2), rotation=45)
plt.xlim(1998, 2024)

crisis_periods = [
    (2009, 2010, 'Мировой финансовый\nкризис и его\nпоследствия'),
    (2020, 2021, 'Пандемия COVID-19\nи энергетический\nкризис')
]

for start, end, label in crisis_periods:
    plt.annotate(label, xy=((start+end)/2, 1.2),
                 xytext=(0, 10), textcoords='offset points',
                 ha='center', va='bottom', fontsize=9,
                 bbox=dict(boxstyle="round,pad=0.3",
                          facecolor="white", alpha=0.8, edgecolor='gray'))

plt.legend(loc='upper left', fontsize=10)

plt.grid(True, linestyle='--', alpha=0.3, axis='x')
plt.tight_layout()

plt.savefig('crisis_dummy_germany.png', dpi=300, bbox_inches='tight')
plt.show()