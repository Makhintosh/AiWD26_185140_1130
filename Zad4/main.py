import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./datasets/imiona.xlsx')

# Zad 1

# urodzenia_na_rok = df.groupby('Rok')['Liczba'].sum()
# plt.plot(urodzenia_na_rok.index, urodzenia_na_rok.values, marker = 'o')
# plt.title('Liczba urodzonych dzieci w poszczegolnych latach')
# plt.xlabel('Rok')
# plt.ylabel('Liczba narodzin')
# plt.grid(True)
# plt.xticks(urodzenia_na_rok.index, rotation=45)
# plt.tight_layout()
# plt.show()

# Zad 2

# urodzenia_wdlug_plci = df.groupby('Plec')['Liczba'].sum()
# etykiety = ['K', 'M']
# wartosci = [urodzenia_wdlug_plci.get('K'), urodzenia_wdlug_plci.get('M')]
# kolory = ['purple', 'yellow']
# plt.bar(etykiety, wartosci, color=kolory)
# plt.xlabel('Plec')
# plt.ylabel('Liczba narodzin')
# plt.show()

# Zad 3

# najnowszy_rok = df['Rok'].max()
# ostatnie_5_lat = list(range(najnowszy_rok - 4, najnowszy_rok + 1))
# df_5_lat = df[df['Rok'].isin(ostatnie_5_lat)]
# urodzenia_wedlug_plci_5_lat = df_5_lat.groupby('Plec')['Liczba'].sum()
# kolory = ['blue' if p == 'K' else 'orange' for p in urodzenia_wedlug_plci_5_lat.index]
# plt.pie(urodzenia_wedlug_plci_5_lat, labels=urodzenia_wedlug_plci_5_lat.index, colors=kolory, autopct='%1.1f%%')
# plt.title(f'Całkowita liczba urodzonych chłopców i dziewczynek w latach {ostatnie_5_lat[0]} - {ostatnie_5_lat[-1]}')
# plt.show()

# Zad 4