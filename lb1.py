import pandas as pd
import seaborn as sns

df = pd.read_csv('random_data.csv')  # Замените 'ваш_файл.csv' на путь к вашему файлу с данными

top_sites = df.groupby('site')['otz'].count().reset_index()
top_sites = top_sites.sort_values(by='otz', ascending=False).head(5)
print(top_sites)

top_curators = df.groupby('kur')['otz'].count().reset_index()
top_curators = top_curators.sort_values(by='otz', ascending=False).head(5)
print(top_curators)

sns.barplot(x='otz', y='site', data=top_sites)

sns.barplot(x='otz', y='kur', data=top_curators)
