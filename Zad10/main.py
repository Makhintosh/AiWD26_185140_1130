import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./Pokemon.csv', index_col=0, encoding='latin')

# Zad 1

# df_filtered = df[df['Type 2'].isnull()]
# sns.set_theme(style='whitegrid')
# fig, ax = plt.subplots(figsize=(8, 6))
#
# sns.scatterplot(
#     data=df_filtered,
#     x='Attack',
#     y='Defense',
#     hue='Stage',
#     ax=ax
# )
#
# plt.title('Zaleznosc ataku do obrony pokemonow o jednym typie dla 3 roznych ewolucji')
# plt.xlabel('Atak')
# plt.ylabel('Obrona')
#
# sns.move_legend(ax, 'upper left', bbox_to_anchor=(1.01, 1))
# plt.tight_layout()
# plt.show()

# Zad 2

# pkm_type_color = ['#F08030', '#78C850', '#6890F0']
#
# typy = ['Fire', 'Grass', 'Water']
# df_task2 = df[df['Type 1'].isin(typy)]
#
# sns.set_theme(style='whitegrid')
# plt.figure(figsize=(8, 6))
#
# sns.countplot(
#     data=df_task2,
#     x='Type 1',
#     palette=pkm_type_color,
#     order=typy
# )
#
# plt.title('Liczba pokemonow typu')
# plt.xlabel('Typ pokemona')
# plt.ylabel('Liczba')
# plt.show()

# Zad 3

# legendary = df['Legendary'].replace({False:'Zwykły', True:'Legendarny'})
# pie_data = legendary.value_counts()
# colors = sns.color_palette('pastel')
# plt.figure(figsize=(7, 7))
# plt.pie(
#     x=pie_data,
#     labels=pie_data.index,
#     autopct='%1.0f%%',
#     colors=colors,
#     wedgeprops={'edgecolor':'white'}
# )
# plt.title('Procent legendarnych pokemonow')
# plt.show()

# Zad 4

