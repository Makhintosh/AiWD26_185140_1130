import pandas as pd
import numpy as np

# Zad 1

df = pd.read_excel('./datasets/imiona.xlsx')

# Zad 2

# a)

a = df[df['Liczba'] > 1000]
# print(a)

# b)

b = df[df['Imie'].str.upper() == 'igor'.upper()]
# print(b)

# c)

c = df['Liczba'].sum()
# print(c)

# d)

d = df.groupby('Rok')['Liczba'].sum()
# print(d)

# e)

e = df[df['Rok'].between(2000, 2005)].groupby('Rok')['Liczba'].sum()
# print(e)

# f)

f = df.groupby('Plec')['Liczba'].sum()
# print(f)

# g)

g = df.groupby(['Plec', 'Imie'], as_index=False)['Liczba'].sum()
# print(g.loc[g.groupby('Plec')['Liczba'].idxmax()])

# h)

h = df.loc[df.groupby(['Rok', 'Plec'])['Liczba'].idxmax()][['Imie', 'Rok']]
# print(h)

# Zad 3

