# Zadanie 1 – Głębokość rekursji w sortowaniu przez scalanie 🧩 (4 punkty)
#
# Strategia „dziel i zwyciężaj” polega na rozbijaniu problemu na mniejsze podproblemy aż do osiągnięcia przypadków bazowych . W algorytmie merge sort tablica jest wielokrotnie dzielona na dwie części, tworząc drzewo rekurencji.
#
# Zaimplementuj funkcję:
#
# def merge_sort_profile(n: int) -> list[list[int]]:
#
# która zwraca profil rekurencji dla sortowania przez scalanie, czyli listę poziomów drzewa rekurencji.
#
# Każdy poziom powinien zawierać rozmiary wszystkich podproblemów powstałych na danym etapie dzielenia.
#
#     Na poziomie 0 znajduje się jeden element: [n]
#     Każdy element k > 1 dzielony jest na:
#         ⌊k/2⌋ oraz ⌈k/2⌉
#     Podział powtarzamy aż wszystkie podproblemy mają rozmiar 1
#     Poziomy należy zwrócić w kolejności od góry drzewa (od największego problemu)
#
# Wejście
#
#     n — liczba elementów (n ≥ 1)
#
# Wyjście
#
#     lista list liczb całkowitych — każdy wewnętrzny wektor to jeden poziom rekurencji
#
# Przykłady
#
# merge_sort_profile(1)
# # [[1]]
#
# merge_sort_profile(4)
# # [[4],
# #  [2, 2],
# #  [1, 1, 1, 1]]
#
# merge_sort_profile(5)
# # [[5],
# #  [2, 3],
# #  [1, 1, 1, 2],
# #  [1, 1]]

from typing import List, Tuple
from utils import parse_input
import os
import sys
import math

'''
Złożoność czasowa algorytmu:
Pętla while wykona się ceil(log_2(n)) razy, ilość wywołań pętli for zależy od długości
tablicy zawierającej elementy poprzedniego poziomu drzewa rekurencji; liczba 
elementów dla kolejnych poziomów drzewa rekurencyjnego rośnie wykładniczo -
tablica dla każdego kolejnego poziomu drzewa ma w przybliżeniu 2 razy więcej
elementów (1 + 2 + 4 + 8 + ...) - uzyskujemy sumę wyrazów ciągu 
geometrycznego o ilorazie q = 2 oraz pierwszym elemencie a = 1. 
Suma wszystkich wyrazów w takim ciągu wynosi dokładnie 2n−1 - własność drzewa
binarnego, jeżeli dane jest n, które jest liczbą liści. Z tych faktów wynika,
że złożoność czasowa tego algorytmu jest równa asymptotycznie O(n) i θ(n)

Złożoność pamięciowa algorytmu:
Złożoność pamięciowa działa analogicznie do złożoności czasowej, dla przypadku
pesymistycznego wynosi O(n) (liczba elementów tablicy result wynosi 2n-1) i
θ(n)
'''


def merge_sort_profile(n: int) -> list[list[int]]:
    result = [[n]]  # dla n >= 1 możemy od razu dodać element na poziomie 0
    while n > 1:  # pętla działa dopóki n > 1 (drzewo wywołań będzie miało rozmiar ceil(log_2(n)) - zapewnia nam to n/2
        arr = []  # w pętli while tworzę pustą tablicę, w której będą przechowywane elementy po podziale
        for i in result[
            -1]:  # wywołana zostaje pętla dla ostatniej podtablicy wywołań - przechodzimy po wszystkich elementach tej podtablicy i wywołujemy dwa podziały
            if i != 1:  # jeżeli element jest równy 1 to nie wywołujemy kolejnych podziałów - jest to warunek zakończenia rekurencji w procedurze merge
                left = math.floor(
                    i / 2)  # rozmiar lewego podproblemu, zgodnie z poleceniem dla n nieparzystego lewa tablica jest tą mniejszą - stąd funkcja floor()
                right = math.ceil(
                    i / 2)  # rozmiar prawego podproblemu, dla n nieparzystego prawa tablica jest tą większą, stąd funkcja ceil()
                arr.append(left)  # dodaj element lewy do tablicy wywołań dla danego poziomu
                arr.append(right)  # dodaj element prawy do tablicy wywołań dla danego poziomu
        n /= 2  # przypisujemy n wartość n/2 - ze względu na warunek zakończenia pętli i wysokości drzewa wywołań ceil(log_2(n))
        result.append(
            arr)  # tablicę wywołań dla danego poziomu dodajemy do wynikowej tablicy przechowującej tablice elementów dla danego poziomu wywołań procedury merge

    return result  # zwracam wynikową tablicę wywołań

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
