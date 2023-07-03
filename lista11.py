# 1
A = [[1, 2], [3, 4]]
print(A)
print(A[0])
print(A[1])

print('\n')
# 2
def zera(a, b):
    A = [[0 for i in range(a)] for j in range(b)]
    return A


def id(n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i] = 1
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


a  = int(input('Wprowadź wymiar a: '))
b = int(input('Wprowadź wymiar b: '))
n = int(input('Wprowadź wymiar macierzy jednostkowej: '))
wyswietl(zera(a, b))
print('\n')
wyswietl(id(n))

print('\n')
# 3
import random
def losowa(a, b, n):
    A = [[random.randint(1, n) for i in range(a)] for j in range(b)]
    return A


def dodaj(A, B):
    W = []
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        W = [[A[j][i] + B[j][i] for i in range(len(A[0]))] for j in range(len(A))]
        return W
    else:
        return W



def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


a = int(input('Ilość kolumn macierzy A: '))
b = int(input('Ilość wierszy macierzy A: '))
n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(a, b, n)
a = int(input('Ilość kolumn macierzy B: '))
b = int(input('Ilość wierszy macierzy B: '))
n = int(input('Górna granica losowanych liczb macierzy B: '))
B = losowa(a, b, n)
wyswietl(A)
print('\n')
wyswietl(B)
print('\n')
wyswietl(dodaj(A, B))

print('\n')
# 4
import random


def losowa(a, b, n):
    A = [[random.randint(1, n) for i in range(a)] for j in range(b)]
    return A


def dodaj(A, B):
    W = []
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        W = [[A[j][i] + B[j][i] for i in range(len(A[0]))] for j in range(len(A))]
        return W
    else:
        return W


def pomnoz(A, B):
    W = []
    iloscwierszy = int(len(A))
    ilosckolumn = int(len(A[0]))
    if iloscwierszy == len(B) and ilosckolumn == len(B[0]):
        W = [[0 for i in range(ilosckolumn)] for j in range(iloscwierszy)]
        for i in range(iloscwierszy):
            for k in range(ilosckolumn):
                iloczyn = 0
                for j in range(ilosckolumn):
                    iloczyn += A[i][j]*B[j][k]
                W[i][k] = iloczyn
        return W
    else:
        return W


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


a = int(input('Ilość kolumn macierzy A: '))
b = int(input('Ilość wierszy macierzy A: '))
n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(a, b, n)
a = int(input('Ilość kolumn macierzy B: '))
b = int(input('Ilość wierszy macierzy B: '))
n = int(input('Górna granica losowanych liczb macierzy B: '))
B = losowa(a, b, n)
wyswietl(A)
print('\n')
wyswietl(B)
print('\n')
wyswietl(dodaj(A, B))
print('\n')
wyswietl(pomnoz(A, B))

print('\n')
#5
import random


def losowa(a, b, n):
    A = [[random.randint(1, n) for i in range(a)] for j in range(b)]
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


def zamW(A, i, j):
    kopia = []
    for k in range(len(A[0])):
        kopia.append(A[i][k])
        A[i][k] = A[j][k]
        A[j][k] = kopia[k]
    return A


def przemW(A, i, k):
    for l in range(len(A)):
        A[i][l] *= k
    return A


def dodajW(A, i, j ,k):
    for l in range(k):
        for a in range(len(A[0])):
            A[i][a] += A[j][a]
    return A


a = int(input('Ilość kolumn macierzy A: '))
b = int(input('Ilość wierszy macierzy A: '))
n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(a, b, n)
wyswietl(A)
wiersz = int(input('Numer wiersza do zamiany:'))
drugiwiersz = int(input('Numer drugiego wiersza do zamiany:'))
wyswietl(zamW(A, wiersz, drugiwiersz))
wiersz = int(input('Numer wiersza do przemnożenia:'))
czynnik = int(input('Podaj czynnik:'))
wyswietl(przemW(A, wiersz, czynnik))
wiersz = int(input('Numer wiersza do sumowania:'))
drugiwiersz = int(input('Numer wiersza dodawanego:'))
n = int(input('Ilość powtórzeń dodawania:'))
wyswietl(dodajW(A, wiersz, drugiwiersz, n))

print('\n')
#6
import random
import numpy as num


def losowa(a, b, n):
    A = [[random.randint(1, n) for i in range(a)] for j in range(b)]
    return A


def wyswietl(A):
    for i in range(len(A)):
        print(A[i])


def det(A):
    wyznacznik = num.linalg.det(A)
    return wyznacznik


a = int(input('Ilość kolumn macierzy A: '))
b = int(input('Ilość wierszy macierzy A: '))
n = int(input('Górna granica losowanych liczb macierzy A: '))
A = losowa(a, b, n)
wyswietl(A)
print("\n")
print(det(A))