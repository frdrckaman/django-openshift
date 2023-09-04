import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv('data/dataset.csv'))

df_median = df['GDP'].median()
df_mean = df['GDP'].mean().round(2)
df_mode = df['GDP'].mode().values[0]

plt.boxplot(df['GDP'], vert=False)

plt.xlabel("cop (in trillions uso)")
plt.title("GDP")
plt.scatter([df_mean], [1], marker='o', color='green', label='Mean')
plt.scatter([df_median], [1], marker='o', color='yellow', label='Median')
plt.scatter([df_mode], [1], marker='o', color='orange', label='Mode')

plt.annotate(f'Mean: {df_mean}', (df_mean, 1.1), color='green')
plt.annotate(f'Median: {df_median}', (df_median, 1.0), color='yellow')
plt.annotate(f'Mode: {df_mode}', (df_mode, 1.1), color='orange')
plt.legend()
plt.show()