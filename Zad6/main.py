import numpy as np
import pandas as pd

# Numpy

# tablica = np.array([[0, 1, 2, 3], [10, 11, 12, 13], [40, 41, 42, 43]])
#
# # 1
#
# srednia_wierszy = np.mean(tablica, axis=1)
# print(f"Srednia wartosc dla kazdego wiersza: {srednia_wierszy}")
#
# # 2
#
# tablica[0:3, 1] = -3
# tablica[0:2] = -3
# print(f"Macierz ze zmieniona wartoscia: \n{tablica}")
#
# # 3
#
# suma = np.sum(tablica > 25)
# print(f"Liczba elementow wiekszych niz 25: {suma}")
#
# # 4
#
# tablica[tablica % 2 == 0] = 0
# print(f"Macierz z liczbami parzystymi = 0: \n{tablica}")
#
# # 5
#
# macierz_7x7 = np.zeros((7, 7), dtype=int)
# np.fill_diagonal(macierz_7x7, 3)
# macierz_7x7[0, 5] = -1
# macierz_7x7[1, 6] = -1
# macierz_7x7[5, 0] = -1
# macierz_7x7[6, 1] = -1
# print(f"Macierz: \n{macierz_7x7}")

# Pandas

powtorzenie = pd.read_csv('powtorzenie.csv', sep=';')

# 1

powtorzenie = powtorzenie[['imie', 'wiek', 'wynik']]
print(powtorzenie)

# 2

sredni_wynik = powtorzenie[powtorzenie['wiek'] > 20]['wynik'].mean()
print(f"Sredni wynik dla osob powyzej 20 lat: {sredni_wynik}")

# 3

powtorzenie['test_zaliczony'] = powtorzenie['wynik'] >= 50
print(powtorzenie)

# 4

srednia_wieku = powtorzenie.groupby('test_zaliczony')['wiek'].mean()
print(srednia_wieku)

# 5

najmlodsi = powtorzenie[powtorzenie['test_zaliczony'] & (powtorzenie['wiek'] == powtorzenie[powtorzenie['test_zaliczony']]['wiek'].min())][['imie']]
print(najmlodsi)