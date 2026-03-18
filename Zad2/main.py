import numpy as np

# Zad 1

# macierz_a = np.array([1, 2, 3])
# macierz_b = np.array([4, 5, 6])
#
# wynik = macierz_a * macierz_b
# print(f"a: {macierz_a}")
# print(f"b: {macierz_b}")
# print(f"wynik: {wynik}")

# Zad 2

# macierz_3x3 = np.random.randint(10, 51, size=(3, 3))
# macierz_4x4 = np.random.randint(10, 51, size=(4, 4))
#
# print(f"3x3:\n {macierz_3x3}")
# print(f"4x4:\n {macierz_4x4}")
#
# print(f"Najniżesze wartości w kolumnach macirzy 3x3: {np.min(macierz_3x3, axis=0)}")
# print(f"Najniżesze wartości w rzędach macirzy 3x3: {np.min(macierz_3x3, axis=1)}")
#
# print(f"Najniżesze wartości w kolumnach macirzy 4x4: {np.min(macierz_4x4, axis=0)}")
# print(f"Najniżesze wartości w rzędach macirzy 4x4: {np.min(macierz_4x4, axis=1)}")

# Zad 3

# macierz_b = np.array([4, 5, 6])
# macierz_a = np.array([1, 2, 3])
#
# iloczyn_skalarny = np.dot(macierz_a, macierz_b)
# print(f"Iloczyn skalarny: {iloczyn_skalarny}")

# Zad 4

# macierz_a = np.array([1, 2, 3], dtype=int)
# macierz_b = np.array([1.2, 2.4, 3.6], dtype=float)
#
# print(f"Mnożenie macierzy: {macierz_a * macierz_b}")

# Zad 5

# macierz_a = np.random.randint(1, 101, size=(2, 3))
# print(f"Macierz:\n {macierz_a}")
# a = np.sin(macierz_a)
# print(f"Wynik sinusa:\n {a}")

# Zad 6

# macierz_a = np.random.randint(1, 101, size=(2, 3))
# print(f"Macierz:\n {macierz_a}")
# b = np.cos(macierz_a)
# print(f"Wynik cos:\n {b}")

# Zad 7

# macierz_a = np.random.randint(1, 101, size=(2, 3))
# a = np.sin(macierz_a)
# b = np.cos(macierz_a)
# print(f"Macierz a:\n {a}")
# print(f"Macierz b:\n {b}")
# print(f"Wynik dodawania macierzy: \n {a + b}")

# Zad 8

# macierz_a = np.random.randint(1, 101, size=(3, 3))
# for rzad in macierz_a:
#     print(rzad)

# Zad 9

# macierz_a = np.random.randint(1, 101, size=(3, 3))
# for i in macierz_a.ravel():
#     print(i)

# Zad 10

# macierz_a = np.random.randint(1, 101, size=(9, 9))
# print(f"Zmieniona macierz: {macierz_a.reshape((3, 27))}")
# Jedyna możliwośc zmiany tej macierzy jest taka aby po pomnożeniu długości macierzy oraz jej szerokości musi ona być taka sama jak pierwotna macierz, tzn. 9 * 9 = 81, więc aby użyć reshape musimy dobrać takie wartości aby powstała tablica też miała 81 elementów np. 3 * 27

# Zad 11

# macierz_a = np.random.randint(1, 101, size=(1, 12))
# macierz3x4 = macierz_a.reshape(3, 4)
# macierz4x3 = macierz_a.reshape(4, 3)
# macierz2x6 = macierz_a.reshape(2, 6)
# print(f"Spłaszczone 3x4:\n {macierz3x4.ravel()}")
# print(f"Spłaszczone 4x3:\n {macierz4x3.ravel()}")
# print(f"Spłaszczone 2x6:\n {macierz2x6.ravel()}")