# Zadanie 1 – Dekodowanie Starożytnych Manuskryptów 📜 (4 punkty)
#
# Odkryto bibliotekę ze starożytnymi zwojami. Każdy zwój posiada unikalny identyfikator zapisany jako string w tablicy scrolls.
#
# Każdy identyfikator ma dokładnie 7 znaków w formacie:
#
# LL-DDDD
#
# gdzie:
#
#     L — wielka litera alfabetu angielskiego (A–Z)
#     - — separator
#     D — cyfra (0–9)
#
# Przykład:
#
# "AB-0123", "ZA-2023"
#
# Zaimplementuj funkcję: radixSortStep(scrolls, k) która wykonuje dokładnie k kroków sortowania pozycyjnego i zwraca tablicę po tych k krokach, gdzie k ∈ [1, 6]. Zwoje powinny być sortowane:
#
#     rosnąco według części numerycznej (DDDD) — od najmniejszej do największej
#     w przypadku remisu — leksykograficznie po części literowej (LL)
#
# Przykład:
#
#     Wejście: scrolls = ["AB-0010", "ZA-0020", "CD-0010"], k=2
#
#     Wyjście: ["AB-0010", "CD-0010", "ZA-0020"]
#
# k=2 oznacza, że należy zwrócić wynik po 2 iteracjach stabilnego sortowania

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
Złożoność czasowa: wykonywana jest standardowa procedura RadixSorta, w którym 
użyto CountingSorta jako wewnętrznego algorytmu sortowania. 
Jego złożoność wynosi w tym przypadku O(d*(b + n)), gdzie
n to liczba elementów do posortowania, b to baza (u nas 26), d - długość klucza
do posortowania (u nas 6, bo bez myślnika każdy klucz ma 7-1 elementów do porównania)
Podstawiając wartości nasza złożoność wyniesie O(6(26 + n)) co asymptotycznie da 
nam O(n). Notacje omega i theta będą identyczne, co wynika z mechaniki CountingSorta.

Złożoność pamięciowa: dla każdej iteracji algorytmu tworzone są dwie dodatkowe
tablice (jedna służąca do zliczania o długości 26, druga tablica wynikowa output 
o długości n - gdzie n to długość tablicy A przekazanej jako argument. Złożoność
pamięciowa wyniesie zatem O(n + k), gdzie n to długość tablicy wynikowej, a k
to długość tablicy do zliczania. Asymptotycznie będzie to zatem złożoność
O(n) dla n >> k. Notacje omega i theta będą identyczne, co wynika z mechaniki CountingSorta.
"""


def getIdx(character: str) -> int:
    # jeżeli character to znak alfabetu - obliczamy jego indeks, w przeciwnym przypadku indeksem jest po prostu on sam jako int
    z = 0
    if character.isalpha():
        z = ord(character.upper()) - ord('A')
    else:
        z = int(character)
    return z


def countingSort(A: list[str], k: int) -> list[str]:
    idx = len(A[0]) - k  # przechowaj obecnie sprawdzany indeks
    if idx <= 2 and idx > 0:
        idx -= 1  # przeskocz znak '-'

    C = [0 for _ in range(
        26)]  # rezerwuję 26 miejsc w tablicy C, bo alfabet angielski ma 26 liter (trochę redundantne rozwiązanie pod kątem pamięciowym)
    # co ważne rezerwuję 26 miejsc, ponieważ mam gwarancję, że na takim samym indeksie będą albo cyfry albo litery - nigdy na przemian nie wystąpią i cyfry i litery na tym samym indeksie
    for i in range(len(A)):
        z = A[i][idx]
        z = getIdx(z)
        C[z] = C[z] + 1  # liczymy powtórzenia cyfr/liter na danej pozycji łańcucha znaków

    for i in range(1, 26):
        C[i] = C[i] + C[i - 1]  # kumulacja indeksów w tablicy C

    output = [None for _ in range(len(A))]  # inicjuję tablicę wyjściową

    for i in range(len(A) - 1, -1, -1):  # pętla przechodzi od prawej do lewej strony listy
        z = A[i][idx]
        z = getIdx(z)
        C[z] = C[z] - 1  # zmniejszamy indeks o 1 bo numerujemy listy od 0
        output[C[z]] = A[i]  # przypisujemy A[i] do listy wynikowej na odpowiednim indeksie
    return output


def radixSortStep(scrolls, k) -> list[str]:
    for i in range(1,
                   k + 1):  # wykonujemy k iteracji CountingSorta, zmieniając sprawdzany indeks znaków od prawej do lewej
        scrolls = countingSort(scrolls, i)
    return scrolls  # zwracamy wynikową listę

###############################
# don't modify the code below #
###############################
# if __name__ == "__main__":
#     if "--debug" in sys.argv:
#         from run_tests import run_tests
#
#         run_tests()
#     else:
#         raw_input = parse_input(input(), os.path.abspath(__file__))
