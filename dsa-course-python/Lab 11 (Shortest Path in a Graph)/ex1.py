# Zadanie 1: Szukanie największego oka w rosole 🍜
#
# Dana jest macierz broth_grid, reprezentująca miskę rosołu widzianą z góry. Każda komórka macierzy przyjmuje wartość albo 1 (oznaczająca tłuszcz na powierzchni), albo 0 (oznaczająca czysty bulion).
#
# Oko rosołowe to zbiór połączonych ze sobą komórek tłuszczu. Dwie komórki tłuszczu są połączone, jeśli stykają się ze sobą poziomo lub pionowo (sąsiedztwo von Neumanna). Czysty bulion (komórki '0') oddziela poszczególne oczka.
#
# Zaimplementuj funkcję get_max_area_of_drops_of_fat(broth_grid: List[List[int]]) -> int, która przyjmie macierz broth_grid, reprezentującą miskę rosołu i zwraca maksymalne pole oka tłuszczu pływającego w tym rosole.
#
# 💡 Można dodawać własne funkcje pomocnicze.
#
# ⚠️ Określ czasową złożoność obliczeniową Twojego rozwiązania (wraz z uzasadnieniem) jako komentarz na początku implementowanej funkcji. ⚠️
# Przykłady
#
# ✅ Przykład 1: Wejście:
#
# get_max_area_of_drops_of_fat=[
#     [1, 0, 0],
#     [1, 0, 0],
#     [1, 0, 0]
# ]
#
# Poprawne wyjście: 3
#
# ✅ Przykład 2: Wejście:
#
# get_max_area_of_drops_of_fat=[
#     [0, 0, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 0],
#     [1, 0, 0, 1]
# ]
#
# Poprawne wyjście: 2 Wyjaśnienie: komórka tłuszczu w prawym donym rogu nie styka się w pionie lub w poziomie z dwu-komórkowym okiem nad nią.

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
WSZYSTKIE ZŁOŻONOŚCI BĘDĄ DOKŁADNIE TAKIE SAME JAK W ZADANIU Z POPRZEDNIEGO
LABU - DLATEGO ZROBIŁEM KOPIUJ-WKLEJ ŻEBY ZNOWU NIE PISAĆ ROZPRAWKI :)

Złożoność czasowa rozwiązania:
Niezależnie od przypadku mamy podwójną pętlę for,
mamy zatem O(i*j) na pewno. DFS na pewno wykona się no najwyżej 1
raz dla pojedynczego indeksu, w przypadku pesymistycznym DFS wykona
się dla każdego indeksu w tablicy. Wtedy sumaryczna złożonośc 
czasowa będzie wynosiła O(i*j) + O(i*j) = O(i*j), gdzie
i - liczba wierszy, j - liczka kolumn

Złożoność pamięciowa rozwiązania:
Tworzymy 3 inty - O(1), tablicę dwuwymiarową row x col tylko
modyfikujemy, nie tworzymy tablicy pomocniczej - ale 
wywołujemy rekurencyjnie dfs - w najgorszym wypadku na stosie
w jednym momencie będzie i*j wywołań rekurencyjnych funkcji dfs
gdzie i - liczba wierszy, j - liczba kolumn np.
gdy oko rosołowe zajmuje cały wiersz.
Zatem złożoność pesymistyczna pamięciowa tego rozwiązania
to O(i*j).
"""


def dfs(row: int, col: int, global_rows: int, global_cols: int, broth_grid: List[List[int]]) -> int:
    if row < 0 or row >= global_rows or col < 0 or col >= global_cols:
        return 0  # zabezpieczenie przed wyjściem poza tablicę
    if broth_grid[row][col] == 0:
        return 0  # komórka jest już odwiedzona lub jest czystym bulionem
    broth_grid[row][col] = 0  # oznacz jako odwiedzoną
    # rekurencyjnie sumujemy bieżącą komórkę (1) oraz wyniki z sąsiedztwa von Neumanna
    area = 1
    area += dfs(row - 1, col, global_rows, global_cols, broth_grid)
    area += dfs(row + 1, col, global_rows, global_cols, broth_grid)
    area += dfs(row, col - 1, global_rows, global_cols, broth_grid)
    area += dfs(row, col + 1, global_rows, global_cols, broth_grid)
    return area


def get_max_area_of_drops_of_fat(broth_grid: List[List[int]]) -> int:
    if not broth_grid:
        return 0  # zabezpieczenie przed pustą listą
    rows = len(broth_grid)
    cols = len(broth_grid[0])
    max_count = 0  # liczymy max rozmiar
    for i in range(rows):
        for j in range(cols):
            if broth_grid[i][j] == 1:
                temp = dfs(i, j, rows, cols, broth_grid)
                if temp > max_count:
                    max_count = temp
    return max_count


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