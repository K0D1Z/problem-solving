# Zadanie 2 – Minimalne m bez kolizji (4 punkty)
#
# Masz daną tablicę różnych liczb całkowitych keys.
#
# Rozważ funkcję haszującą:
#
# h(k) = k mod m
#
# Zaimplementuj funkcję: def minimal_m(keys: list[int]) -> int:
#
# która zwraca najmniejsze dodatnie m, takie że funkcja h(k) = k mod m jest bezkolizyjna dla wszystkich kluczy.
# Wejście
#
#     keys — lista unikalnych liczb całkowitych
#     1 ≤ n ≤ 10^5
#     0 ≤ keys[i] ≤ 10^9
#
# Wyjście
#
#     najmniejsze m > 0, takie że:
#
#     k1 % m != k2 % m   dla każdych k1 ≠ k2
#
# Przykład 1
#
# keys = [1, 2, 3]
#
# Output: 3
#
# Przykład 2
#
# keys = [10, 20, 30]
#
# Output: 3
#
# Przykład 3
#
# keys = [1, 5, 11]
#
# Output: 7
#
# Wyjaśnienie:
#
#     m = 3 -> kolizja (5 mod 3 = 2, 11 mod 3 = 2).
#
#     m = 4 -> kolizja (1 mod 4 = 1, 5 mod 4 = 1).
#
#     m = 5 -> kolizja (1 mod 5 = 1, 11 mod 5 = 1).
#
#     m = 6 -> kolizja (5 mod 6 = 5, 11 mod 6 = 5).
#
#     m = 7 nie ma kolizji.

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
Złożoność czasowa:
Wewnętrzna pętla przechodzi zawsze n razy, gdzie n to długość przekazanej
listy. Algorytm wykonuje tę pętle do momentu, kiedy nie znajdziemy prawidłowego
m (oznaczmy je jako M). Pętla while wykona się zatem M - m + 1 razy.
Zatem złożoność w najgorszym wypadku wyniesie
O(n*(M-m+1)) - dość nietypowa złożoność

Złożoność pamięciowa:
Algorytm tworzy nowy set na wyliczone hashe, który najgorszym przypadku
jeśli chodzi o pamięć (czyli w naszym przypadku podczas iteracji pętli,
kiedy znajdujemy w końcu prawidłowe m) przyjmuje n elementów - złożoność
zatem to O(n). W pojedynczych przypadkach algorytm może przyjąć tylko jeden
element - gdy np. dwa pierwsze elementy dla danego m mają identyczny hash
"""


def h(k: int, m: int) -> int:
    return k % m


def minimal_m(keys: list[int]) -> int:
    m = len(keys)  # m nie może być mniejsze od długości listy przekazanej w argumencie
    while True:
        # tworzę oddzielny set na wyliczone hashe dla każdej z wartości w liście keys
        set_of_hashes = set()
        for k in keys:
            value = h(k, m)
            if value in set_of_hashes:  # jeżeli wartość już jest w set_of_hashes - to nie jest szukane m - wychodzimy z pętli
                break
            set_of_hashes.add(value)  # w przeciwnym wypadku dodajemy wartość do set_of_hashes
        else:
            return m  # jeżeli przeszliśmy przez całą pętle - to znaczy że wszystkie wartości są unikalne, zwracamy m
        m += 1  # w przeciwnym wypadku sprawdzamy dla m o jeden większego


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