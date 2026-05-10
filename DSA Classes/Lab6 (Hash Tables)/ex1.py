# Zadanie 1 – Czy kolejność była możliwa? (4 punkty)
#
# Masz daną końcową postać tablicy haszującej o rozmiarze m, która została zbudowana przy użyciu:
#
#     funkcji haszującej:
#     h(k) = k mod m
#     adresowania liniowego:
#     h(k, i) = (h(k) + i) mod m
#
# Tablica była początkowo pusta, a następnie wstawiano do niej kolejne klucze (bez duplikatów).
#
# Zaimplementuj funkcję: def is_valid_insertion_order(table: list[int | None]) -> bool:
#
# która sprawdza, czy istnieje jakakolwiek kolejność wstawiania kluczy, która mogła doprowadzić do podanego końcowego stanu tablicy.
# Wejście
#
#     table — lista długości m
#     Każdy element to:
#         liczba całkowita k (klucz), albo
#         None (puste miejsce)
#
# Wyjście
#
#     True — jeśli istnieje poprawna kolejność wstawiania
#     False — jeśli taki stan tablicy jest niemożliwy
#
# Założenia
#
#     Wstawianie odbywa się zgodnie z zasadą:
#         zaczynamy od h(k)
#         jeśli miejsce zajęte → próbujemy kolejne (h(k)+1) mod m, itd.
#     Nie było usuwania elementów.
#     Wszystkie klucze są unikalne.
#     1 ≤ m ≤ 10^5
#
# Przykład 1
#
# table = [20, 12, None, None]
#
# h(20) = 0 → trafia na 0
# h(12) = 0 → zajęte → trafia na 1
#
# Output: True
#
# Przykład 2
#
# table = [None, 21, 12, None]
#
# Output: False
#
# (brak kolejności, która daje taki układ)

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
    Złożoność czasowa: O(n^2) - mamy dwie pętle for, które w najgorszym przypadku
    będą musiały przejść po całej tablicy. Pierwsza pętla for, która sprawdza
    czy żaden element nie przeskoczył przez puste miejsce w tablicy nie 
    zmienia asymptotycznie złożoności algorytmu.

    Złożonośc pamięciowa: O(n) - wykorzystuję dodatkową tablicę current_table o
    długości n
"""


def h1(k: int, m: int) -> int:
    return k % m


def h2(k: int, i: int, m: int) -> int:
    return (h1(k, m) + i) % m


def is_valid_insertion_order(table: list[int | None]) -> bool:
    m = len(table)
    current_table = list(table)

    # sprawdzami, czy żaden element nie przeskoczył przez puste miejsce z wartością None
    for i in range(m):
        if current_table[i] is None:
            continue
        hash_i = h1(current_table[i], m)

        while hash_i != i:
            # jeżeli po drodze znajdziemy None, to element nie mógł dotrzeć do faktycznej pozycji na indeksie i
            if current_table[hash_i] is None:
                return False  # gdy znajdziemy taki przypadek, od razu wiemy, że nie jest to poprawna tablica
            hash_i = (hash_i + 1) % m  # liczymy hash za pomocą drugiej funkcji (tutaj ją trochę uprościłem)

    # liczymy ile kluczy jest do usunięcia
    sum_of_keys_to_remove = sum((1 for x in current_table if x is not None))

    while sum_of_keys_to_remove > 0:
        is_found = False

        # szukam ostatniego klucza
        for i in range(m):
            if current_table[i] is None:
                continue

            can_be_last = True  # zakładamy, że element mógł być wstawiony na końcu
            # jeżeli element był wstawiony na końcu to musimy udowodnić, że jego obecność nie była niezbędna dla innych elementów
            for j in range(m):
                key_j = current_table[j]
                if i == j or key_j is None:
                    continue

                # sprawdzamy, czy dany element j nie musiał przejść przez element i, aby dotrzeć na swoje miejsce
                hash_j = h1(key_j, m)
                distance_hash_j_to_j = (
                                               j - hash_j) % m  # obliczam drogę, którą musiał pokonać element j z miejsca hash_j do miejsca j, używam modulo przy zawijaniu elementu na koniec tablicy
                distance_hash_j_to_i = (
                                               i - hash_j) % m  # obliczam drogę, którą musiał pokonać element i z miejsca hash_j do miejsca i, używam modulo przy zawijaniu elementu na koniec tablicy

                if distance_hash_j_to_j > distance_hash_j_to_i:  # jeżeli dystans j jest większy od dystansu i, to indeks i leży na trasie przemieszczenia elementu j - i nie mógł być dodany jako ostatni
                    can_be_last = False
                    break

            if can_be_last:  # w przypadku, gdy element był ostatni, możemy go bezpiecznie usunąć i zmniejszyć liczbę elementów do sprawdzenia
                current_table[i] = None
                sum_of_keys_to_remove -= 1
                is_found = True
                break

        # jeżeli nie znaleźliśmy elementu, który był ostatni (przeszliśmy całą tablicę) - utknęliśmy w cyklu - zwracamy False bo układ się już nie uprości
        if not is_found:
            return False

    return True  # jeżeli usunęliśmy wszystkie elementy z tablicy, zwracamy True - układ jest możliwy do osiągnięcia

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
