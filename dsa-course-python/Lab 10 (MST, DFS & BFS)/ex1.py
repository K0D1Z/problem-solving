# Zadanie 1: Szukanie największego oka w rosole 🍜
#
# Dana jest macierz broth_grid, reprezentująca miskę rosołu widzianą z góry. Każda komórka macierzy przyjmuje wartość albo 1 (oznaczająca tłuszcz na powierzchni), albo 0 (oznaczająca czysty bulion).
#
# Oko rosołowe to zbiór połączonych ze sobą komórek tłuszczu. Dwie komórki tłuszczu są połączone, jeśli stykają się ze sobą poziomo lub pionowo (sąsiedztwo von Neumanna). Czysty bulion (komórki '0') oddziela poszczególne oczka.
#
# Zaimplementuj funkcję get_nr_of_drops_of_fat(broth_grid: List[List[int]]) -> int, która przyjmie macierz broth_grid, reprezentującą miskę rosołu i zwraca całkowitą liczbę odrębnych ok tłuszczu pływających w tym rosole.
#
# 💡 Można dodawać własne funkcje pomocnicze.
#
# 💡 Hint: Użyj DFS.
#
#
# ⚠️ Określ czasową złożoność obliczeniową Twojego rozwiązania (wraz z uzasadnieniem) jako komentarz na początku implementowanej funkcji. ⚠️
# Przykłady
#
# ✅ Przykład 1:
#
# Wejście:
#
# broth_grid = [
#   [1,1,1,1,0],
#   [1,1,0,1,0],
#   [1,1,0,0,0],
#   [0,0,0,0,0]
# ]
#
# Prawidłowe wyjście: 1 Wyjaśnienie: Wszystkie '1' są ze sobą połączone, tworząc jedno duże, spójne oko.
#
# ✅ Przykład 2: Wejście:
#
# broth_grid = [
#   [1,1,0,0,0],
#   [1,1,0,0,0],
#   [0,0,1,0,0],
#   [0,0,0,1,1]
# ]
#
# Prawidłowe wyjście: 3
#
# Wyjaśnienie:
#
#     W lewym górnym rogu mamy jedno duże oko (2×2 blok '1').
#     W środku po prawej jest małe, pojedyncze oko (pojedyncza '1').
#     W prawym dolnym rogu mamy kolejne oko (1×2 blok '1').

from typing import List, Tuple
from utils import parse_input
import os
import sys

"""
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


# ważne - lista jako argument w Pythonie nie jest traktowana jak
# kopia tylko jak referencja - modyfikuję oryginalną listę
# zatem
def dfs(row: int, col: int, global_rows: int, global_cols: int, broth_grid: List[List[int]]) -> None:
    if row < 0 or row >= global_rows or col < 0 or col >= global_cols:
        return  # zabezpieczenie przed wyjściem poza tablicę
    if broth_grid[row][col] == 0:
        return  # jak komórka jest 0 nie wywołujemy już dfs
    else:
        broth_grid[row][col] = 0  # oznacz jako odwiedzona
        # wywołujemy dfs tak jak w poleceniu (sąsiedztwo von Neumanna)
        dfs(row - 1, col, global_rows, global_cols, broth_grid)
        dfs(row + 1, col, global_rows, global_cols, broth_grid)
        dfs(row, col - 1, global_rows, global_cols, broth_grid)
        dfs(row, col + 1, global_rows, global_cols, broth_grid)


def get_nr_of_drops_of_fat(broth_grid: List[List[int]]) -> int:
    if not broth_grid:
        return 0  # zabezpieczenie przed pustą listą
    rows = len(broth_grid)
    cols = len(broth_grid[0])
    count = 0  # couter liczby ok
    for i in range(rows):
        for j in range(cols):
            if broth_grid[i][j] == 1:
                dfs(i, j, rows, cols,
                    broth_grid)  # rekurencyjnie aktualizuję tablicę (komórki sąsiadujące wg. von Neumanna, które miały 1 teraz otrzymują 0)
                count += 1  # modyfikujemy couter (pozbyliśmy się z tablicy jednego oka rosołu)
    return count

# ###############################
# # don't modify the code below #
# ###############################
# if __name__ == "__main__":
#     if "--debug" in sys.argv:
#         from run_tests import run_tests
#
#         run_tests()
#     else:
#         raw_input = parse_input(input(), os.path.abspath(__file__))
