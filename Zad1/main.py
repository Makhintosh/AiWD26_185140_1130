import numpy as np

# Zad 1

# tablica = np.arange(2, 42, 2)
# print(tablica)

# Zad 2

# lista = [1.99, 2.5, 3.14, -4.8, 5.01]
# tablica = np.array(lista, dtype=np.int64)
# print(tablica)

# Zad 3

def macierz(n):
    return np.arange(1, n*n + 1).reshape(n, n)

n = int(input("Podaj wielkosc macierzy: "))
print(macierz(n))
print(macierz(n).size)
